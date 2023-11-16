from mercado import db
# no nosso mercado temos vários ítens ou produtos
# esse é o nosso model que vai gerar uma tabela no banco de dados
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(length=30), nullable=False, unique=True)
    preco = db.Column(db.Integer, nullable=False)
    cod_barra = db.Column(db.String(length=12), nullable=False, unique=True)
    descricao = db.Column(db.String(length=1024), nullable=False, unique=True)
    
    # Para melhorar a visualização no retorno dos dados
    # o self são as informações das colunas
    def __repr__(self):
        return f"Item {self.nome}"
