# from app.extensions import db
# from datetime import datetime
# from app.apps.concentracao.enums import SituacaoConcentracaoEnum

# class Concentracao(db.Model):
#     __tablename__ = 'concentracao'

#     id = db.Column(db.Integer, primary_key=True)
#     momento_checkin = db.Column(db.DateTime, nullable=False, default=datetime.now)
#     momento_checkout = db.Column(db.DateTime, nullable=True)
#     situacao = db.Column(db.Enum(SituacaoConcentracaoEnum), nullable=False, default=SituacaoConcentracaoEnum.DISPONIVEL.name)
    
#     evento_id = db.Column(db.Integer, db.ForeignKey('evento.id', ondelete="CASCADE"), nullable=False)
#     jogador_id = db.Column(db.Integer, db.ForeignKey('jogador.id', ondelete="CASCADE"), nullable=False)

#     # Relacionamentos
#     jogador = db.relationship('Jogador', back_populates='concentracoes')
#     evento = db.relationship('Evento', back_populates='concentracoes')

#     escalacoes = db.relationship('Escalacao', back_populates='concentracao', cascade="all, delete-orphan")

#     # Índice único para evitar duplicidade de jogador em um evento
#     __table_args__ = (
#         db.Index('evento_jogador_index', 'evento_id', 'jogador_id', unique=True),
#     )

#     def __repr__(self):
#         return f"{self.momento_checkin.strftime('%H:%M:%S')} - {self.jogador.nome_camisa.upper()}"
