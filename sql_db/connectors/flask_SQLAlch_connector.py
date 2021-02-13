from flask import Flask
import os
from dotenv import load_dotenv
load_dotenv()
from flask_sqlalchemy import SQLAlchemy

def f_sqlalch_conn(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db = SQLAlchemy(app)

    return db