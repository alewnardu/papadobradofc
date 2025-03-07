from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from app.apps.concentracao.models import Concentracao
from app.apps.evento.models import Evento
from sqlalchemy.exc import SQLAlchemyError
from app.apps.concentracao.forms import ConcentracaoForm
from datetime import datetime
from app.extensions import db
from app.apps.jogador.models import Jogador

concentracao_bp = Blueprint('concentracao', __name__, url_prefix='/concentracao',template_folder="../../templates/")

@concentracao_bp.route("/<int:id_evento>/listagem", methods=['GET'])
@login_required
def listagem(id_evento):
    evento = Evento.query.get_or_404(id_evento)
    try:
        concentracoes = Concentracao.query.filter_by(evento_id=evento.id).order_by(Concentracao.momento_checkin).all()
        return render_template('concentracao/list.html',  concentracoes=concentracoes, evento=evento)
    except SQLAlchemyError as e:
        flash("Lista de chegada indisponível. Tente novamente mais tarde!", "danger")
        return redirect(url_for("evento.listagem"))

@concentracao_bp.route("/<int:id_evento>/remocao/<int:id_concentracao>", methods=['GET', 'POST'])
@login_required
def remocao(id_evento, id_concentracao):
    try:
        concentracao = Concentracao.query.filter_by(id=id_concentracao, evento_id=id_evento).first()
        if concentracao:
            db.session.delete(concentracao)
            db.session.commit()
            flash(f"Jogador {concentracao.jogador} removido da lista de chegada!", "success")
        else:
            flash("Não foi possível concluir a operação de remoção do jogador da lista de chegada.", "warning")
        return redirect(url_for("concentracao.listagem", id_evento=id_evento))
    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"Erro ao remover jogador da lista de chegada: {str(e)}")
        flash("Remoção da lista de chegada indisponível. Tente novamente mais tarde.", "warning")
        return redirect(url_for("concentracao.listagem", id_evento=id_evento))

@concentracao_bp.route("/<int:id_evento>/cadastro", methods=['GET', 'POST'])
@login_required
def cadastro(id_evento):
    form = ConcentracaoForm()
    if form.validate_on_submit():
        try:
            print("Chegada do Jogador: ", form.jogador.data)
            evento = Evento.query.get_or_404(id_evento)
            jogador = Jogador.query.get_or_404(form.jogador.data.id)
            if Concentracao.query.filter_by(evento_id=evento.id, jogador_id=jogador.id).first() is None:
                new_concentracao = Concentracao(
                    momento_checkin=datetime.now(),
                    evento_id=evento.id,
                    jogador_id=jogador.id,
                )
                db.session.add(new_concentracao)
                db.session.commit()
                flash("Lista de chegada atualizada com sucesso!", "success")
                return redirect(url_for("concentracao.listagem", id_evento=evento.id))
            flash(f"O jogador {jogador} já está na lista de chegada!", "warning")
            return render_template('concentracao/form.html', form=form, id_evento=id_evento)
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Erro ao cadastrar ordem de chegada: {str(e)}")
            flash("Erro ao cadastrar ordem de chegada! Tente novamente mais tarde. ", "warning")
    return render_template('concentracao/form.html', form=form, id_evento=id_evento)