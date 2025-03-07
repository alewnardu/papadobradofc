from app.extensions import db
from datetime import datetime
from app.apps.evento.enums import SituacaoEventoEnum

class Evento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    local = db.Column(db.String(255), nullable=False, default="Atenas Futebol Clube, QD 1002 Sul, Palmas - TO")
    situacao = db.Column(db.Enum(SituacaoEventoEnum), nullable=False, default=SituacaoEventoEnum.PREVISTO.name)
    inicio = db.Column(db.DateTime, nullable=False, default=datetime.now)
    termino = db.Column(db.DateTime, nullable=True)
    duracao = db.Column(db.Integer, nullable=False, default=90) 
    
    # Relacionamento com as concentrações do evento (Dá acesso às suas presenças nas listas de chegada)
    concentracoes = db.relationship('Concentracao', back_populates='evento')

    def __repr__(self):
        return f"Evento {self.id} - {self.inicio.strftime('%d/%m/%Y - %H:%M')} - {self.local}"

    