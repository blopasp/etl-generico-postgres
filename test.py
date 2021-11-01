from controle.bd import BD
from controle.bd import connect_bd
from json import load
import pandas as pd

maneger = BD(load(open('conf/connect.json')))

test = {'test': ['hoje']}
df = pd.DataFrame(test)

ins = "insert into test (test) values ('amanha');"

drop_table = 'drop table test;'
maneger.query(ins)
maneger.query(drop_table)
maneger.create_table_pandas(df, 'test')
maneger.query(ins)
maneger.return_tables()
#maneger.insert_list([['amanha', 'ontem']], ['test'], 'test')
maneger.close_bd()