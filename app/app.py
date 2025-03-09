from flask import Flask, render_template
from flask_login import current_user
from app.config import Config
from app.extensions import db, bcrypt, migrate, login_manager
from app.apps.auth.routes import auth_bp
from app.apps.jogador.routes import jogador_bp
from app.apps.auth.models import User

# Função user_loader para carregar o usuário
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def create_app():
    app = Flask(__name__, static_folder="static", template_folder="templates")
    app.config.from_object(Config)

    # Inicializar extensões
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"  # Definir a view de login

    # Registrar Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(jogador_bp)
    
    return app

app = create_app()

# Registrar context processor corretamente
def inject_user():
    return dict(current_user=current_user)

app.context_processor(inject_user)

# Rota de debug para verificar o usuário autenticado
@app.route('/debug_user')
def debug_user():
    if current_user.is_authenticated:
        return f"Usuário autenticado: {current_user.username}"
    return "Usuário não autenticado"

if __name__ == "__main__":
    app.run(debug=True)
