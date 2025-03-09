# from flask import Blueprint, render_template, redirect, url_for, flash
# from flask_login import login_required
# from app.apps.time.models import Time
# from app.apps.escalacao.models import Escalacao
# from sqlalchemy.exc import SQLAlchemyError

# escalacao_bp = Blueprint('escalacao', __name__, url_prefix='/escalacao',template_folder="../../templates/")


# @escalacao_bp.route("/time/<int:id_time>", methods=['GET'])
# @login_required
# def listagem(id_time):
#     try:
#         time = Time.query.get_or_404(id_time)
#         escalacoes = Escalacao.query.filter_by(time_id=id_time).order_by(Escalacao.id).all()
#         return render_template('escalacao/list.html',  escalacoes=escalacoes, time=time)
#     except SQLAlchemyError as e:
#         flash("Lista de jogadores indisponível. Tente novamente mais tarde!", "danger")
#         return redirect(url_for("evento.listagem"))  # Redireciona para os times do evento

