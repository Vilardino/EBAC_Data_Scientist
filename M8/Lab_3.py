import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('/data/ecommerce_ex3.csv')

# Calcular o intervalo interquartil (IQR) para a coluna 'N_Avaliacoes'
q1 = df['N_Avaliacoes'].quantile(0.25)
q3 = df['N_Avaliacoes'].quantile(0.75)
iqr = q3 - q1

# Definir o limite superior para identificar outliers
limite_alto = q3 + 1.5 * iqr

# Filtrar os produtos que possuem um número de avaliações maior que o limite superior
df_avaliados = df[df['N_Avaliacoes'] > limite_alto]

# Exibir o DataFrame filtrado
print(df_avaliados)
