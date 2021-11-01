import pandas as pd
from controle.bd import connect_bd
import unicodedata
from glob import glob


def open_csv_pandas(path):
    chunks = []
    try:
        for chunk in pd.read_csv(path, delimiter = ';',chunksize=50000, encoding='latin-1'):
            chunks.append(chunk)
        return pd.concat(chunks)
    except:
        for chunk in pd.read_csv(path, delimiter = ',' ,chunksize=55000, encoding='latin-1'):
            chunks.append(chunk)
        return pd.concat(chunks)

def remove_accent(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')\
                      .strip()\
                      .replace(' ', '_')
                      
def fit_column(df):
    return [remove_accent(column) for column in df.columns]

def etl_df(path, tipo_arquivo, table):
    paths = glob(path+'\\*.'+tipo_arquivo)

    for path in paths:
        df = open_csv_pandas(path)
        df.columns = fit_column(df)

        try:
            connect_bd('connect.json').insert_df_pandas(df, table)
            print(f'Arquivo {path} inserido com sucesso')
        except:
            connect_bd('connect.json').create_table_pandas(df.loc[:0], table)
            connect_bd('connect.json').insert_df_pandas(df.loc[1:], table)
            print(f'Arquivo {path} inserido com sucesso')
        

if __name__ == '__main__':
    etl_df(r'C:\Users\012019631\Downloads\Receitas', 'csv', 'receitas_governo_federal')

connect_bd('connect.json').return_tables()
