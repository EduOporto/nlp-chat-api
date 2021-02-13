
# Creating the APP and connecting the DB with Flask-SQLAlchemy
from flask import Flask
from sql_db.connectors.flask_SQLAlch_connector import f_sqlalch_conn

app = Flask(__name__)
db = f_sqlalch_conn(app)

# Creating the login_manager and setting the user reloader
import flask_login as fl

login_manager = fl.LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Creating the session
import os
from dotenv import load_dotenv
load_dotenv()

app.secret_key = os.getenv('flask_session')

# Import classes
from rest_api.classes.user import User