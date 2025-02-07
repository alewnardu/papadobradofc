from flask import Flask, Blueprint, render_template
from app.config import Config
from app.extensions import db, bcrypt, migrate
from app.apps.auth.routes import auth_bp
from app.apps.jogador.routes import jogador_bp

def create_app():
    app = Flask(__name__, static_folder="static", template_folder="templates")
    app.config.from_object(Config)

    # Inicializar extensões
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    # Registrar Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(jogador_bp)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
