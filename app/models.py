from app import db
import datetime
from flask_login import UserMixin

class User(db.Model,UserMixin):
    __tablename__ = 'user'
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
    __tablename__ = 'student'
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
    __tablename__ = 'faculty'
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

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(400))
    createdBy = db.Column(db.String(20))
    sentTo = db.Column(db.String(20))
    readStatus = db.Column(db.Boolean)
    timeCreated = db.Column(db.DateTime)
    subject = db.Column(db.String(20))

    def __init__(self, content, createdBy, sentTo,  subject ):
        self.content = content
        self.createdBy = createdBy
	self.sentTo = sentTo 	
	self.readStatus = False
	self.timeCreated = datetime.datetime.now()
	self.subject = subject

    def markAsRead(self):
	self.readStatus = True
    
    def markAsUnread(self):
	self.readStatus = False

    def __repr__(self):
	return self.subject	
