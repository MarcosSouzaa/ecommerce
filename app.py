from flask import Flask, render_template

app = Flask(__name__)

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
