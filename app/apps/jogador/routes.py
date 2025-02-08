from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.extensions import db
from app.apps.jogador.models import Jogador
from app.apps.jogador.forms import JogadorForm

jogador_bp = Blueprint('jogador', __name__, url_prefix='/jogador',template_folder="../../templates/")

@jogador_bp.route('/cadastrar', methods=['GET', 'POST'])
@login_required
def cadastrar_jogador():
    form = JogadorForm()
    if form.validate_on_submit():
        jogador = Jogador(
            nome_camisa=form.nome_camisa.data,
            numero_camisa=form.numero_camisa.data,
            nome_completo=form.nome_completo.data,            
            is_policial_penal=form.is_policial_penal.data,
            is_associado=form.is_associado.data,
            is_mensalista=form.is_mensalista.data,
        )
        
        db.session.add(jogador)
        db.session.commit()
        
        flash('Jogador criado com sucesso!', 'success')
        return redirect(url_for('index'))
    
    return render_template('jogador/form.html', form=form)

@jogador_bp.route("/listar-jogadores")
@login_required
def listar_jogadores():
    jogadores = Jogador.query.all()
    return render_template('jogador/list.html', jogadores=jogadores)