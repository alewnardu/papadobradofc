from app.extensions import db

class TimePartida(db.Model):
    __tablename__ = 'time_partida'

    time_id = db.Column(db.Integer, db.ForeignKey('time.id', ondelete="CASCADE"), primary_key=True)
    partida_id = db.Column(db.Integer, db.ForeignKey('partida.id', ondelete="CASCADE"), primary_key=True)

    # Relacionamentos bidirecionais
    time = db.relationship('Time', back_populates='partidas')
    partida = db.relationship('Partida', back_populates='times_partida')

    def __repr__(self):
        return f"Time {self.time} na Partida {self.partida.id}"
