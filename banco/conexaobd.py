import mysql.connector
import sys
sys.path.append('../projetos_navarro')
import scrapy_lucros


#Estabelecendo a conexão com o banco de dados
conexao = mysql.connector.connect(
    host="localhost",  # Endereço do servidor de banco de dados
    user="root",  # Nome de usuário do banco de dados
    password="",  # Senha do banco de dados
    database="bd_navarro" , # Nome do banco de dados
    charset='utf8'
)

#Caso a conexão tenha sido estabelecida vai aparecer a mensagem abaixo
print("Conexão com o banco de dados estabelecida com sucesso.")

#Criando um objeto de cursor para executar nossas consultas SQL
cursor = conexao.cursor()

#Importando as funções de extração de html do nosso outro arquivo
from scrapy_lucros import extrair_infos_ul, sopa_bonita, extrair_infos_banco, extrair_tabela_liquido, extrair_tabela_trimestral
from scrapy_lucros import banco

#Pegando os dados
dados = extrair_infos_ul(sopa_bonita)
nome_banco = banco

#Verificação para ver se o banco já existe em nosso banco de dados, como todas as tabelas são relacionadas por um banco logo se em uma tabela existir
#uma informação sobre aquele banco nas outras também vão existir
cursor.execute("SELECT nome FROM bancos_consultas WHERE nome = %s", (nome_banco,))
verificacao_banco = cursor.fetchone()

if verificacao_banco:
    print(f"As informações do banco {nome_banco} já foram cadastradas.\n")
        
    cursor.execute("SELECT * FROM info_bancos WHERE nome_banco = %s", (nome_banco,))
    exibir_tabela_info = cursor.fetchall()
    print("\nInformações do banco:")
    for exibir_info in exibir_tabela_info:
        print(exibir_info)
        
    cursor.execute("SELECT * FROM bancos_consultas WHERE nome = %s", (nome_banco,))
    exibir_tabela_banco = cursor.fetchall()
    print("\nResumo do último balanço")
    for exibir_banco in exibir_tabela_banco:
        print(exibir_banco)

    cursor.execute("SELECT * FROM lucro_liquido_bancos WHERE nome_banco = %s", (nome_banco,))
    exibir_tabela_lucrolqd = cursor.fetchall()
    print("\nHistórico do Lucro Líquido:")
    for exibir_lucrolqd in exibir_tabela_lucrolqd:
        print(exibir_lucrolqd)

    cursor.execute("SELECT * FROM lucro_liquido_trimestral_bancos WHERE nome_banco = %s", (nome_banco,))
    exibir_tabela_trimestral = cursor.fetchall()
    print("\nLucro Líquido Trimestral:")
    for exibir_trimestral in exibir_tabela_trimestral:
        print(exibir_trimestral)

else:
    print(f"As informações do banco {nome_banco} não estão em nosso banco de dados, portanto puxaremos essa informação do site banco data e armazenaremos em nosso banco de dados!")
    infos_banco = extrair_infos_banco(sopa_bonita)
    infos_ul = extrair_infos_ul(sopa_bonita)
    tabela_liquido = extrair_tabela_liquido(sopa_bonita)
    tabela_trimestral = extrair_tabela_trimestral(sopa_bonita)

    # Imprimindo na ordem desejada
    print("Informações do Banco:")
    print(infos_banco)
    print("\n")

    print("Resumo do Último Balanço:")
    print(infos_ul)
    print("\n")

    print("Tabela de Lucro Líquido:")
    print(tabela_liquido)
    print("\n")

    print("Tabela Trimestral:")
    print(tabela_trimestral)
    print("\n")

    #TABELA ULTIMO BALANÇO
    # # executa uma consulta SQL de inserção - aqui para a parte do ultimo balanço
    cursor.execute("INSERT INTO bancos_consultas (nome, data_publicacao, lucro_liquido, patrimonio_liquido, ativo_total, captacoes, carteira_credito_classificada, patrimonio_referencia_rwa, numero_agencias, numero_pontos_atendimento) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
               (nome_banco, dados["Publicação"], dados["Lucro Líquido (R$)"], dados["Patrimônio Líquido (R$)"], dados["Ativo Total (R$)"], dados["Captações (R$)"], dados["Carteira de Crédito Classificada (R$)"], dados["Patrimônio de Referência RWA (R$)"], dados["Número de Agências"], dados["Número de Pontos de Atendimento"]))
    
    #TABELA INFORMAÇÕES DO BANCO
    dados = extrair_infos_banco(sopa_bonita)
    #Aqui estamos pegando só a segunda coluna da nossa tabela
    valores_a_inserir = dados.iloc[:, 1].tolist()
    valores_a_inserir.insert(0, nome_banco)
    cursor.execute("INSERT INTO info_bancos (nome_banco, matriz, site_oficial, consolidacao, nome_fantasia, razao_social, cnpj, data_de_abertura, controle_acionario, tipo_da_instituicao) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", valores_a_inserir)

    #TABELA DE LUCROS LIQUIDOS
    dados = extrair_tabela_liquido(sopa_bonita)

    ano = dados['Ano'].tolist()
    resultado = dados['Resultado'].tolist()
    valor = dados['Valor (R$)'].tolist()

    # Itera sobre cada linha da tabela e insere os dados no banco
    for i in range(len(ano)):
        cursor.execute("INSERT INTO lucro_liquido_bancos (nome_banco, ano, resultado, valor_rs) VALUES (%s, %s, %s, %s)", (nome_banco, ano[i], resultado[i], valor[i]))

    #TABELA DE LUCROS LIQUIDOS TRIMESTRAIS
    dados = extrair_tabela_trimestral(sopa_bonita)
    trimestre = dados['Trimestre'].tolist()
    tri1 = dados['2T2023'].tolist()
    tri2 = dados['1T2023'].tolist()
    tri3 = dados['4T2022'].tolist()
    tri4 = dados['3T2022'].tolist()
    tri5 = dados['2T2022'].tolist()
    tri6 = dados['1T2022'].tolist()
    tri7 = dados['4T2021'].tolist()
    tri8 = dados['3T2021'].tolist()
    tri9 = dados['2T2021'].tolist()

    for i in range(len(trimestre)):
        cursor.execute("INSERT INTO lucro_liquido_trimestral_bancos (nome_banco, trimestre, 2T2023, 1T2023, 4T2022, 3T2022, 2T2022, 1T2022, 4T2021, 3T2021, 2T2021) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                    (nome_banco, trimestre[i], tri1[i], tri2[i], tri3[i], tri4[i], tri5[i], tri6[i], tri7[i], tri8[i], tri9[i]))


    # Confirmar a inserção dos dados
    conexao.commit()

    # Feche o cursor e a conexão
    conexao.close()
