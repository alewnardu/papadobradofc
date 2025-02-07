from flask import Flask, render_template
from app.config import Config
from app.extensions import db, bcrypt, migrate, login_manager
from flask_login import current_user
from app.apps.auth.routes import auth_bp
from app.apps.jogador.routes import jogador_bp
from app.apps.auth.models import User

# Função user_loader para carregar o usuário
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  # Ajuste conforme o seu modelo de User

def create_app():
    app = Flask(__name__, static_folder="static", template_folder="templates")
    app.config.from_object(Config)

    # Inicializar extensões
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Registrar Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(jogador_bp)

    @app.context_processor
    def inject_user():
        return dict(current_user=current_user)
    
    @app.route('/')
    def index():
        return render_template('index.html')

    login_manager.login_view = "auth.login"

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
