from flask import Flask

#create the flask app and initialized the secret key
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'random string'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    return app

