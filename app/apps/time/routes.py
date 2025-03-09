from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from app.extensions import db, bcrypt
from app.apps.auth.models import User
from app.apps.jogador.models import Jogador
from app.apps.jogador.forms import JogadorForm
from sqlalchemy.exc import SQLAlchemyError
from app.apps.jogador.enums import SituacaoJogadorEnum

time_bp = Blueprint('time', __name__, url_prefix='/times',template_folder="../../templates/")

@time_bp.route("/listagem")
@login_required
def listagem():
    page = request.args.get("page", 1, type=int)
    per_page = 10

    times_pagination = Time.query.order_by(Time.nome).paginate(page=page, per_page=per_page, error_out=False)
    
    return render_template(
        "time/list.html", 
        times=times_pagination.items,  # Times da página atual
        pagination=times_pagination  # Objeto de paginação para os links
    )
