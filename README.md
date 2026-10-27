# 📌 FakePinterest

Aplicação web inspirada no Pinterest, desenvolvida com Python e Flask como projeto de aprendizado em desenvolvimento Backend.

O objetivo deste projeto é praticar o desenvolvimento de aplicações web, a integração com bancos de dados relacionais e a organização de código utilizando ferramentas comuns no ecossistema Python.

## 🚀 Tecnologias utilizadas

* **Python** — linguagem de programação.
* **Flask** — framework para desenvolvimento web.
* **Flask-SQLAlchemy** — integração entre a aplicação e o banco de dados.
* **MySQL** — sistema de gerenciamento de banco de dados relacional.
* **PyMySQL** — driver de conexão entre Python e MySQL.
* **Flask-Login** — gerenciamento de autenticação e sessões de usuários.
* **Flask-Bcrypt** — geração e verificação de hashes de senhas.
* **HTML5** — estrutura das páginas web.
* **Git e GitHub** — versionamento e hospedagem do código.

## 📂 Estrutura do projeto

```text
ProjetoFakePinterest/
│
├── fakepinterest/
│   ├── __init__.py
│   ├── routes.py
│   ├── forms.py
│   ├── models.py
│   │
│   └── templates/
│       ├── base.html
│       ├── homepage.html
│       └── perfil.html
│
├── criar_banco.py
├── main.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

*Observação: a estrutura acima representa a organização prevista para o projeto. Os arquivos devem corresponder à estrutura existente no repositório.*

## 🗄️ Banco de dados

O projeto utiliza o MySQL para armazenar os dados da aplicação.

A integração com o banco é realizada utilizando Flask-SQLAlchemy, que permite definir modelos Python para representar as tabelas.

### Tabela `usuario`

Responsável por armazenar os dados dos usuários.

| Campo      | Descrição                                          |
| ---------- | -------------------------------------------------- |
| `id`       | Identificador único do usuário.                    |
| `username` | Nome de usuário.                                   |
| `email`    | Endereço de e-mail.                                |
| `senha`    | Campo destinado ao armazenamento do hash da senha. |

### Tabela `foto`

Responsável por armazenar informações sobre as imagens publicadas.

| Campo          | Descrição                                          |
| -------------- | -------------------------------------------------- |
| `id`           | Identificador único da foto.                       |
| `imagem`       | Nome ou caminho do arquivo da imagem.              |
| `data_criacao` | Data e hora de criação do registro.                |
| `id_usuario`   | Chave estrangeira que relaciona a foto ao usuário. |

O relacionamento entre as tabelas permite associar as fotos aos respectivos usuários.

## ⚙️ Configuração do ambiente

### 1. Pré-requisitos

Para executar o projeto, você precisará de:

* Python instalado.
* MySQL instalado e em execução.
* Git instalado.
* Um terminal ou editor de código, como o PyCharm.

### 2. Clone o repositório

```bash
git clone https://github.com/Caio-25/Fake_Pinterest.git
```

Entre na pasta do projeto:

```bash
cd Fake_Pinterest
```

### 3. Crie um ambiente virtual

```bash
python -m venv .venv
```

Ative o ambiente virtual no Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Instale as dependências

Se o arquivo `requirements.txt` estiver atualizado:

```bash
python -m pip install -r requirements.txt
```

### 5. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto e configure as variáveis necessárias:

```dotenv
MYSQL_USER=seu_usuario
MYSQL_PASSWORD=sua_senha
MYSQL_HOST=localhost
MYSQL_DATABASE=fakepinterest
SECRET_KEY=sua_chave_secreta
```

Substitua os valores de exemplo pelos valores do seu ambiente local.

**Segurança:** o arquivo `.env` contém informações privadas e não deve ser enviado ao GitHub.

### 6. Crie o banco de dados

Se o banco ainda não existir, crie-o no MySQL ou utilize o script `criar_banco.py`, caso ele esteja configurado para essa finalidade.

As tabelas devem corresponder aos modelos definidos em `models.py`.

### 7. Execute a aplicação

Com o ambiente configurado e o banco de dados disponível, execute:

```bash
python main.py
```

Se a aplicação iniciar corretamente, acesse no navegador o endereço local informado pelo Flask, normalmente:

```text
http://127.0.0.1:5000
```

## 🔐 Segurança

O projeto utiliza variáveis de ambiente para separar as configurações sensíveis do código-fonte.

A implementação da autenticação utiliza Flask-Login para gerenciar sessões de usuários e Flask-Bcrypt para trabalhar com hashes de senhas.

As senhas não devem ser armazenadas em texto puro.

## 🎯 Objetivos de aprendizado

Este projeto faz parte dos meus estudos em Engenharia de Software e desenvolvimento Backend com Python.

Por meio dele, busco desenvolver conhecimentos em:

* Desenvolvimento de aplicações web com Flask.
* Organização de projetos Python.
* Modelagem de dados relacionais.
* Integração entre Python e MySQL.
* Utilização do ORM SQLAlchemy.
* Autenticação e gerenciamento de sessões.
* Proteção de senhas com hashes.
* Versionamento de código com Git e GitHub.
* Documentação técnica de projetos.

## 🛠️ Próximas melhorias

* Concluir e testar o cadastro de usuários.
* Implementar e testar o login e o logout.
* Finalizar o gerenciamento de sessões.
* Desenvolver a publicação e a exibição de imagens.
* Melhorar a validação dos formulários.
* Aprimorar a interface e a experiência do usuário.
* Expandir a documentação e os testes.

## 👨‍💻 Autor

**Caio Sena**

Estudante de Engenharia de Software, com foco em desenvolvimento Backend utilizando Python e bancos de dados relacionais.

* GitHub: [Caio-25](https://github.com/Caio-25)
* Projeto: [FakePinterest](https://github.com/Caio-25/Fake_Pinterest)
