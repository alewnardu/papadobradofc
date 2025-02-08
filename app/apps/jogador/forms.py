from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Optional

class JogadorForm(FlaskForm):
    nome_camisa = StringField('Nome na Camisa', validators=[DataRequired(), Length(min=3, max=25)])
    numero_camisa = IntegerField('Número na Camisa', validators=[DataRequired()])
    nome_completo = StringField('Nome Completo', validators=[DataRequired(), Length(min=3, max=120)])
    is_policial_penal = BooleanField('Policial Penal?', validators=[Optional()])
    is_associado = BooleanField('Associado SINDPPEN?', validators=[Optional()])
    is_mensalista = BooleanField('Mensalista na Pelada?', validators=[Optional()])
    situacao = SelectField('Situação do Jogador', choices=[
        ('APTO', 'Apto para Jogar'),
        ('DEPARTAMENTO_MEDICO', 'Departamento Médico'),
        ('SUSPENSO', 'Suspenso da Pelada'),
        ('INDISPONIVEL', 'Indisponível'),
        ('NAO_ESCALADO', 'Não Escalado'),
    ], validators=[DataRequired()])