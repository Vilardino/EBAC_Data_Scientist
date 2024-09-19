import pandas as pd

# Carregar o DataFrame
df = pd.read_csv('/data/ecommerce_tratados_ex3.csv')

# Dicionário para transformar Qtd_Vendidos em números
qtd_vendidos_dict = {
    'Nenhum': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '+5': 5,
    '+25': 25,
    '+50': 50,
    '+100': 100,
    '+1000': 1000,
    '+10mil': 10000,
    '+50mil': 50000
}

# Criar o campo Qtd_Vendidos_Cod
df['Qtd_Vendidos_Cod'] = df['Qtd_Vendidos'].map(qtd_vendidos_dict)

# Criar o campo Marca_Freq com a frequência relativa dos valores de Marca
marca_freq = df['Marca'].value_counts(normalize=True).to_dict()
df['Marca_Freq'] = df['Marca'].map(marca_freq)

# Criar o campo Material_Freq com a frequência relativa dos valores de Material, incluindo NaN
material_freq = df['Material'].value_counts(normalize=True, dropna=False).to_dict()
df['Material_Freq'] = df['Material'].map(material_freq)

# Manter os valores NaN originais na coluna Material_Freq
df.loc[df['Material'].isna(), 'Material_Freq'] = float('nan')

# Exibir as primeiras linhas do DataFrame para verificar as transformações
print(df.head())
