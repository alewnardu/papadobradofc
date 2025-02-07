from flask import Blueprint, render_template, redirect, url_for, flash
from app.apps.auth.forms import LoginForm
from flask_login import logout_user

auth_bp = Blueprint('auth', __name__, url_prefix='/auth',template_folder="../../templates/")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template("auth/login.html", form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash('Sessão encerrada!', 'success')
    return redirect(url_for('index'))

@auth_bp.route("/register")
def register():
    return render_template('auth/register.html')
