# Finalização do Exercício: Tratamento de Colunas

Para concluir o tratamento dos dados, realizaremos as seguintes etapas:

## Passo a Passo

### 1. Converter a Coluna 'Desconto' para Tipo String
- Converta a coluna `'Desconto'` para o tipo **string**.

### 2. Modificar a Coluna 'Desconto' para Exibir Apenas o Valor Numérico
- Modifique a coluna `'Desconto'` para exibir apenas o valor numérico do desconto.
  - Exemplo: "18% OFF" deve se tornar "18".

### 3. Criar Novas Colunas Baseadas na Coluna 'Condicao'
- **Condicao_Atual**: Extraia a primeira parte do campo `'Condicao'`.
  - Exemplo: "Novo | +10mil vendidos" deve se tornar "Novo".
- **Qtd_Vendidos**: Extraia a quantidade de itens vendidos do campo `'Condicao'`.
  - Exemplo: "Novo | +10mil vendidos" deve se tornar "+10mil".
  - Se não houver quantidade especificada, escreva "Nenhum".

### Nota Adicional
- Caso queira explorar outra solução, você pode usar a função `assign` para adicionar ou modificar várias colunas de um DataFrame de maneira encadeada. 
- Você pode passar funções lambda dentro do `assign` para aplicar transformações nas colunas.

Saiba mais: Caso queria explorar outra solução, você pode usar a função `assign` para adicionar ou modificar várias colunas de um DataFrame de maneira encadeada. Lembre-se de que você pode passar funções lambda dentro do `assign` para aplicar transformações nas colunas:

```python
df = pd.read_csv('/data/ecommerce_ex4.csv', encoding='utf-8').assign(
  # Adicione suas transformações aqui
)
