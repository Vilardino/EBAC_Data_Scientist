import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

# Carregar o arquivo CSV
df = pd.read_csv('/data/ecommerce_tratados_ex2.csv')

# Inicializando o MinMaxScaler
scaler = MinMaxScaler()

# Criando o campo Nota_MinMax
df['Nota_MinMax'] = scaler.fit_transform(df[['Nota']])

# Criando o campo N_Avaliacoes_MinMax
df['N_Avaliacoes_MinMax'] = scaler.fit_transform(df[['N_Avaliacoes']])

# Criando o campo Desconto_MinMax
df['Desconto_MinMax'] = scaler.fit_transform(df[['Desconto']])

# Criando o campo Preco_MinMax
df['Preco_MinMax'] = scaler.fit_transform(df[['Preco']])

# Inicializando o LabelEncoder
label_encoder = LabelEncoder()

# Criando o campo Marca_Cod
df['Marca_Cod'] = label_encoder.fit_transform(df['Marca'])

# Criando o campo Material_Cod
df['Material_Cod'] = label_encoder.fit_transform(df['Material'])

# Criando o campo Temporada_Cod
df['Temporada_Cod'] = label_encoder.fit_transform(df['Temporada'])

# Exibe o DataFrame resultante
print(df.head())
