import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('/data/ecommerce_tratados.csv')

# Verifica a quantidade de dados únicos em cada coluna
unicos = df.nunique()
print('Análise de dados únicos:\n', unicos)

# Calcula estatísticas descritivas dos campos numéricos
estatisticas = df.describe()
print('Estatísticas dos dados:\n', estatisticas)

# Cria o campo "Preço" com o cálculo em relação aos campos "Reais" e "Centavos"
df['Preco'] = df['Reais'] + (df['Centavos'] / 100)

# Remove os campos 'Reais', 'Centavos', 'Condicao', 'Condicao_Atual'
df = df.drop(columns=['Reais', 'Centavos', 'Condicao', 'Condicao_Atual'])

# Exibe o DataFrame resultante
print(df.head())
