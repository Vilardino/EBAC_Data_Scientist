import requests
from bs4 import BeautifulSoup
import pandas as pd
requests.packages.urllib3.disable_warnings()

url = 'https://books.toscrape.com/'
requisicao = requests.get(url)
requisicao.encoding = 'utf-8'

extracao = BeautifulSoup(requisicao.text, 'html.parser')

contar_livros = 0
catalogo = []

# Função para truncar o título baseado em número de palavras
def truncar_titulo_palavras(titulo, limite_palavras=4):
    palavras = titulo.split()  # Quebrar o título em palavras
    if len(palavras) > limite_palavras:
        return ' '.join(palavras[:limite_palavras]) + ' ...'
    return titulo

# Iterando pelos artigos de livros
for artigo in extracao.find_all('article', class_='product_pod'):
    livro = {}

    # Extraindo o título do livro e truncando pelo número de palavras
    titulo = artigo.find('h3').find('a')['title']
    livro['Título'] = truncar_titulo_palavras(titulo)

    # Extraindo o preço do livro
    preco = artigo.find('p', class_='price_color').text
    livro['Preço'] = preco

    # Adicionando o livro ao catálogo
    catalogo.append(livro)

    # Incrementando a contagem de livros
    contar_livros += 1

# Exibindo o total de livros
print('Total livros:', contar_livros)

# Exibindo o catálogo de livros com título e preço
titulos = [livro['Título'] for livro in catalogo]
precos = [livro['Preço'] for livro in catalogo]

print(titulos)
print(precos)
