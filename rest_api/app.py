from flask import Flask

app = Flask(__name__)

from sql_db.sql_engine_conector.sql_engine_conector import *