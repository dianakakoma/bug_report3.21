from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
from .models import Report
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET','POST'])
@login_required
def home():
    if request.method == 'POST':
        report = request.form.get('report')
        print(report)
        req = request.form
        issueDescription = req.get('issueDescription')
        url = req.get('url')
        suggested_fix = req.get('suggested_fix')
        screenshot = req.get('screenshot')
        resolution_status = req.get('resolution_status')
        date = req.get('date')

        if len(issueDescription) < 1:
            flash("The report is too short!", category='error')
        else:
            new_report = Report(issueDescription=issueDescription, user_id=current_user.id, url=url, suggested_fix=suggested_fix, screenshot=screenshot, resolution_status=resolution_status, date=date )
            db.session.add(new_report)
            db.session.commit()
            flash('Report added!', category='success')
    return render_template("home.html", user=current_user)

@views.route('/delete-report', methods=['POST'])
def delete_report():
    report = json.loads(request.data)
    reportId = report['reportId']
    report = Report.query.get(reportId)
    if report:
        #user can only delete their own notes
        if report.user_id == current_user.id:
            db.session.delete(report)
            db.session.commit()
    return jsonify({})