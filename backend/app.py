# backend/app.py

from flask import Flask
from flask_cors import CORS

# Configuração da aplicação
app = Flask(__name__)
CORS(app) # Habilita o CORS para permitir requisições do frontend

# Rota de teste principal
@app.route("/")
def hello_world():
    return "API com Flask da Plataforma DB Cursos no ar!"

# Bloco para rodar a aplicação
if __name__ == "__main__":
    # O debug=True faz o servidor reiniciar automaticamente quando você altera o código
    app.run(debug=True, port=5000)