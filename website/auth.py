from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<h3>Logoout</h3>"

@auth.route('/sign-up')
def signUp():
    return render_template("sign_up.html")
