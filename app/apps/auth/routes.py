from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import logout_user, login_user, current_user, login_required
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from app.extensions import db, bcrypt
from app.apps.auth.forms import LoginForm, RegistrationForm
from app.apps.auth.models import User
from app.apps.jogador.models import Jogador

auth_bp = Blueprint('auth', __name__, url_prefix='/autenticacao',template_folder="../../templates/")

@auth_bp.route("/usuarios/listagem", methods=['GET'])
@login_required
def listagem():
    try:
        page = request.args.get('page', 1, type=int)
        per_page = 5
        
        usuarios = User.query.order_by(User.username).paginate(page=page, per_page=per_page, error_out=False)
        return render_template('auth/list.html', usuarios=usuarios.items, pagination=usuarios)
    except SQLAlchemyError as e:
        flash("Lista de usuários indisponível. Tente novamente mais tarde!", "danger")
        return redirect(url_for("home.home"))
    
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home.home"))

    form = LoginForm()
    if form.validate_on_submit():
        try:
            user = User.query.filter_by(username=form.username.data).first()
        except SQLAlchemyError:
            flash("Acesso indisponível! Tente novamente mais tarde.", "warning")
            return render_template("auth/login.html", form=form)
        
        if user and user.check_password(form.password.data):
            if user.is_active:
                login_user(user, remember=True)
                flash("Bem-vindo, peladeiro!", "success")
                return redirect(url_for("home.home"))
            else:
                flash("Conta inativa! Por favor, entre em contato com o administrador.", "warning")
                return render_template("auth/login.html", form=form)
        else:
            flash("Usuário ou senha incorretos!", "danger")
            return render_template("auth/login.html", form=form)
    return render_template("auth/login.html", form=form)

@auth_bp.route('/logout')
def logout():
    logout_user()
    flash('Sessão encerrada!', 'success')
    return redirect(url_for('home.home'))

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        try:
            if User.query.filter_by(username=form.username.data).first() is not None:
                raise Exception(f'O nome "{form.username.data}" de usuário já utilizado! Tente novamente outro nome.')
        
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
            new_user = User(username=form.username.data, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            
            perfil_jogador = Jogador(
                nome_camisa=new_user.username,
                numero_camisa=User.query.count() + 1,
                nome_completo=new_user.username,
                user_id=new_user.id
            )
            db.session.add(perfil_jogador)
            db.session.commit()
            flash("Cadastro realizado com sucesso! Acione um administrador para ativar sua conta.", "success")
            return redirect(url_for("home.home"))
        except IntegrityError as e:
            db.session.rollback()
            print(f"Erro de integridade: {str(e)}")
            flash("Este nome de usuário já está em uso. Escolha outro.", "warning")

        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Erro no banco de dados ao cadastrar usuário: {str(e)}")
            flash("Erro ao cadastrar! Tente novamente mais tarde.", "warning")

        except Exception as e:
            db.session.rollback()
            print(f"Erro inesperado: {str(e)}")
            flash("Ocorreu um erro inesperado. Tente novamente.", "danger")
    return render_template('auth/register.html', form=form)
