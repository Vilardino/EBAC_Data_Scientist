# Extração de Dados: Título e Preço dos Livros

## Objetivo
Neste exercício, vamos extrair o **título** e o **preço** dos livros listados na primeira página do site [books.toscrape.com](https://books.toscrape.com/). Para isso, seguiremos os passos abaixo.

## Parte 1: Extraindo Título e Preço

### Passos

1. **Encontrar a tag `<h3>` dentro da tag `<article>`**:
   - Crie um `for` loop para percorrer todas as tags `<article>` no código-fonte da página.
   - Dentro de cada `<article>`, encontre a tag `<h3>`, que contém o título do livro.
   - Extraia os textos da tag `<h3>` e armazene na variável `titulo`.

2. **Atualizar o valor de `livro['Título']`**:
   - Use a variável `titulo` para atualizar o campo `livro['Título']`.

3. **Encontrar a tag `<p class='price_color'>`**:
   - Crie um segundo `for` loop dentro da tag `<article>` para encontrar a tag `<p>` com a classe `price_color` utilizando o comando `findall('p', class_='price_color')`.
   - Extraia os textos da tag `<p>` e armazene na variável `preco`.

4. **Atualizar o valor de `livro['Preço']`**:
   - Use a variável `preco` para atualizar o campo `livro['Preço']`.

