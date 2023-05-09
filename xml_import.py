import os
import xml.etree.ElementTree as ET

class read_xml():
    def __init__(self, directory) -> None:
        self.directory = directory
    
    def all_files(self):
        return [ os.path.join(self.directory, arq) for arq in os.listdir(self.directory) 
        if arq.lower().endswith(".xml")]
    
    def check_none(self, var):
        if var == None:
            return ""
        else:
            try:
                return var.text.replace('.',',')
            except:
                return var.text
    
    def nf_data(self, xml):
        root = ET.parse(xml).getroot()
        nsNFe = {"ns": "http://www.portalfiscal.inf.br/nfe"}
        numNF = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:nNF", nsNFe))
        chaveNF = self.check_none(root.find("./ns:protNFe/ns:infProt/ns:chNFe", nsNFe))
        fornecedor = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:xNome", nsNFe))

        item_nf = 1
        notas = []
        for item in root.findall("./ns:NFe/ns:infNFe/ns:det", nsNFe):
            pedido = self.check_none(item.find(".ns:prod/ns:xPed", nsNFe))
            item_pedido = self.check_none(item.find(".ns:prod/ns:nItemPed", nsNFe))
            qtd = self.check_none(item.find(".ns:prod/ns:qCom", nsNFe))
            val_unit = self.check_none(item.find(".ns:prod/ns:vUnCom", nsNFe))
            ncm = self.check_none(item.find(".ns:prod/ns:NCM", nsNFe))
            ncm = f'{ncm[:4]}.{ncm[4:6]}.{ncm[6:]}'
            aliq_ipi = self.check_none(item.find(".ns:imposto/ns:IPI/ns:IPITrib/ns:pIPI", nsNFe))
            val_ipi = self.check_none(item.find(".ns:imposto/ns:IPI/ns:IPITrib/ns:vIPI", nsNFe))
            if item.find(".ns:imposto/ns:ICMS/ns:ICMS00/ns:orig", nsNFe) == None:
                origem = self.check_none(item.find(".ns:imposto/ns:ICMS/ns:ICMS10/ns:orig", nsNFe))
                aliq_icms = self.check_none(item.find(".ns:imposto/ns:ICMS/ns:ICMS10/ns:pICMS", nsNFe))
                val_icms = self.check_none(item.find(".ns:imposto/ns:ICMS/ns:ICMS10/ns:vICMS", nsNFe))
                aliq_icmsst = self.check_none(item.find(".ns:imposto/ns:ICMS/ns:ICMS10/ns:pICMSST", nsNFe))
                val_icmsst = self.check_none(item.find(".ns:imposto/ns:ICMS/ns:ICMS10/ns:vICMSST", nsNFe))
            elif item.find(".ns:imposto/ns:ICMS/ns:ICMS10/ns:orig", nsNFe) == None:
                origem = self.check_none(item.find(".ns:imposto/ns:ICMS/ns:ICMS00/ns:orig", nsNFe))
                aliq_icms = self.check_none(item.find(".ns:imposto/ns:ICMS/ns:ICMS00/ns:pICMS", nsNFe))
                val_icms = self.check_none(item.find(".ns:imposto/ns:ICMS/ns:ICMS00/ns:vICMS", nsNFe))
                aliq_icmsst = ""
                val_icmsst = ""
            dados = [numNF, chaveNF, pedido, item_pedido, fornecedor, qtd, val_unit, ncm, origem, aliq_icms, val_icms, 
                     aliq_ipi, val_ipi, aliq_icmsst, val_icmsst]
            notas.append(dados)
            item_nf += 1
        return notas

if __name__ == "__main__":
    xml = read_xml('C:\\Users\\joaov\\Desktop\\Python\\Projeto NFs')
    all = xml.all_files()

    for i in all:
        result = xml.nf_data(i)

    print(result)
