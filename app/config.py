import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'minha_chave_secreta')
    WTF_CSRF_ENABLED = True
    USERNAME = os.getenv('DB_USERNAME', 'admin')
    PASSWORD = os.getenv('DB_PASSWORD', 'password')
    HOST = os.getenv('DB_HOST', 'default.mysql.pythonanywhere-services.com')
    DATABASE = os.getenv('DB_NAME', 'papadobradofc$default')
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOGIN_VIEW = 'auth.login'
