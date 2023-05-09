import xml.etree.ElementTree as ET

print('----------Validador de NFs----------')
arqinp = str(input('Digite o nome do arquivo: '))
arq = arqinp + '.xml'
root = ET.parse(arq).getroot()

nsNFe = {"ns": "http://www.portalfiscal.inf.br/nfe"}
numNF = root.find("./ns:NFe/ns:infNFe/ns:ide/ns:nNF", nsNFe).text

c = 0
n = 1
itens = []
for item in root.findall("./ns:NFe/ns:infNFe/ns:det", nsNFe):
    cod = str(root.findall("./ns:NFe/ns:infNFe/ns:det/ns:prod/ns:xProd", nsNFe)[c].text)
    ncm = root.findall("./ns:NFe/ns:infNFe/ns:det/ns:prod/ns:NCM", nsNFe)[c].text
    ncm = str(f'{ncm[:4]}.{ncm[4:6]}.{ncm[6:]}')
    origem = int(root.findall("./ns:NFe/ns:infNFe/ns:det/ns:imposto/ns:ICMS/ns:ICMS00/ns:orig", nsNFe)[c].text)
    qtd = float(root.findall("./ns:NFe/ns:infNFe/ns:det/ns:prod/ns:qCom", nsNFe)[c].text)
    val_unit = float(root.findall("./ns:NFe/ns:infNFe/ns:det/ns:prod/ns:vUnCom", nsNFe)[c].text)
    bc_icms = float(root.findall("./ns:NFe/ns:infNFe/ns:det/ns:imposto/ns:ICMS/ns:ICMS00/ns:vBC", nsNFe)[c].text)
    #if root.findall("./ns:NFe/ns:infNFe/ns:det/ns:imposto/ns:ICMS/ns:ICMS00", nsNFe) == True:
    aliq_icms = float(root.findall("./ns:NFe/ns:infNFe/ns:det/ns:imposto/ns:ICMS/ns:ICMS00/ns:pICMS", nsNFe)[c].text)
    val_icms = float(root.findall("./ns:NFe/ns:infNFe/ns:det/ns:imposto/ns:ICMS/ns:ICMS00/ns:vICMS", nsNFe)[c].text)
    #elif root.findall("./ns:NFe/ns:infNFe/ns:det/ns:imposto/ns:ICMS/ns:ICMS10", nsNFe) == True:
    #aliq_icms = float(root.findall("./ns:NFe/ns:infNFe/ns:det/ns:imposto/ns:ICMS/ns:ICMS10/ns:pICMS", nsNFe)[c].text)
    #val_icms = float(root.findall("./ns:NFe/ns:infNFe/ns:det/ns:imposto/ns:ICMS/ns:ICMS10/ns:vICMS", nsNFe)[c].text)
        #aliq_icmsst = float(root.findall("./ns:NFe/ns:infNFe/ns:det/ns:imposto/ns:ICMS/ns:ICMS10/ns:pICMSST", nsNFe)[c].text)
        #val_icmsst = float(root.findall("./ns:NFe/ns:infNFe/ns:det/ns:imposto/ns:ICMS/ns:ICMS10/ns:vICMSST", nsNFe)[c].text)
    if root.findall("./ns:NFe/ns:infNFe/ns:det/ns:imposto/ns:IPI/ns:IPITrib/ns:pIPI", nsNFe) == True:
        aliq_ipi = float(root.findall("./ns:NFe/ns:infNFe/ns:det/ns:imposto/ns:IPI/ns:IPITrib/ns:pIPI", nsNFe)[c].text)
        val_ipi = float(root.findall("./ns:NFe/ns:infNFe/ns:det/ns:imposto/ns:IPI/ns:IPITrib/ns:vIPI", nsNFe)[c].text)
    else:
        aliq_ipi = 0
        val_ipi = 0
    valor_ped = val_unit * ((aliq_ipi+100)/100)
    dados_materiais = [f'Material-{n}', cod, ncm, origem, qtd, val_unit, bc_icms, aliq_icms, val_icms, aliq_ipi, val_ipi, valor_ped]
    itens.append(dados_materiais)
    n += 1
    c += 1

print(f'NF {numNF}')
print(f'A NF tem {len(itens)} material(is)')
for x in range(len(itens)):
    print(f'{itens[x][0]}: \n '
        f'{itens[x][1]} - Qtd: {itens[x][4]} \n'
          f'NCM: {itens[x][2]} e Origem: {itens[x][3]} \n'
          f'Valor no pedido: R$ {itens[x][11]} e BC: R$ {itens[x][6]} \n'
          f'Alíquota ICMS: {itens[x][7]}% e Valor ICMS: R$ {itens[x][8]} \n'
          f'Alíquota IPI: {itens[x][9]}% e Valor IPI: R$ {itens[x][10]} \n')