
# Importa a função responsável por renderizar os templates HTML.
from flask import render_template

# Importa a aplicação Flask.
from fakepinterest import app


# Define a rota da página inicial.
@app.route("/")
def homepage():
    # Carrega o template da página inicial.
    return render_template("homepage.html")


# Define a rota da página de perfil.
@app.route("/perfil/<usuario>")
def perfil(usuario):
    # Carrega o template do perfil e envia o nome do usuário.
    return render_template("Perfil.html", usuario=usuario)
