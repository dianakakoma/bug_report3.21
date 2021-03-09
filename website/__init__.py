from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

#create the flask app and initialized the secret key
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'random string'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Report

    #initializing the database
    db.init_app(app)

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    #confirm if database already exists so that we don't overwrite it.
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print("Created database!")

