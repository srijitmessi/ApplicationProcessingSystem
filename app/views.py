from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from app import app, login_manager
from models import User
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user

@app.route('/')
@login_required
def home():
    return "Hello Boss!  <a href='/logout'>Logout</a>"

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        e_mail = request.form['email']
        p_word = request.form['password']
        user = User.query.filter_by(email=e_mail).first()
        if p_word == user.password:
            login_user(user)
            return redirect("/")
        else:
            return flash("Wrong email or password")
    else:
        return render_template("login.html")
    return home()

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return home()

@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))

