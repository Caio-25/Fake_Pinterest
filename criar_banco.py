import pymysql

from fakepinterest import app, database
from fakepinterest.models import Usuario, Foto


# Cria o banco de dados MySQL caso ele ainda não exista.
conexao = pymysql.connect(
    host="MYSQL_HOST",
    user="MYSQL_USUARIO",
    password="MYSQL_SENHA",
    autocommit=True
)

try:
    with conexao.cursor() as cursor:
        cursor.execute(
            "CREATE DATABASE IF NOT EXISTS fakepinterest"
        )

    print("Banco de dados fakepinterest criado com sucesso!")

finally:
    conexao.close()


# Cria as tabelas utilizando os modelos do Flask-SQLAlchemy.
with app.app_context():

    # Cria as tabelas definidas no models.py.
    database.create_all()

    print("Tabelas criadas com sucesso!")
