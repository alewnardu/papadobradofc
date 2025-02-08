from flask import Blueprint, render_template, redirect, url_for, flash
from app.apps.auth.forms import LoginForm, RegistrationForm
from flask_login import logout_user, login_user, current_user
from app.extensions import db, bcrypt
from app.apps.auth.models import User
from sqlalchemy.exc import SQLAlchemyError
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

auth_bp = Blueprint('auth', __name__, url_prefix='/auth',template_folder="../../templates/")

limiter = Limiter(key_func=get_remote_address)

@auth_bp.route("/login", methods=["GET", "POST"])
@limiter.limit("5 per minute", key_func=lambda: form.username.data if form.username.data else get_remote_address())
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    form = LoginForm()
    if form.validate_on_submit():
        try:
            user = User.query.filter_by(username=form.username.data).first()
        except SQLAlchemyError:
            flash("Acesso indisponível! Tente novamente mais tarde.", "warning")
            return render_template("auth/login.html", form=form)

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash("Bem-vindo, peladeiro!", "success")
            return redirect(url_for("index"))
        else:
            flash("Usuário ou senha incorretos!", "danger")
    return render_template("auth/login.html", form=form)

@auth_bp.route('/logout')
def logout():
    logout_user()
    flash('Sessão encerrada!', 'success')
    return render_template('index.html')

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        try:
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
            new_user = User(username=form.username.data, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash("Cadastro realizado com sucesso!", "success")
            return redirect(url_for("index"))
        except SQLAlchemyError:
            db.session.rollback()
            flash("Cadastro indisponível! Tente novamente mais tarde.", "warning")
    return render_template('auth/register.html', form=form)
