from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db - SQLAlchemy()
DB_NAME = "database.db"

#create the flask app and initialized the secret key
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'random string'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite///{DB_NAME}'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    #initializing the database
    db.init_app(app)

    return app

