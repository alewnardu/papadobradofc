from app.extensions import db

class Escalacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time_id = db.Column(db.Integer, db.ForeignKey('time.id'), nullable=False)
    concentracao_id = db.Column(db.Integer, db.ForeignKey('concentracao.id'), nullable=False)

    time = db.relationship('Time', back_populates='escalacoes')
    concentracao = db.relationship('Concentracao', back_populates='escalacoes')

    def __repr__(self):
        return f"{self.time.nome} - {self.concentracao.jogador.nome_camisa}"
