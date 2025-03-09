from app.extensions import db
from datetime import datetime
from app.apps.partida.enums import SituacaoPartidaEnum

class Partida(db.Model):
    __tablename__ = 'partida'

    id = db.Column(db.Integer, primary_key=True)
    inicio = db.Column(db.DateTime, nullable=False, default=datetime.now)
    termino = db.Column(db.DateTime, nullable=True)
    duracao = db.Column(db.Integer, nullable=False, default=10)  # Padrão de 10 minutos
    situacao = db.Column(db.Enum(SituacaoPartidaEnum), nullable=False, default=SituacaoPartidaEnum.PENDENTE.name)
    
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.now())

    # Relacionamento com os times participantes da partida
    times_partida = db.relationship('TimePartida', back_populates='partida', cascade="all, delete-orphan")

    def __repr__(self):
        return f"Partida {self.id} - {self.inicio.strftime('%d/%m/%Y %H:%M')} - {self.situacao.name}"
