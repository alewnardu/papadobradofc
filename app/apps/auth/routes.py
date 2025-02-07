from flask import Blueprint, render_template
from app.apps.auth.forms import LoginForm

auth_bp = Blueprint('auth', __name__, url_prefix='/auth',template_folder="../../templates/")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template("auth/login.html", form=form)


@auth_bp.route("/register")
def register():
    return render_template('auth/register.html')
