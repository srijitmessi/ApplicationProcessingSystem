from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import config, os

app = Flask(__name__)
app.secret_key=os.urandom(12)
app.config['SQLALCHEMY_DATABASE_URI'] = config.database_path
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

from app import views,models
