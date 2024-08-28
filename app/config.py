import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('this_is_a_secret_uwu')
    #SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(basedir, "app.db")}'
    #SQLALCHEMY_TRACK_MODIFICATIONS = False