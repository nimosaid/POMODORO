import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgres://fuffrcocybnszz:8d493f9916b524ba1c8c6c0922f26b8ae45eb1ffd87a0775eeca451f2181c165@ec2-54-235-220-220.compute-1.amazonaws.com:5432/d804lilg5dv5kg'
class DevConfig(Config):
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}