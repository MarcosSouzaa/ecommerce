from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello, World</h1>'

@app.route('/sobre/<usuario>')
def sobre(usuario):
    return f'<h3>Sobre mim: {usuario}</h3>'


 