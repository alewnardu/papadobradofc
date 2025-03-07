from flask_login import UserMixin
from app.extensions import db, bcrypt

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=False)

    jogador = db.relationship('Jogador', back_populates='user', uselist=False)

    def set_password(self, password):
        """Armazena a senha de forma segura"""
        self.password = bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password):
        """Verifica se a senha está correta"""
        return bcrypt.check_password_hash(self.password, password)
    
    def __repr__(self):
        return f'<User {self.username}>'