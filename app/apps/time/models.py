# from app.extensions import db

# class Time(db.Model):
#     __tablename__ = 'time'

#     id = db.Column(db.Integer, primary_key=True)
#     nome = db.Column(db.String(100), unique=True, nullable=False)
#     is_active = db.Column(db.Boolean, nullable=False, default=True)

#     # Relacionamento com Escalacoes
#     escalacoes = db.relationship('Escalacao', back_populates='time', cascade="all, delete-orphan")

#     # Relacionamento com Time_Partida (Histórico de partidas do time)
#     partidas = db.relationship('Time_Partida', back_populates='time', cascade="all, delete-orphan")

#     def __repr__(self):
#         return f"{self.nome.upper()}"
