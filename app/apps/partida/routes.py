# from flask import Blueprint, render_template, redirect, url_for, flash, request
# from flask_login import login_required
# from app.extensions import db, bcrypt
# from app.apps.auth.models import User
# from app.apps.jogador.models import Jogador
# from app.apps.jogador.forms import JogadorForm
# from sqlalchemy.exc import SQLAlchemyError
# from app.apps.jogador.enums import SituacaoJogadorEnum

# jogador_bp = Blueprint('jogador', __name__, url_prefix='/jogador',template_folder="../../templates/")

# @jogador_bp.route('/cadastrar', methods=['GET', 'POST'])
# @login_required
# def cadastrar_jogador():
#     form = JogadorForm()
#     if form.validate_on_submit():
#         try:
#             with db.session.begin():
#                 new_jogador = Jogador(
#                     nome_camisa=form.nome_camisa.data,
#                     numero_camisa=form.numero_camisa.data,
#                     nome_completo=form.nome_completo.data,            
#                     is_policial_penal=form.is_policial_penal.data,
#                     is_associado=form.is_associado.data,
#                     is_mensalista=form.is_mensalista.data,
#                 )
#                 db.session.add(new_jogador)
#                 db.session.flush()
                
#                 hashed_password = bcrypt.generate_password_hash(new_jogador.nome_camisa).decode("utf-8")
#                 perfil_usuario = User(username=new_jogador.nome_camisa, password=hashed_password, is_active=True)
#                 db.session.add(perfil_usuario)
#             flash("Jogador cadastrado com sucesso!.", "success")
#             return redirect(url_for("jogador.listagem"))
#         except SQLAlchemyError as e:
#             db.session.rollback()
#             print(f"Erro ao cadastrar jogador: {str(e)}")
#             flash("Cadastro indisponível! Tente novamente mais tarde.", "warning")
#     return render_template('jogador/form.html', form=form)

# @jogador_bp.route("/listar-jogadores")
# @login_required
# def listagem():
#     page = request.args.get("page", 1, type=int)
#     per_page = 10

#     jogadores_pagination = Jogador.query.order_by(Jogador.nome_completo).paginate(page=page, per_page=per_page, error_out=False)
    
#     return render_template(
#         "jogador/list.html", 
#         jogadores=jogadores_pagination.items,  # Jogadores da página atual
#         pagination=jogadores_pagination  # Objeto de paginação para os links
#     )

# @jogador_bp.route("/alterar-situacao/<int:jogador_id>", methods=['GET', 'POST'])
# @login_required
# def alterar_situacao(jogador_id):
#     try:
#         jogador = Jogador.query.get_or_404(jogador_id)
#         jogador.situacao = (
#             SituacaoJogadorEnum.INATIVO.name if jogador.situacao.value == SituacaoJogadorEnum.ATIVO.name  
#             else SituacaoJogadorEnum.ATIVO.name 
#         )
#         db.session.commit()
#         flash(f"A situação do jogador {jogador.nome_camisa} foi alterada para {jogador.situacao.value}.", "success")
#         return redirect(url_for("jogador.listagem"))
#     except SQLAlchemyError as e:
#         db.session.rollback()
#         print(f"Erro ao alterar situação do jogador {jogador_id}: {str(e)}")
#         flash(f"Erro ao salvar alteração. Tente novamente mais tarde.", "warning")
#     except Exception as e:
#         db.session.rollback()
#         print(f"Erro inesperado ao alterar situação do jogador {jogador_id}: {str(e)}")
#         flash(f"Erro inesperado! Tente novamente mais tarde.", "warning")

#     return redirect(url_for("jogador.listagem"))