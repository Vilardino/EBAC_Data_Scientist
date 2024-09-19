# Continuação do Projeto: Filtragem por Quantidade de Comentários

Para filtrar os produtos com as maiores quantidades de comentários (`N_Avaliações`), utilizaremos o método do Intervalo Interquartil (IQR). 

## Passo a Passo

### 1. Calcular o Intervalo Interquartil (IQR)
- O IQR é a diferença entre o terceiro quartil (Q3) e o primeiro quartil (Q1).
  - `iqr = q3 - q1`

### 2. Determinar o Limite Superior para Outliers
- O limite superior é calculado como:
  - `limite_alto = q3 + 1.5 * iqr`

### 3. Filtrar Produtos Acima do Limite
- Filtre os produtos que têm `N_Avaliações` maior que `limite_alto`.
- Armazene o resultado na variável `df_avaliados`.
