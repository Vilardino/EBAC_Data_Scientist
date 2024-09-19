# Preparação dos Dados

Para a preparação dos dados, siga os passos abaixo:

## Passo a Passo

### 1. Verificar a Quantidade de Dados Únicos
- Verifique a quantidade de **dados únicos** para cada campo.
- Armazene o resultado na variável `unicos`.

### 2. Verificar Estatísticas dos Campos Numéricos
- Verifique as **estatísticas** dos campos numéricos.
- Armazene o resultado na variável `estatisticas`.

### 3. Criar o Campo 'Preco'
- Crie o campo `'Preco'` com o cálculo baseado nos campos `Reais` e `Centavos`:
  - Fórmula: `Preco = Reais + (Centavos / 100)`
- O novo campo deve ser criado no mesmo DataFrame `df`.

### 4. Remover Campos Específicos
- Remova os seguintes campos do DataFrame `df`: `['Reais', 'Centavos', 'Condicao', 'Condicao_Atual']`.
- A remoção deve ser feita no mesmo DataFrame `df`.
