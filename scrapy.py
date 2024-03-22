import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO

banco = input("Informe o banco que deseja saber sobre: ")
print(f"Banco selecionado: \n{banco}")

paypal = 10878448
bb = 'bb'
caixa = 'caixa-economica-federal'

cabecalho = {'user-agent': 'Mozilla/5.0'}
response = requests.get(f'https://www.bancodata.com.br/relatorio/{banco}/', headers = cabecalho)
if banco == "paypal":
  response = requests.get(f'https://www.bancodata.com.br/relatorio/{paypal}/')
elif banco == "banco do brasil":
  response = requests.get(f'https://www.bancodata.com.br/relatorio/{bb}/')
elif banco == "caixa":
  response = requests.get(f"https://www.bancodata.com.br/relatorio/{caixa}/")

response.text

sopao_macarronico = response.text
sopao_macarronico

sopa_bonita = BeautifulSoup(sopao_macarronico, 'html.parser')

#INFORMAÇÕES DO BANCO
tabela_banco = sopa_bonita.find('table', {"class": "table table-striped table-hover"})
tabela_banco_str = str(tabela_banco)
tabela_banco_io = StringIO(tabela_banco_str)

df_tabela_banco = pd.read_html(tabela_banco_io)[0]
print(df_tabela_banco)

tabelas_tri_liqui = sopa_bonita.find_all('table', {"class": "table table-bordered"})

tabela_liquido_str = str(tabelas_tri_liqui)
tabela_liquido_io = StringIO(tabela_liquido_str)
df_tabela_liquido = pd.read_html(tabela_liquido_io)[0]
print("\n")

tabela_trimestral_str = str(tabelas_tri_liqui)
tabela_trimestral_io = StringIO(tabela_trimestral_str)
df_tabela_trimestral = pd.read_html(tabela_trimestral_io)[1]
print("\n")

def extrair_infos(sopa_bonita):
    main_info = sopa_bonita.find_all('div', {"main-info"})
    ul = sopa_bonita.find('ul', {"statistics"})

    span_info = ul.find_all('span')

    dados = {}
    for span, valores in zip(span_info, main_info):
        nome_span = span.text.strip()
        nome_val = valores.find('strong').text.strip()

        dados[nome_span] = nome_val

    return dados

# Para utilizar a função
dados = extrair_infos(sopa_bonita)
print(dados)





print("\n")

tabela_indice = sopa_bonita.find('table', {"class": "table table-striped text-center"})
tabela_indice_str = str(tabela_indice)
tabela_indice_io = StringIO(tabela_indice_str)
df_tabela_indice = pd.read_html(tabela_indice_io)[0]



tabela = sopa_bonita.find('table', {"class": "table table-bordered"})
tabela_str = str(tabela) #Transformando a tabela inteira em uma string
tabela_str_io = StringIO(tabela_banco_str)

df_tabela = pd.read_html(tabela_str_io)[0] #Aqui é passado uma função read_html pois transformamos nossa tabela em uma unica variavel por isso é melhor utilizar ele do que o DataFrame normal...
#o read_html vai retornar uma lista de dataframes, por isso que sem utilizar o [0] ele vem com as chaves, pq ta acessando uma lista de dataframes, utilizando o [0] pegamos só o primeiro elemento e assim a exibição da tabela fica bonitinha
print("Histórico do Lucro Líquido\n")
print(df_tabela_liquido)
print("\n")

print("Índices de Basileia e Imobilização\n")
print(df_tabela_indice)
print("\n")
print("Lucro Líquido Trimestral\n")
print(df_tabela_trimestral)

# Display utilizado para melhor exibição da tabela, exibe de maneira mais formatada


