from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/perfil")
def perfil():
    return render_template("Perfil.html")


if __name__ == "__main__":
    app.run(debug=True)