from app.extensions import db
from datetime import datetime

class Gol(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jogador_id = db.Column(db.Integer, db.ForeignKey('jogador.id'), nullable=False)
    partida_id = db.Column(db.Integer, db.ForeignKey('partida.id'), nullable=False)
    momento_gol = db.Column(db.DateTime, nullable=False, default=datetime.now)

    jogador = db.relationship('Jogador')
