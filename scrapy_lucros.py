import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO

cabecalho = {'user-agent': 'Mozilla/5.0'}

#Criando um dicionário para as urls que são diferentes dos nomes
banco_urls = {
    'caixa': 'https://www.bancodata.com.br/relatorio/caixa-economica-federal/',
    'banco do brasil': 'https://www.bancodata.com.br/relatorio/bb/',
    'paypal': 'https://www.bancodata.com.br/relatorio/10878448/'
}

banco = input("Informe o banco que deseja saber sobre: ").lower()
print(f"Banco selecionado: {banco}")

#Lógica para pesquisar se o banco informado existe dentro da lista de urls
if banco in banco_urls:
    url_banco = banco_urls[banco]
else:
    url_banco = f"https://www.bancodata.com.br/relatorio/{banco}/"


response = requests.get(url_banco, headers = cabecalho)
sopa_bonita = BeautifulSoup(response.text, 'html.parser')

def extrair_infos_banco(sopa_bonita):
   tabela_banco = sopa_bonita.find('table', {"class": "table table-striped table-hover"})
   dados = {}
   tabela_banco_str = str(tabela_banco)
   tabela_banco_io = StringIO(tabela_banco_str)
   dados = pd.read_html(tabela_banco_io)[0]
   return dados

def extrair_infos_ul(sopa_bonita):
    main_info = sopa_bonita.find_all('div', {"main-info"})
    ul = sopa_bonita.find('ul', {"statistics"})
    span_info = ul.find_all('span')
    dados = {}
    for span, valores in zip(span_info, main_info):
        nome_span = span.text.strip()
        nome_val = valores.find('strong').text.strip()
        dados[nome_span] = nome_val
    return dados

def extrair_tabela_liquido(sopa_bonita):
   tabelas_tri_liqui = sopa_bonita.find_all('table', {"class": "table table-bordered"})
   dados = {}
   tabela_liquido_str = str(tabelas_tri_liqui)
   tabela_liquido_io = StringIO(tabela_liquido_str)
   dados = pd.read_html(tabela_liquido_io)[0]
   return dados

def extrair_tabela_trimestral(sopa_bonita):
   tabelas_tri_liqui = sopa_bonita.find_all('table', {"class": "table table-bordered"})
   dados = {}
   tabela_trimestral_str = str(tabelas_tri_liqui)
   tabela_trimestral_io = StringIO(tabela_trimestral_str)
   dados = pd.read_html(tabela_trimestral_io)[1]
   return dados


#A função read_html é usada pois transformamos nossa tabela em uma unica variavel por isso é melhor utilizar ele do que o DataFrame normal...
#o read_html vai retornar uma lista de dataframes, por isso que sem utilizar o [0] ele vem com as chaves, pq ta acessando uma lista de dataframes, utilizando o [0] pegamos só o primeiro elemento e assim a exibição da tabela fica bonitinha
