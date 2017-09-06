from app import db
from flask_login import UserMixin
class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(120), unique=True)
    accType =db.Column(db.String(20), nullable=False)

    def __init__(self, email, password,accType):
        self.email = email
        self.password = password
        self.accType = accType

    def __repr__(self):
        return self.email

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True)
    vtuId = db.Column(db.String(8), unique=True)
    regId = db.Column(db.String(20), unique=True)

    def __init__(self, email, vtuId, regId):
        self.email = email
        self.vtuId = vtuId
        self.regId = regId

    def __repr__(self):
        return self.email

class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True)
    ttsId = db.Column(db.String(8), unique=True)
    regId = db.Column(db.String(20), unique=True)

    def __init__(self, email, ttsId, regId):
        self.email = email
        self.ttsId = ttsId
        self.regId = regId

    def __repr__(self):
        return self.email

