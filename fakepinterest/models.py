# Importa o objeto database criado na aplicação Flask.
# Ele permite definir os modelos e as tabelas do banco de dados.
from fakepinterest import database
# Importa datetime para trabalhar com datas e horários.
from datetime import datetime, timezone

# Cria o modelo Usuario, que representa a tabela de usuários no
class Usuario(database.Model):
    # Cria a coluna id, que identifica cada usuário de forma única.
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.Integer, primary_key=True)
    email = database.Column(database.String(150), nullable=False)
    senha = database.Column (database.String(255), nullable=False)
    fotos = database.relationship("Foto",backref="Usuario", lazy=True)

# Cria o modelo Foto, que representa a tabela de fotos no banco de dados.
class Foto(database.Model):

    id = database.Column(database.Integer,primary_key=True)
    imagem = database.Column(database.String(255), default="default.png")
    data_criacao = database.Column(database.DateTime(timezone=True),nullable=False,default=lambda: datetime.now(timezone.utc))
    id_usuario = database.Column(database.Integer,database.ForeignKey('usuario.id'), nullable=False)
