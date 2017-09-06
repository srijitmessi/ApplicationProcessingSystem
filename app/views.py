from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify, json
import os
from app import app, login_manager
from models import User
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user

@app.route('/')
@login_required
def home():
    return "Hello Boss!  <a href='/logout'>Logout</a>"

@app.route('/login')
def login():
    return render_template('login.html')

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
            return redirect("/")
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

