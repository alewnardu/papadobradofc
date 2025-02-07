import os
from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Optional
from flask_migrate import Migrate
from urllib.parse import quote

# Configuração do Flask
app = Flask(__name__, static_folder="static", template_folder="templates")
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'chave_secreta_padrao')  # Chave secreta vinda do ambiente

# Configuração do Banco de Dados MySQL no PythonAnywhere
# USERNAME = os.getenv('DB_USERNAME', 'papadobradofc')
# db_password = os.getenv('DB_PASSWORD', 'minha_senha_segura')  # Defina isso no ambiente
# PASSWORD = db_password.replace("\\@", "@")  # Corrige caso o $ tenha sido escapado

# HOST = os.getenv('DB_HOST', 'papadobradofc.mysql.pythonanywhere-services.com')
# db_name = os.getenv('DB_NAME', 'papadobradofc$default')
# DATABASE = db_name.replace("\\$", "$")  # Corrige caso o $ tenha sido escapado

# app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}?charset=utf8mb4'

DATABASE_URI = os.getenv('DB_URI', '')
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa as extensões
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)

# Modelo de Usuário
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    numero_camisa = db.Column(db.SmallInteger, nullable=False)
    nome_completo = db.Column(db.String(120), nullable=False)
    is_policial_penal = db.Column(db.Boolean, nullable=False, default=False)
    is_associado = db.Column(db.Boolean, nullable=False, default=False)
    is_mensalista = db.Column(db.Boolean, nullable=False, default=False)
    password = db.Column(db.String(60), nullable=False)

# Formulário de Cadastro
class RegistrationForm(FlaskForm):
    username = StringField('Nome na Pelada', validators=[DataRequired(), Length(min=3, max=25)])
    numero_camisa = IntegerField('Número da Camisa', validators=[DataRequired()])
    nome_completo = StringField('Nome Completo', validators=[DataRequired(), Length(min=3, max=120)])
    is_policial_penal = BooleanField('Policial Penal?', validators=[Optional()])
    is_associado = BooleanField('Associado SINDPPEN?', validators=[Optional()])
    is_mensalista = BooleanField('Mensalista na Pelada?', validators=[Optional()])
    password = PasswordField('Senha', validators=[DataRequired()])
    confirm_password = PasswordField('Confirmação de Senha', validators=[DataRequired(), EqualTo('password', message='As senhas não coincidem')])

# Rota para Cadastro
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(
            username=form.username.data,
            numero_camisa=int(form.numero_camisa.data),
            nome_completo=form.nome_completo.data,
            is_policial_penal=form.is_policial_penal.data or False,
            is_associado=form.is_associado.data or False,
            is_mensalista=form.is_mensalista.data or False,
            password=hashed_password
        )
        db.session.add(user)
        db.session.commit()
        flash('Sua conta foi criada com sucesso!', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', title='Cadastro', form=form)

# Página Inicial
@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)