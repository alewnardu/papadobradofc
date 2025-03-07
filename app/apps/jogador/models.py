from app.extensions import db
from app.apps.jogador.enums import SituacaoJogadorEnum
class Jogador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_camisa = db.Column(db.String(25), nullable=False)
    numero_camisa = db.Column(db.SmallInteger, nullable=False)
    nome_completo = db.Column(db.String(120), nullable=False)
    is_policial_penal = db.Column(db.Boolean, nullable=False, default=False)
    is_associado = db.Column(db.Boolean, nullable=False, default=False)
    is_mensalista = db.Column(db.Boolean, nullable=False, default=False)
    situacao = db.Column(db.Enum(SituacaoJogadorEnum), nullable=False, default=SituacaoJogadorEnum.ATIVO.name)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)  # Permite null, não é obrigatório ter usuário

    # Relacionamento de volta com o usuário (pode ser None se não houver usuário)
    user = db.relationship('User', back_populates='jogador', uselist=False)
    
    # Relacionamento com as concentrações do jogador em cada evento (Suas presenças nas listas de chegada)
    concentracoes = db.relationship('Concentracao', back_populates='jogador')


    def __repr__(self):
        return f"{self.nome_completo.upper()}"

