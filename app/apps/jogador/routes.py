from flask import Blueprint, render_template
from app.apps.jogador.models import Jogador

jogador_bp = Blueprint('jogador', __name__, url_prefix='/jogador')

@jogador_bp.route("/")
def listar_jogadores():
    jogadores = Jogador.query.all()
    return render_template('jogador/list.html', jogadores=jogadores)

