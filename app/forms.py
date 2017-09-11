from flask import Flask, render_template, flash, request
from wtforms import Form, validators, StringField, SubmitField


class LoginForm(Form):
    email = StringField('Email:', validators=[validators.required(), validators.Length(min=6, max=35)])
    password = StringField('Password:', validators=[validators.required(), validators.Length(min=3, max=35)])

