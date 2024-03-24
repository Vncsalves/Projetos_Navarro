import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO


cabecalho = {'user-agent': 'Mozilla/5.0'}

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


#Criando um dicionário para as urls que são diferentes dos nomes
banco_urls = {
    'caixa': 'https://www.bancodata.com.br/relatorio/caixa-economica-federal/',
    'banco do brasil': 'https://www.bancodata.com.br/relatorio/bb/',
    'paypal': 'https://www.bancodata.com.br/relatorio/10878448/'
}


banco1 = input("Informe o primeiro banco que deseja comparar: ").lower()
banco2 = input("Informe o segundo banco que deseja comparar: ").lower()

#Lógica para pesquisar se o banco informado existe dentro da lista de urls
if banco1 in banco_urls:
    url_banco1 = banco_urls[banco1]
else:
    url_banco1 = f"https://www.bancodata.com.br/relatorio/{banco1}/"

if banco2 in banco_urls:
    url_banco2 = banco_urls[banco2]
else:
    url_banco2 = f"https://www.bancodata.com.br/relatorio/{banco2}/"


response1 = requests.get(url_banco1, headers=cabecalho)
response2 = requests.get(url_banco2, headers=cabecalho)

sopa_bonita1 = BeautifulSoup(response1.text, 'html.parser')
sopa_bonita2 = BeautifulSoup(response2.text, 'html.parser')

dados_banco1_ul = extrair_infos_ul(sopa_bonita1)
dados_banco2_ul = extrair_infos_ul(sopa_bonita2)

tabela_liquido_banco1 = extrair_tabela_liquido(sopa_bonita1)
tabela_liquido_banco2 = extrair_tabela_liquido(sopa_bonita2)

tabela_trimestral_banco1 = extrair_tabela_trimestral(sopa_bonita1)
tabela_trimestral_banco2 = extrair_tabela_trimestral(sopa_bonita2)

print(f"Dados do primeiro banco - {banco1}:")
print("Resumo do Último Balanço:")
print(dados_banco1_ul)
print("\n")

print("Tabela de Lucro Líquido:")
print(tabela_liquido_banco1)
print("\n")

print("Tabela Trimestral:")
print(tabela_trimestral_banco1)
print("\n")

print(f"\nDados do segundo banco - {banco2}:")
print("Resumo do Último Balanço:")
print(dados_banco2_ul)
print("\n")

print("Tabela de Lucro Líquido:")
print(tabela_liquido_banco2)
print("\n")

print("Tabela Trimestral:")
print(tabela_trimestral_banco2)