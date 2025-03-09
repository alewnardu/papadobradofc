# from app.extensions import db
# from app.apps.jogador.enums import SituacaoJogadorEnum, PosicaoJogadorEnum

# class Jogador(db.Model):
#     __tablename__ = 'jogador'

#     id = db.Column(db.Integer, primary_key=True)
#     nome_completo = db.Column(db.String(120), nullable=False)
#     nome_camisa = db.Column(db.String(25), unique=True, nullable=False)
#     numero_camisa = db.Column(db.SmallInteger, nullable=False)
#     posicao = db.Column(db.Enum(PosicaoJogadorEnum), nullable=False, default=PosicaoJogadorEnum.CORINGA.name)
#     is_policial_penal = db.Column(db.Boolean, nullable=False, default=False)
#     is_associado = db.Column(db.Boolean, nullable=False, default=False)
#     is_mensalista = db.Column(db.Boolean, nullable=False, default=False)
#     situacao = db.Column(db.Enum(SituacaoJogadorEnum), nullable=False, default=SituacaoJogadorEnum.ATIVO.name)
#     created_at = db.Column(db.TIMESTAMP, server_default=db.func.now())

#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True, nullable=False)

#     # Relacionamento com User (1-1)
#     user = db.relationship('User', back_populates='jogador', uselist=False)

#     # Relacionamento com Concentração (1-N, pois um jogador pode estar em vários eventos)
#     concentracoes = db.relationship('Concentracao', back_populates='jogador', cascade="all, delete-orphan")

#     def __repr__(self):
#         return f"{self.nome_completo.upper()}"


