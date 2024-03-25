# Importa a classe Flask e a função render_template do módulo flask
from flask import Flask, render_template

# Cria uma instância da classe Flask com o nome do módulo atual (__name__) e define o diretório estático como 'static'
app = Flask(__name__, static_folder='static')

# Define uma rota para a URL raiz ('/') e associa a função homepage a essa rota
@app.route("/")
def homepage():
    # Retorna o resultado da função render_template, que renderiza o template "index.html"
    return render_template("index.html")

# Define uma rota para a URL '/lucros' e associa a função lucros a essa rota
@app.route("/lucros")
def lucros():
    # Retorna o resultado da função render_template, que renderiza o template "lucros.html"
    return render_template("lucros.html")

# Verifica se o script está sendo executado diretamente (não importado como um módulo)
if __name__ =="__main__":
    # Inicia o servidor Flask na porta padrão (5000) em modo de depuração (debug=True)
    app.run(debug=True)
