from .import db  

from flask_login import UserMixin

from sqlalchemy.sql import func

    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150))
    nome_empresa = db.Column(db.String(150))
    password = db.Column(db.String(150))
    password = db.Column(db.String(150))
    data = db.Column(db.String(10000))
    estabelecimento = db.relationship('Estabelecimentos')
    comercios_item = db.relationship('Comercios_items')
    servicos = db.relationship('Servicos')
    date = db.Column(db.DateTime(timezone=True), default=func.now())

class Estabelecimentos(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150))
    segmento_fk = db.Column(db.Integer, db.ForeignKey('segmentos.id')) 
    endereco = db.Column(db.String(150))
    telefone = db.Column(db.String)
    descricao = db.Column(db.Text)
    foto = db.Column(db.Text)
    user_fk = db.Column(db.Integer, db.ForeignKey("user.id"))

   # items = db.relationship('Items')





class Comercios_items(db.Model, UserMixin):
    item_id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(150))
    nome = db.Column(db.String(150))
    marca = db.Column(db.String(150))
    volume = db.Column(db.String(150))
    peso = db.Column(db.String(150))
    valor = db.Column(db.String(10))
    fim_promo = db.Column(db.String(150))
    foto = db.Column(db.Text, nullable =False)
    user_fk = db.Column(db.Integer, db.ForeignKey("user.id"))
    


class Servicos(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String)
    descricao = db.Column(db.String(150))
    valor = db.Column(db.String(150))
    horario_func = db.Column(db.String(150))
    foto = db.Column(db.Text)
    user_fk = db.Column(db.Integer, db.ForeignKey('user.id'))

class Segmentos(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(10))
    Estabelecimentos = db.relationship('Estabelecimentos')