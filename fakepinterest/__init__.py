import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

# Carrega as variáveis do arquivo .env.
load_dotenv()

# Cria a aplicação Flask.
app = Flask(__name__)

# Obtém os dados de conexão das variáveis de ambiente.
usuario = os.getenv("MYSQL_USER")
senha = os.getenv("MYSQL_PASSWORD")
host = os.getenv("MYSQL_HOST")
banco = os.getenv("MYSQL_DATABASE")

# Configura a conexão com o MySQL.
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"mysql+pymysql://{usuario}:{senha}@{host}/{banco}")
app.config["SECRET_KEY"] ="b6jGTAQPNaWg_KaVD9vL9Q"


# Inicializa o SQLAlchemy na aplicação.
database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "homepage"

# Importa as rotas do projeto.
from fakepinterest import routes