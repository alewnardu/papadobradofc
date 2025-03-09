
    escalacao_id = db.Column(db.Integer, db.ForeignKey('escalacao.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)


from app.extensions import db
from datetime import datetime

class Gol(db.Model):
    __tablename__ = 'gol'

    id = db.Column(db.Integer, primary_key=True)
    escalacao_id = db.Column(db.Integer, db.ForeignKey('escalacao.id', ondelete="CASCADE"), nullable=False)
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.now())

    # Relacionamentos bidirecionais
    escalacao = db.relationship('Escalacao', back_populates='gols')

    def __repr__(self):
        return f"Gol de {self.escalacao.concentracao.jogador.nome_camisa} na Partida {self.partida.id}"
