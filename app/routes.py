from flask import Blueprint, render_template, redirect, url_for, flash
# from app.apps.evento.models import Evento
from sqlalchemy import func
from datetime import date
# from app.apps.evento.enums import SituacaoEventoEnum

home_bp = Blueprint('home', __name__, url_prefix='/',template_folder="../templates/")

@home_bp.route("/")
def home():
    return render_template('index.html', evento=None)
    # try:        
    #     evento_atual = Evento.query.filter(
    #         func.date(Evento.inicio) >= date.today(),
    #         Evento.situacao.in_([SituacaoEventoEnum.PREVISTO.name, SituacaoEventoEnum.INICIADO.name])
    #     ).first()
    #     return render_template('index.html', evento=evento_atual)
    # except Exception as e:
    #     flash(f"Atenção: {str(e)}", "warning")
    #     return render_template('index.html', evento=None)
    
    