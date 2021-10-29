import sys
sys.path.insert(0, '.')

if __name__ == '__main__':
    
    from teste.roda_query import *
    from controle.bd import connect_bd
    
    maneger = connect_bd(sys.argv[1])
    
    maneger.query(open(valida_query(sys.argv[2])).read())
    maneger.close_bd()
    
    print('Processo Finalizado com sucesso!!!')