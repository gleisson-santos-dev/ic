import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
import time

# Inicialização do tempo
start_time = time.time()

# Carregar dados
file_A = 'C:\\Users\\gleisson\\Desktop\\gitHub\\ic\aquivos de trinamento e validação\\input_RNA_com_falha_emb.xlsx'
file_B = 'C:\\Users\\gleisson\\Desktop\\gitHub\\ic\\aquivos de trinamento e validação\\input_RNA_sem_falha_emb.xlsx'
amostras_70_A = pd.read_excel(file_A).values
amostras_70_B = pd.read_excel(file_B).values

# Concatenar dados
amostras_70 = np.vstack((amostras_70_A, amostras_70_B))
np.random.shuffle(amostras_70)

# Separar entradas e saídas
X = amostras_70[:, :-1]
y = amostras_70[:, -1]

# Adicionar coluna de bias
X = np.hstack((np.ones((X.shape[0], 1)) * -1, X))

# Definir modelo
model = Sequential()
model.add(Dense(1, input_dim=X.shape[1], activation='tanh', use_bias=False))

# Definir otimizador
sgd = SGD(learning_rate=1e-3)

# Compilar modelo
model.compile(loss='hinge', optimizer=sgd, metrics=['accuracy'])

# Treinar modelo
model.fit(X, y, epochs=20000, verbose=0)

# Mostrar pesos finais
weights = model.get_weights()[0]
print("Os pesos finais 'W_final' valem:")
print(weights.flatten())

# Carregar dados de teste
file_1 = 'C:\\Users\\gleisson\\Desktop\\gitHub\\ic\\aquivos de trinamento e validação\\Execução_RNA.xlsx'
dados = pd.read_excel(file_1).values

# Preparar dados de teste
dados = np.hstack((np.ones((dados.shape[0], 1)) * -1, dados))

# Fazer predições
predictions = model.predict(dados)
predictions = np.where(predictions >= 0, 1, -1)

# Comparar com a saída ideal
saida_ideal_file = 'C:\\Users\\gleisson\\Desktop\\gitHub\\ic\\aquivos de trinamento e validação\\saida_ideal.xlsx'
saida_ideal = pd.read_excel(saida_ideal_file).values.flatten()

erro_final = np.mean(predictions.flatten() != saida_ideal) * 100
print('Erro percentual da rede é de:')
print(erro_final)

# Tempo de processamento
elapsed_time = time.time() - start_time
print('Tempo de processamento da rede é de:')
print(elapsed_time)
