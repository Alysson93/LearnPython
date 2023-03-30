import pandas as pd

# dados = pd.read_excel('camihho/do/arquivo') # Para ler excel

dados = pd.read_csv('arquivos/atletas.csv') # Para ler csv

print(dados.head(2)) # Para ler as primerias linhas (5 por padrão)
print()

print(dados.shape) # Exibe o número de linhas e colunas do df
print()

print(dados.describe()) # Traz informações sobre os dados numéricos
print()

print('Pandas version:', pd.__version__)