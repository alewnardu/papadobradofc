# from app.extensions import db

# class Escalacao(db.Model):
#     __tablename__ = 'escalacao'

#     id = db.Column(db.Integer, primary_key=True)
#     time_id = db.Column(db.Integer, db.ForeignKey('time.id'), nullable=False)
#     concentracao_id = db.Column(db.Integer, db.ForeignKey('concentracao.id'), nullable=False)
#     is_active = db.Column(db.Boolean, nullable=False, default=True)

#     # Relacionamentos
#     time = db.relationship('Time', back_populates='escalacoes')
#     concentracao = db.relationship('Concentracao', back_populates='escalacoes')

#     def __repr__(self):
#         status = "Ativo" if self.is_active else "Inativo"
#         return f"{self.time.nome} - {self.concentracao.jogador.nome_camisa} ({status})"

#     @staticmethod
#     def reescalar_jogadores(evento_id):
#         """Reescalona jogadores que perderam para um time incompleto ou cria um novo time."""
#         from app.models import Time, Jogador  # Importações necessárias para manipular os dados

#         # Buscar todos os times do evento atual
#         times_disponiveis = (
#             db.session.query(Time)
#             .join(Escalacao)
#             .join(Concentracao)
#             .filter(Concentracao.evento_id == evento_id, Escalacao.situacao == True)
#             .group_by(Time.id)
#             .having(db.func.count(Escalacao.id) < 6)  # Filtra times com menos de 6 jogadores
#             .all()
#         )

#         # Buscar jogadores que perderam
#         jogadores_perdedores = (
#             db.session.query(Escalacao)
#             .join(Concentracao)
#             .filter(Concentracao.evento_id == evento_id, Escalacao.ativo == True)
#             .all()
#         )

#         for escalacao in jogadores_perdedores:
#             escalacao.ativo = False  # Desativar a escalação antiga

#             if times_disponiveis:
#                 # Se houver time com vaga, realoca o jogador
#                 novo_time = times_disponiveis[0]
#             else:
#                 # Criar novo time se não houver espaço nos times existentes
#                 novo_time = Time(nome=f"Time {Time.query.count() + 1}")
#                 db.session.add(novo_time)
#                 db.session.commit()  # Salvar para obter um ID válido

#             # Criar nova escalação para o jogador
#             nova_escalacao = Escalacao(time_id=novo_time.id, concentracao_id=escalacao.concentracao_id, ativo=True)
#             db.session.add(nova_escalacao)

#         db.session.commit()  # Salvar todas as alterações
