from flask import Blueprint, render_template

auth_bp = Blueprint('auth', __name__, url_prefix='/auth',template_folder="../../templates/auth")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    return render_template("auth/login.html")

@auth_bp.route("/register")
def register():
    return render_template('auth/register.html')
