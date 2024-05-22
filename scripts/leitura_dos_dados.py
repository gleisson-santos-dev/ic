import os
import pandas as pd
import numpy as np
#-------------------------- funçoes usadas ---------------------------
def to_df(caminho):
    nome_arq = []
    conjunto_de_dados = []
    nome_arq = os.listdir(caminho)
    for i in range(len(nome_arq)):
        df = pd.read_csv(caminho+'\\'+nome_arq[i], delimiter='\t')
        conjunto_de_dados.append(df)
    return conjunto_de_dados

def gera_pasta(caminho, nomes, conjunto):
    os.chdir(caminho)
    for i in range(len(conjunto)):
        print("criando o arquivo: "+nomes[i]+".csv")
        conjunto[i].to_csv(nomes[i]+".csv", index= False)

#----------------------------leitura dos dados-------------------------------------------------------------
caminho_pasta_1 = 'C:\\Users\\gleisson\\Desktop\\iniciação cientifica\\data\\1st_test\\1st_test'
caminho_pasta_2 = 'C:\\Users\\gleisson\\Desktop\\iniciação cientifica\\data\\2nd_test\\2nd_test'
caminho_pasta_3 = 'C:\\Users\\gleisson\\Desktop\\iniciação cientifica\\data\\3rd_test\\4th_test\\txt'

conjunto_1 = to_df(caminho_pasta_1)
print("conjunto 1 gerado!")

conjunto_2 = to_df(caminho_pasta_2)
print("conjunto 2 gerado!")

conjunto_3 = to_df(caminho_pasta_3)
print("conjunto 3 gerado")

#------------------adicionando descrição aus dados-----------------------------------------------
 
for i in range(len(conjunto_1)):
    conjunto_1[i].columns = ['rolamento 1', 'rolamento 2', 'rolamento 3', 'rolamento 4', 'rolamento 5', 'rolamento 6', 'rolamento 7', 'rolamento8']

for i in range(len(conjunto_2)):
    conjunto_2[i].columns = ['rolamento1', 'rolamento2', 'rolamento3', 'rolamento4']
    
for i in range(len(conjunto_3)):
    conjunto_3[i].columns = ['rolamento1', 'rolamento2', 'rolamento3', 'rolamento4']

