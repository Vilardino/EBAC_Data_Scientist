import pandas as pd

df = pd.read_csv('/data/ecommerce.csv')

# Verifique a quantidade de linhas e colunas
linhas_colunas = df.shape
print('Verificar a qtd de Linhas e colunas: ', linhas_colunas)

# Verifique os tipos de dados
tipos = df.dtypes
print('Verificar Tipagem:\n', tipos)

# Verifique a quantidade de valores nulos
nulos = df.isnull().sum()
print('Verificar valores nulos:\n', nulos)

# Substitua os valores nulos das colunas ‘Temporada’ e ‘Marca’ por ‘Não Definido’
df['Temporada'].fillna('Não Definido', inplace=True)
df['Marca'].fillna('Não Definido', inplace=True)

# Verifique novamente a quantidade de valores nulos para confirmar a substituição
nulos_apos_substituicao = df.isnull().sum()
print('Verificar valores nulos após substituição:\n', nulos_apos_substituicao)

