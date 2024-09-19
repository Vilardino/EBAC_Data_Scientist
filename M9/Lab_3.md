# Finalização da Preparação dos Dados

Para concluir a preparação dos dados, siga os passos abaixo:

## Passo a Passo

### 1. Criar o Campo 'Qtd_Vendidos_Cod'
- Crie o campo `'Qtd_Vendidos_Cod'` com a transformação do campo `'Qtd_Vendidos'` para números de acordo com suas grandezas. Utilize a seguinte correspondência:
  - `'Nenhum'` = 0
  - `'1'` = 1
  - `'2'` = 2
  - `'3'` = 3
  - `'4'` = 4
  - `'+5'` = 5
  - `'+25'` = 25
  - `'+50'` = 50
  - `'+100'` = 100
  - `'+1000'` = 1000
  - `'+10mil'` = 10000
  - `'+50mil'` = 50000

### 2. Criar o Campo 'Marca_Freq'
- Crie o campo `'Marca_Freq'` com a transformação do campo `'Marca'` para números de acordo com a frequência do valor.

### 3. Criar o Campo 'Material_Freq'
- Crie o campo `'Material_Freq'` com a transformação do campo `'Material'` para números de acordo com a frequência do valor.
