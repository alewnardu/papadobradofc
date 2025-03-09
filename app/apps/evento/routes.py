# from flask import Blueprint, render_template, redirect, url_for, flash, request
# from flask_login import login_required
# from sqlalchemy.exc import SQLAlchemyError, IntegrityError
# from app.extensions import db
# from app.apps.evento.forms import EventoForm
# from app.apps.evento.models import Evento
# from datetime import datetime
# from app.apps.evento.enums import SituacaoEventoEnum
# from datetime import date
# from sqlalchemy import func
# from app.apps.partida.models import Partida
# from app.apps.time.models import Time
# from app.apps.concentracao.models import Concentracao
# import locale

# locale.setlocale(locale.LC_TIME, "pt_BR.utf8")
# evento_bp = Blueprint('evento', __name__, url_prefix='/evento',template_folder="../../templates/")

# @evento_bp.route("/listagem", methods=['GET'])
# @login_required
# def listagem():
#     evento_atual = Evento.query.filter(
#         func.date(Evento.inicio) >= date.today(),
#         Evento.situacao.in_([SituacaoEventoEnum.PREVISTO.name, SituacaoEventoEnum.INICIADO.name])
#     ).first()
    
#     enable_cadastrar = evento_atual is None
    
#     page = request.args.get("page", 1, type=int)
#     per_page = 5

#     eventos = Evento.query.order_by(Evento.inicio.desc()).paginate(page=page, per_page=per_page, error_out=False)
#     return render_template('evento/list.html', eventos=eventos.items, enable_cadastrar=enable_cadastrar, pagination=eventos)

# @evento_bp.route("/cadastro", methods=['GET', 'POST'])
# @login_required
# def cadastro():
#     form = EventoForm()    
#     if form.validate_on_submit():        
#         try:
#             if Evento.query.filter(
#                 func.date(Evento.inicio) >= form.inicio.data.date(),
#                 Evento.situacao.in_([SituacaoEventoEnum.PREVISTO.name, SituacaoEventoEnum.INICIADO.name])
#             ).first() is not None:
#                 raise Exception(f"Já existe um evento cadastrado para {form.inicio.data.strftime("%A, dia %d de %B").capitalize()}.")
            
#             new_evento = Evento(
#                 nome=form.nome.data,
#                 local=form.local.data,                    
#                 inicio=form.inicio.data,
#                 duracao=form.duracao.data,
#                 situacao=form.situacao.data,
#             )
            
#             db.session.add(new_evento)
#             db.session.commit()
#             flash("Evento cadastrado com sucesso!", "success")
#             return redirect(url_for("evento.listagem"))
#         except Exception as e:
#             db.session.rollback()
#             flash(f"Atenção: {str(e)}", "warning")
#             return render_template('evento/form.html', form=form)
#         except SQLAlchemyError as e:
#             db.session.rollback()  # Garante que a sessão seja restaurada
#             print(f"Erro ao cadastrar evento: ")
#             flash("Erro ao cadastrar evento! Tente novamente mais tarde.", "warning")
#     return render_template('evento/form.html', form=form)

# @evento_bp.route("/remocao/<int:id_evento>", methods=['GET', 'POST'])
# @login_required
# def remocao(id_evento):
#     try:
#         evento = Evento.query.get_or_404(id_evento)
#         if evento.situacao.name in [SituacaoEventoEnum.INICIADO.name, SituacaoEventoEnum.ENCERRADO.name]:
#             raise Exception("Evento com situação iniciado ou encerrado não pode ser removido.")
        
#         if any([
#             Concentracao.query.filter_by(evento_id=id_evento).count(),
#             Partida.query.filter_by(evento_id=id_evento).count(),
#             Time.query.filter_by(evento_id=id_evento).count()
#         ]):
#             raise Exception("Não é possível remover evento com lista de chegada, times ou partidas vinculadas.")

#         db.session.delete(evento)
#         db.session.commit()
#         data_formatada = evento.inicio.strftime("%A, dia %d de %B").capitalize()
#         flash(f"Evento de {data_formatada} removido com sucesso!", "success")
#         return redirect(url_for("evento.listagem"))
#     except Exception as e:
#         db.session.rollback()
#         flash(f"Atenção: {str(e)}", "warning")
#         return redirect(url_for("evento.listagem"))
#     except IntegrityError as e:
#         db.session.rollback()
#         flash(f"Atenção: {str(e)}", "warning")
#         return redirect(url_for("evento.listagem"))
#     except SQLAlchemyError as e:
#         db.session.rollback()
#         flash(f"Atenção: {str(e)}", "danger")
#         return redirect(url_for("evento.listagem"))