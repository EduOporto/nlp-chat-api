from flask import Flask
import os
from dotenv import load_dotenv
load_dotenv()
from flask_sqlalchemy import SQLAlchemy

def f_sqlalch_conn(app):

    sql_pass = os.getenv('MySQLPass')

    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqldb://root:{sql_pass}@localhost:3306/nlp_chat_api'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db = SQLAlchemy(app)

    return db