from flask import Blueprint, render_template
from app.apps.jogador.models import Jogador
from flask_login import login_required

jogador_bp = Blueprint('jogador', __name__, url_prefix='/jogador',template_folder="../../templates/")

@jogador_bp.route("/")
@login_required
def listar_jogadores():
    jogadores = Jogador.query.all()
    return render_template('jogador/list.html', jogadores=jogadores)

