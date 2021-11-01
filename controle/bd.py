import psycopg2 as pg
from psycopg2 import connect, extras
import os
from json import load


class BD:
    conn = None

    def __init__(self, conf):
        self.conf = conf
    
    def connect(self):
        return pg.connect(host = self.__conf['host'],
                        database = self.__conf['database'],
                        user = self.__conf['user'],
                        password = self.__conf['pwd'])
    @property
    def conf(self):
        return self.__conf
  
    @conf.setter
    def conf(self, conf):
        self.__conf = conf
        self.__conn = self.connect()

    @property
    def conn(self):
        return self.__conn

    def query(self, script:str):
        with self.conn.cursor() as cursor:
            cursor.execute(script)
            
        self.conn.commit()
    
    def get_results_query(self, query):

        with self.conn.cursor(cursor_factory=extras.DictCursor) as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
            colunas = [x[0] for x in cursor.description]
        self.conn.commit()
        
        results_dict = {}

        a = 0
        for coluna in colunas:
            results_dict[coluna] = []
            [results_dict[coluna].append(x[a]) for x in results]

            a += 1
        
        return results_dict

    def insert_df_pandas(self, df, tabela):
        self.constraints_on()

        insert = f'''
            INSERT INTO {tabela} ({", ".join(tuple(df.columns))}) VALUES ({", ".join(['%s']*len(df.columns))})
        '''    
        
        with self.conn.cursor() as cursor:
            cursor.executemany(insert, [tuple(x) for x in df.values])
        self.conn.commit()

        print(f'Processo de insercao na tabela {tabela} concluido.')
        self.constraints_off()

    def insert_list(self, lista:list, colunas:list, tabela:str):
        self.constraints_on()

        insert = f'''
            INSERT INTO {tabela} ({", ".join(colunas)}) VALUES ({", ".join(['%s']*len(lista))})
        '''

        self.conn = self.connect()
        
        with self.conn.cursor() as cursor:
            cursor.executemany(insert, [tuple(x) for x in lista])
        self.conn.commit()

        print(f'Processo de insercao na tabela {tabela} concluido.')
        self.constraints_off()
        
    @staticmethod
    def procurar_padrao(string, padrao):
        if string.find(padrao) >= 0:
            return True
        else:
            return False
    
    @staticmethod
    def colunas_tabela(coluna, tipo):
            if BD.procurar_padrao(tipo, 'int'):
                return f"\n         {coluna} integer"
            elif BD.procurar_padrao(tipo, 'float'):
                return f"\n         {coluna} decimal(10,2)"
            elif BD.procurar_padrao(tipo, 'object'):
                return f"\n         {coluna} text"
            elif BD.procurar_padrao(tipo, 'date'):
                return f"\n         {coluna} date" 
    
    def return_tables(self):
        return self.get_results_query("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")

    def constraints_on(self):
        self.query('set session_replication_role to replica')

    def constraints_off(self):
        self.query('set session_replication_role to default;')

    def create_table_pandas(self, df, tabela = 'TABLE_NAME', PK = 'id_table'):
        '''
        Função utilizada para criar uma tabela no banco e inserir os dados disponiveis
        '''
    
        table = """
        CREATE TABLE IF NOT EXISTS TABLE_NAME(
        id_table serial primary key,
        """

        a = 0

        for coluna, valores in df.iteritems():
            if a < (df.shape[1] - 1):
                table = table + BD.colunas_tabela(coluna, str(valores.dtype)) + ','
            else:
                table = table + BD.colunas_tabela(coluna, str(valores.dtype))
            
            a += 1

        table = table + '\n);'
        if tabela != 'TABLE_NAME':
            table = table.replace('TABLE_NAME', tabela)

        if PK != 'id_table':
            table = table.replace('id_table', PK)
        
        print(f'{table}')
        self.query(table)
        self.insert_df_pandas(df, tabela)

        print(f'Processo de criacao e insercao na tabela {tabela} concluido.')
    
    def close_bd(self):
        return self.conn.close()

def connect_bd(conf):
    path = os.path.join('.', 'conf' ,conf)
    try:
        config = load(open(path))

        return BD(config)
    except:
        raise Exception('Arquivo conf incorreto') from None