import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'minha_chave_secreta')
    WTF_CSRF_ENABLED = True
    USERNAME = os.getenv('DB_USERNAME', 'papadobradofc')
    PASSWORD = os.getenv('DB_PASSWORD', 'Senh4ppfc')
    HOST = os.getenv('DB_HOST', 'papadobradofc.mysql.pythonanywhere-services.com')
    DATABASE = os.getenv('DB_NAME', 'papadobradofc$papadobradofc')
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOGIN_VIEW = 'auth.login'
