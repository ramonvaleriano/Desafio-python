"""
Program: desafio_python -> main.py
Author: Ramon R. Valeriano
Description: Algoritmo desenvolvivo com o intuito de validar teste admissional.
Developed: 17/02/2020 - 11:00

"""

from urllib import request # Biblioteca usada para coletar dados da internet
from zipfile import ZipFile # Biblioeca usada para ler dados zipados, nesse caso vamos ler e descompactar
from io import BytesIO # Biblioteca usada para entrada e saída de arquivos.

import pandas as pd # Biblioteca usada para a leitura de dados.
import json # Transformar os dados no formado Json.
import os # Ler detalhes diretamente do sistema operacional.



def identificacao(dados):
    '''
    Função que fara todo o processo de criar o retorno de dados no formado json. Irá
    filtrar e retonar o objeto no formato jason
    :param dados: Dados coletados do banco do dados.
    '''

    colunas_desejadas = ['REF_AREA', 'ENERGY_PRODUCT', 'FLOW_BREAKDOWN', 'UNIT_MEASURE']
    dados_filtrados = pd.DataFrame(dados, columns=colunas_desejadas)
    dados_filtrados['TIME_PERIOD'] = pd.to_datetime(dados['TIME_PERIOD'])
    quantidade = len(dados_filtrados)

    for i in range(quantidade):
        lista1 = list(dados_filtrados.iloc[i])
        lista2 = list(dados['TIME_PERIOD'][(dados_tratados['REF_AREA'] == lista1[0])])
        print(lista1)
        nome = lista1[0]+lista1[1]+lista1[2]+lista1[3]
        print(nome)
        dicionario = {
            "series_id": nome,
            'points':lista2,
            "fields":{
                "country": lista1[0],
                "product": lista1[1],
                "flow": lista1[2],
                "unit measure":lista1[3]
            }
        }
        # Transformando os dados em json
        resultado = json.dumps(dicionario)
        resultado = json.loads(resultado)
        print(resultado)

#Coletando dados do da web
dados_zipados = request.urlopen("https://www.jodidata.org/_resources/files/downloads/gas-data/jodi_gas_csv_beta.zip")

#Verificando se a uma pasta para por o arquivo, se não houver, criar tal pasta.
if  os.path.exists("data") != True:
    os.mkdir("data")

#Descompactando o arquivo zipado da internet.
descompactar = ZipFile(BytesIO(dados_zipados.read()))
descompactar.extractall("data")
descompactar.close()

#Realizando a leitura do arquivo
arquivo = 'data/jodi_gas_beta.csv'
dados = pd.read_csv(arquivo, sep=',')

#Definindo as colunasd desejadas
colunas= ['REF_AREA', 'ENERGY_PRODUCT', 'FLOW_BREAKDOWN', 'UNIT_MEASURE',
                             'TIME_PERIOD']

#Filtrando os dados pelas colunas desejadas
dados_tratados = pd.DataFrame(dados, columns=colunas)
identificacao(dados_tratados)


