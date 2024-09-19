import pandas as pd

# Carregar o DataFrame
df = pd.read_csv('/data/ecommerce_ex4.csv', encoding='utf-8')

# Converter a coluna 'Desconto' para string
df['Desconto'] = df['Desconto'].astype(str)

# Extrair e limpar os dados da coluna 'Condicao'
# Extrair a primeira parte da coluna 'Condicao' e remover espaços extras
df['Condicao_Atual'] = df['Condicao'].apply(lambda x: x.split(' | ')[0].strip() if ' | ' in x else x.strip())

# Extrair a quantidade de itens vendidos
df['Qtd_Vendidos'] = df['Condicao'].apply(lambda x: x.split(' ')[-2] if ' | ' in x and len(x.split(' | ')) > 1 else 'Nenhum')

# Modificar a coluna 'Desconto' para exibir apenas o valor numérico
df['Desconto'] = df['Desconto'].apply(lambda x: x.replace('% OFF', '').strip() if '% OFF' in x else x.strip())

# Exibir o DataFrame resultante para conferência
print(df.head())
