from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from . import db
from .models import Report

views = Blueprint('views', __name__)

@views.route('/', methods=['GET','POST'])
@login_required
def home():
    if request.method == 'POST':
        report = request.form.get('report')

        if len(report) < 1:
            flash("Note is too short!", category='error')
        else:
            new_report = Report(issueDescription=report, user_id=current_user.id)
            db.session.add(new_report)
            db.session.commit()
            flash('Report added!', category='success')
    return render_template("home.html", user=current_user)