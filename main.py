from flask import Flask, render_template, url_for

# Inicializa a aplicação Flask.
app = Flask(__name__)

# Define a rota da página inicial.
@app.route("/")
def homepage():
    # Renderiza o HTML da página inicial
    return render_template("homepage.html")

# Define a rota da página de perfil.
@app.route("/perfil/<usuario>")
def perfil(usuario):
    # Renderiza o HTML da página de perfil
    return render_template("Perfil.html", usuario=usuario)


if __name__ == "__main__":
    # Inicia o servidor de desenvolvimento.
    app.run(debug=True)