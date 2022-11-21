import sys
sys.path.insert(0, '.')

from controle.bd import BD
from controle.bd import connect_bd
from json import load
import os
      
def list_path_queries():
    lista_caminhos = []
    
    for raiz, diretorio, arquivos in os.walk('.'):
        for f in arquivos:
            lista_caminhos.append(os.path.join(raiz,f))
    
    return lista_caminhos

def valida_query(querie:str):

    if not querie.endswith('.sql'):
        raise Exception("Por favor, insira um arquivo com o final '.sql'") from None

    caminhos = list(filter(lambda x: x.__contains__(querie) ,list_path_queries()))
    
    if len(caminhos) == 0:
        raise Exception('Arquivo inexistente!') from None
    
    elif len(caminhos) > 1:
        raise Exception('Voce digitou um nome generico. Por favor, digite exatamente o nome da query') from None
    
    else: return caminhos[0]