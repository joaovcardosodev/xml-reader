import sqlite3
from sqlite3.dbapi2 import Cursor

class DataBase():
    def __init__(self, name = "system.db") -> None:
        self.name = name
    
    def conecta(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass

    def create_table_nfe(self):

        cursor = self.connection.cursor()

        cursor.execute(f"""

            CREATE TABLE IF NOT EXISTS Notas(
            
            NFe TEXT,
            Chave TEXT,
            Pedido TEXT,
            Item TEXT,
            Fornecedor TEXT,
            Quantidade TEXT,                
            Preço TEXT,
            NCM TEXT,
            Origem TEXT,
            Alíquota_ICMS TEXT,
            Valor_ICMS TEXT,
            Alíquota_IPI TEXT,
            Valor_IPI TEXT,
            Alíquota_ICMSST TEXT,
            Valor_ICMSST TEXT,

        
        PRIMARY KEY(Chave, NFe)                
            );
        """)

    def insert_data(self, full_dataset):
        cursor = self.connection.cursor()
        campos_tabela = (
            'NFe','Chave','Pedido','Item','Fornecedor','Quantidade',
             'Preço','NCM','Origem','Alíquota_ICMS','Valor_ICMS','Alíquota_IPI','Valor_IPI',
             'Alíquota_ICMSST','Valor_ICMSST')  
        qtd = ','.join(map(str, '?'*15))
        query = f"""INSERT INTO Notas {campos_tabela} VALUES ({qtd}) """
        
        try:
            for nota in full_dataset:
                cursor.execute(query, tuple(nota))
                self.connection.commit()
        except sqlite3.IntegrityError:
            print('Nota já existe no banco')

if __name__ == "__main__":

    db = DataBase()
    db.conecta()
    db.create_table_nfe()
    db.close_connection()