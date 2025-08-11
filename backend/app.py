# backend/app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token, jwt_required, JWTManager, get_jwt_identity

# --- CONFIGURAÇÃO DAS APLICAÇÕES E EXTENSÕES ---
app = Flask(__name__)
CORS(app)

# Configuração do Banco de Dados (usando o nome do serviço 'db' do Docker)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:admin@db:5432/db_cursos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuração do JWT (JSON Web Tokens)
# Esta chave secreta é usada para assinar os tokens. Mude para algo seguro!
app.config['JWT_SECRET_KEY'] = 'uma-chave-secreta-super-segura-mude-depois'

# Inicializa as extensões
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)


# --- MODELOS DO BANCO DE DADOS ---
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha_hash = db.Column(db.String(128), nullable=False)

class Curso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_curso = db.Column(db.String(150), nullable=False)
    descricao = db.Column(db.Text, nullable=True)

class Matricula(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    curso_id = db.Column(db.Integer, db.ForeignKey('curso.id'), nullable=False)


# --- ROTAS DA API ---

# Rota de teste principal
@app.route("/")
def hello_world():
    return "API com Flask da Plataforma DB Cursos no ar!"

# ROTA DE CADASTRO DE USUÁRIO
@app.route("/register", methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    
    # Verifica se o usuário já existe
    if Usuario.query.filter_by(email=email).first():
        return jsonify({"msg": "Este email já está em uso"}), 409

    # Gera o hash da senha
    hashed_password = bcrypt.generate_password_hash(data['senha']).decode('utf-8')
    
    # Cria o novo usuário
    novo_usuario = Usuario(
        nome=data['nome'],
        email=email,
        senha_hash=hashed_password
    )
    
    db.session.add(novo_usuario)
    db.session.commit()
    
    return jsonify({"msg": "Usuário criado com sucesso!"}), 201

# ROTA DE LOGIN
@app.route("/login", methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    senha = data.get('senha')
    
    usuario = Usuario.query.filter_by(email=email).first()
    
    # Verifica se o usuário existe e se a senha está correta
    if usuario and bcrypt.check_password_hash(usuario.senha_hash, senha):
        # Cria o token de acesso
        access_token = create_access_token(identity=usuario.id)
        return jsonify(access_token=access_token)
        
    return jsonify({"msg": "Email ou senha inválidos"}), 401


# ROTA PROTEGIDA DE EXEMPLO
@app.route("/portal", methods=['GET'])
@jwt_required() # Esta linha protege a rota
def portal():
    # Pega o ID do usuário a partir do token
    current_user_id = get_jwt_identity()
    usuario = Usuario.query.get(current_user_id)
    
    return jsonify({
        "msg": f"Bem-vindo ao portal, {usuario.nome}!",
        "seu_id": usuario.id
    }), 200


# Bloco para rodar a aplicação
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)