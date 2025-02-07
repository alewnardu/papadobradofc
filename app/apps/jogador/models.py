from app.extensions import db

class Jogador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_completo = db.Column(db.String(120), nullable=False)
    nome_camisa = db.Column(db.String(25), nullable=False)
    numero_camisa = db.Column(db.SmallInteger, nullable=False)
    is_policial_penal = db.Column(db.Boolean, nullable=False, default=False)
    is_associado = db.Column(db.Boolean, nullable=False, default=False)
    is_mensalista = db.Column(db.Boolean, nullable=False, default=False)
