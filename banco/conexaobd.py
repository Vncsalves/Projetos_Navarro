import mysql.connector
import sys
sys.path.append('../projetos_navarro')
import scrapy

# Estabeleça a conexão com o banco de dados
conexao = mysql.connector.connect(
    host="localhost",  # Endereço do servidor de banco de dados
    user="root",  # Nome de usuário do banco de dados
    password="",  # Senha do banco de dados
    database="bd_navarro" , # Nome do banco de dados
    charset='utf8'
)

# Informar quando a conexão for estabelecida
print("Conexão com o banco de dados estabelecida com sucesso.")

# Crie um objeto de cursor para executar consultas SQL
cursor = conexao.cursor()

# Obtenha a sopa bonita de alguma forma (por exemplo, importando o arquivo onde ela está definida)

# Obtenha os dados a serem inseridos
from scrapy import extrair_infos, sopa_bonita
from scrapy import banco

# Obtenha os dados a serem inseridos
dados = extrair_infos(sopa_bonita)
nome_banco = banco

# Execute uma consulta SQL para cada linha do DataFrame
cursor.execute("INSERT INTO bancos_consultas (nome, data_publicacao, lucro_liquido, patrimonio_liquido, ativo_total, captacoes, carteira_credito_classificada, patrimonio_referencia_rwa, numero_agencias, numero_pontos_atendimento) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
               (nome_banco, dados["Publicação"], dados["Lucro Líquido (R$)"], dados["Patrimônio Líquido (R$)"], dados["Ativo Total (R$)"], dados["Captações (R$)"], dados["Carteira de Crédito Classificada (R$)"], dados["Patrimônio de Referência RWA (R$)"], dados["Número de Agências"], dados["Número de Pontos de Atendimento"]))

# Confirmar a inserção dos dados
conexao.commit()

# Feche o cursor e a conexão
cursor.close()
conexao.close()
