from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mercado.db"
db.init_app(app)

# no nosso mercado temos vários ítens ou produtos
# esse é o nosso model que vai gerar uma tabela no banco de dados
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(length=30), nullable=False, unique=True)
    preco = db.Column(db.Integer, nullable=False)
    cod_barra = db.Column(db.String(length=12), nullable=False, unique=True)
    descricao = db.Column(db.String(length=1024), nullable=False, unique=True)

@app.route('/')
def page_home():
    return render_template('home.html')

@app.route('/produtos')
def page_produto():
    itens = [
       {'id': 1, 'nome':'Celular', 'cod_barra':'234568789654','preco': 1200},
       {'id': 2, 'nome':'Notebook', 'cod_barra':'121245445454','preco': 3500},
       {'id': 3, 'nome':'Teclado', 'cod_barra':'325645678965','preco': 120},
       {'id': 4, 'nome': 'Monitor', 'cod_barra':'565654879991','preco':800}
    ]     
    return render_template('produtos.html', itens = itens)
