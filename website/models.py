#database models
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    issueDescription = db.Column(db.String(1500))
    url = db.Column(db.String(200))
    screenshot = db.Column(db.String(300))
    suggested_fix = db.Column(db.String(10000))
    resolution_status = db.Column(db.String(30))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    #associate each report with a user - one to many relationship (one user, many notes)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    #create a list of notes created by this user
    reports = db.relationship('Report')