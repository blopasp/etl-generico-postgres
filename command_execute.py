import os
from controle.bd import connect_bd
import psycopg2

def search(string, padrao):
    return string.__contains__(padrao)

if __name__ == '__main__':
    import os, sys
    from controle.bd import connect_bd

    nao_rodaram = []
    for raiz, diretorio, arquivos in os.walk('.'):
        if search(raiz, sys.argv[1]):
            for f in arquivos:
                try:
                    if f.endswith('.sql'):
                        connect_bd('connect.json')\
                            .query(open(os.path.join(raiz,f)).read())
                        print(f'Comando do arquivo {f} executado com sucesso')
                except: nao_rodaram.append(os.path.join(raiz,f))
    # nao_rodaram[::-1] retorna lista de tras pra frente
    for caminho in nao_rodaram[::-1]:
        try:
            connect_bd('connect.json')\
                .query(open(caminho).read())
            print(f'Comando do arquivo {caminho} executado com sucesso')
        except psycopg2.errors.SyntaxError as error: 
            print(f'\nComando do arquivo {caminho} falhou, erro de sintaxe\n\n{error}\n')
        except psycopg2.errors.UndefinedFunction as error:
            print(f'\nComando do arquivo {caminho} falhou, funcao nao encontrada\n\n{error}\n')