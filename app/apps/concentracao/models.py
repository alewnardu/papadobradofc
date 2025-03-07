from app.extensions import db
from datetime import datetime
from app.apps.concentracao.enums import SituacaoConcentracaoEnum

class Concentracao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    momento_checkin = db.Column(db.DateTime, nullable=False, default=datetime.now)
    momento_checkout = db.Column(db.DateTime, nullable=True)
    situacao = db.Column(db.Enum(SituacaoConcentracaoEnum), nullable=False, default=SituacaoConcentracaoEnum.DISPONIVEL.name)
    evento_id = db.Column(db.Integer, db.ForeignKey('evento.id'), nullable=False)
    jogador_id = db.Column(db.Integer, db.ForeignKey('jogador.id'), nullable=False)

    # Definição do relacionamento para acessar os dados do jogador
    jogador = db.relationship('Jogador', back_populates='concentracoes')
    
    # Definição do relacionamento para acessar os dados do evento
    evento = db.relationship('Evento', back_populates='concentracoes')

    # Relacionamento com as escalações do jogador em cada evento (Dá acesso aos times em que eles foram escalados)
    escalacoes = db.relationship('Escalacao', back_populates='concentracao')

    # Definir índice único entre evento_id e jogador_id
    __table_args__ = (
        db.Index('evento_jogador_index', 'evento_id', 'jogador_id', unique=True),
    )

    def __repr__(self):
        return f"{self.momento_checkin.strftime('%H:%M:%S')} - {self.jogador.nome_camisa.upper()}"
