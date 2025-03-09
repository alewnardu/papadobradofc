# from flask_wtf import FlaskForm
# from wtforms import StringField, IntegerField, BooleanField, SelectField, DateTimeField
# from wtforms.validators import DataRequired, Length, NumberRange
# from app.apps.evento.enums import SituacaoEventoEnum

# class EventoForm(FlaskForm):  
#     nome = StringField('Nome', default="Futebol da Polícia Penal", validators=[DataRequired(), Length(min=3, max=120)])
#     local = StringField('Local', default="Atenas Futebol Clube, QD 1002 Sul, Palmas - TO", validators=[DataRequired(), Length(min=3, max=120)])
#     inicio = DateTimeField(
#         'Início do Evento',
#         format="%Y-%m-%dT%H:%M",  # Ajustado para corresponder ao input HTML
#         validators=[DataRequired()]
#     )
#     termino = DateTimeField(
#         'Término do Evento',
#         format="%Y-%m-%dT%H:%M",  # Ajustado para corresponder ao input HTML
#         validators=[DataRequired()]
#     )
#     duracao = IntegerField('Duração (minutos)', default=90, validators=[
#         DataRequired(),
#         NumberRange(min=60, message="A duração deve ser no mínimo 60 minutos.")
#     ])
#     situacao = SelectField('Situação do Evento', choices=[
#         (status.name, status.value) for status in SituacaoEventoEnum
#     ], validators=[DataRequired()])