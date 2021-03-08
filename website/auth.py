from flask import Blueprint, render_template,request,flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    #getting the input data from the form
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<h3>Logoout</h3>"

@auth.route('/sign-up', methods=['GET','POST'])
def signUp():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 5:
            flash("Email must be longer than 4 characters.", category='error')
        elif len(firstName) < 2:
            flash("Your first name must be longer than 2 characters.", category='error')
        elif password1 != password2:
            flash("Your confirmation does not match", category='error')
        else:
            #if all conditions have been met congratulate the user on the success.
            flash("Congratulations, account successfully created.", category='success')
    return render_template("sign_up.html")
