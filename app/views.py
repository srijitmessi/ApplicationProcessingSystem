from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify, json
import os
from app import app, login_manager
<<<<<<< HEAD
from app.models import User
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
=======
from app.models import *
from flask_login import current_user, login_required, login_user, logout_user
>>>>>>> origin/master

@app.route('/')
@login_required
def root():
    return "Hello Boss!  <a href='/logout'>Logout</a>"

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/home')
@login_required
def home():
    if(current_user.accType == 'stud') :
        return studentHome()
    elif(current_user.accType == 'fac') :
        return facHome()

@app.route('/loginUser', methods=['POST'])
def loginUser():
    if request.method == 'POST':
        e_mail = request.form['email']
        p_word = request.form['password']
        user = User.query.filter_by(email=e_mail).first()
        if not p_word:
            return json.dumps({'status':'Please Enter Password'})
        if user is None:
            return json.dumps({'status':'Invalid Email'})
        if p_word == user.password:
            login_user(user)
            return redirect("/home")
        else:
            return json.dumps({'status':'Password Incorrect'})
    else:
        redirect("/login")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return login()

@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))

def studentHome():
    return "Welcome Student"

def facHome():
    return "Welcome Faculty"
