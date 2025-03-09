# from flask_wtf import FlaskForm
# from wtforms_sqlalchemy.fields import QuerySelectField
# from wtforms.validators import DataRequired
# from app.apps.jogador.models import Jogador
# from app.apps.jogador.enums import SituacaoJogadorEnum

# def jogador_query():
#     return Jogador.query.filter(
#         Jogador.situacao.in_([
#             SituacaoJogadorEnum.ATIVO.name,
#             SituacaoJogadorEnum.DEPARTAMENTO_MEDICO.name
#         ])
#     )

# class ConcentracaoForm(FlaskForm):
#     jogador = QuerySelectField(
#         label="Jogador",
#         query_factory=jogador_query,
#         get_label=lambda jogador: f"{jogador.nome_camisa.upper()} ({'🟢' if jogador.situacao.name == 'ATIVO' else '🔴' if jogador.situacao.name == 'INATIVO' else '🔵' if jogador.situacao.name == 'DEPARTAMENTO_MEDICO' else '🟡'} {jogador.situacao.value})",
#         allow_blank=True,
#         blank_text="Selecione um jogador...",
#         validators=[DataRequired()],
#         description="Escolha um jogador disponível para compor a escalação.",
#         render_kw={
#             "class": "form-select",
#             "aria-describedby": "jogadorHelp"
#         }
#     )
