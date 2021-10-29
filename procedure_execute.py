import os
from controle.bd import connect_bd

def search(string, padrao):
    return string.__contains__(padrao)

if __name__ == '__main__':
    import os
    from controle.bd import connect_bd

    for raiz, diretorio, arquivos in os.walk('.'):
        if search(raiz, 'call_procedure'):
            for f in arquivos:
                if f.endswith('.sql'):
                    connect_bd('connect.json')\
                        .query(open(os.path.join(raiz,f)).read())
                