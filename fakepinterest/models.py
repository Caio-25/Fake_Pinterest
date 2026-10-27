from fakepinterest import database, login_manager

from datetime import datetime, timezone

from flask_login import UserMixin


# Carrega um usuário a partir do seu ID durante a autenticação.
@login_manager.user_loader
def load_usuario(id_usuario):
    return database.session.get(Usuario, int(id_usuario))


# Representa a tabela de usuários no banco de dados.
class Usuario(database.Model, UserMixin):

    # Identificador único de cada usuário.
    id = database.Column(database.Integer, primary_key=True)

    # Nome de usuário armazenado como texto e sem duplicações.
    username = database.Column(
        database.String(100),
        nullable=False,
        unique=True
    )

    # E-mail obrigatório.
    email = database.Column(database.String(150), nullable=False)

    # Campo para armazenar o hash da senha.
    senha = database.Column(database.String(255), nullable=False)

    # Relacionamento entre usuários e suas fotos.
    fotos = database.relationship("Foto", backref="usuario", lazy=True)


# Representa a tabela de fotos no banco de dados.
class Foto(database.Model):

    # Identificador único da foto.
    id = database.Column(database.Integer, primary_key=True)

    # Nome ou caminho do arquivo da imagem.
    imagem = database.Column(
        database.String(255),
        default="default.png"
    )

    # Data e hora de criação da foto.
    data_criacao = database.Column(
        database.DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc)
    )

    # Identifica o usuário proprietário da foto.
    id_usuario = database.Column(
        database.Integer,
        database.ForeignKey("usuario.id"),
        nullable=False
    )