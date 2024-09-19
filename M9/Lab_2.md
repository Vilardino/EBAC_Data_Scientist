# Continuação da Preparação dos Dados

Para a continuação da preparação dos dados, siga os seguintes passos:

## Passo a Passo

### 1. Criar o Campo 'Nota_MinMax'
- Crie o campo `'Nota_MinMax'` com a transformação do campo `'Nota'` para numérico em uma escala de 0 a 1, utilizando o `MinMaxScaler`.

### 2. Criar o Campo 'N_Avaliações_MinMax'
- Crie o campo `'N_Avaliações_MinMax'` com a transformação do campo `'N_Avaliações'` para numérico em uma escala de 0 a 1, utilizando o `MinMaxScaler`.

### 3. Criar o Campo 'Desconto_MinMax'
- Crie o campo `'Desconto_MinMax'` com a transformação do campo `'Desconto'` para numérico em uma escala de 0 a 1, utilizando o `MinMaxScaler`.

### 4. Criar o Campo 'Preco_MinMax'
- Crie o campo `'Preco_MinMax'` com a transformação do campo `'Preco'` para numérico em uma escala de 0 a 1, utilizando o `MinMaxScaler`.

### 5. Criar o Campo 'Marca_Cod'
- Crie o campo `'Marca_Cod'` utilizando o método `LabelEncoder` para transformar o campo `'Marca'` em numérico.

### 6. Criar o Campo 'Material_Cod'
- Crie o campo `'Material_Cod'` utilizando o método `LabelEncoder` para transformar o campo `'Material'` em numérico.

### 7. Criar o Campo 'Temporada_Cod'
- Crie o campo `'Temporada_Cod'` utilizando o método `LabelEncoder` para transformar o campo `'Temporada'` em numérico.
