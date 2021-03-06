
# Creating the APP and session
from flask import Flask, render_template, request, redirect, url_for, flash
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('flask_session')

# Connecting the DB with Flask-SQLAlchemy
from sql_db.connectors.flask_SQLAlch_connector import f_sqlalch_conn

db = f_sqlalch_conn(app)

# Creating the login_manager and setting the user reloader
from flask_login import LoginManager, login_required, login_user, current_user, logout_user

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Import the hasher
from hasher.hasher import pablo_hasher

# Import models
from rest_api.models.user import User
from rest_api.models.chat import Chat
from rest_api.models.group import Group
from rest_api.models.messages import Cmessage, Gmessage

# Import forms
try:
    from rest_api.forms.forms import SignIn, LogIn, NewGroup, AddUser, RemoveUser, NewMessage, ExitGroup
except:
    pass

# Import NLTK-Vader Sentiment Analysis and instanciate it 
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

# Import miscellaneous
from datetime import datetime