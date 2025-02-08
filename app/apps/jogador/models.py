from app.extensions import db

class Jogador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_camisa = db.Column(db.String(25), nullable=False)
    numero_camisa = db.Column(db.SmallInteger, nullable=False)
    nome_completo = db.Column(db.String(120), nullable=False)
    is_policial_penal = db.Column(db.Boolean, nullable=False, default=False)
    is_associado = db.Column(db.Boolean, nullable=False, default=False)
    is_mensalista = db.Column(db.Boolean, nullable=False, default=False)
    situacao = db.Column(db.String(50), nullable=False, default='APTO')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)  # Permite null, não é obrigatório ter usuário

    # Relacionamento de volta com o usuário (pode ser None se não houver usuário)
    user = db.relationship('User', backref=db.backref('perfil_jogador', lazy=True), uselist=False)
