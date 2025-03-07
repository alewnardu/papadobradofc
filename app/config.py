import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', '9870e1457b4e12f21224f6c4354f41ff9cfea58070414c8b')
    WTF_CSRF_ENABLED = True
    USERNAME = os.getenv('DB_USERNAME', 'papadobradofc')
    PASSWORD = os.getenv('DB_PASSWORD', 'Senh4ppfc')
    HOST = os.getenv('DB_HOST', 'papadobradofc_db')
    DATABASE = os.getenv('DB_NAME', 'papadobradofc')
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOGIN_VIEW = 'auth.login'
