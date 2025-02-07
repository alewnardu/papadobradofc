from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Length, Optional

class JogadorForm(FlaskForm):
    username = StringField('Nome na Pelada', validators=[DataRequired(), Length(min=3, max=25)])
    numero_camisa = IntegerField('Número da Camisa', validators=[DataRequired()])
    nome_completo = StringField('Nome Completo', validators=[DataRequired(), Length(min=3, max=120)])
    is_policial_penal = BooleanField('Policial Penal?', validators=[Optional()])
    is_associado = BooleanField('Associado SINDPPEN?', validators=[Optional()])
    is_mensalista = BooleanField('Mensalista na Pelada?', validators=[Optional()])
