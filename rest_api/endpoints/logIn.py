from rest_api.app import *
from flask import request
from hasher.hasher import pablo_hasher
import binascii, pandas as pd

@app.route('/login')
def logIn():
    user_nick = str(request.args.get('user_nick'))
    user_pass = str(request.args.get('user_pass'))

    logIn_query = f"""SELECT user_pass, up_salt FROM nlp_chat_api.users
                        WHERE user_nick = '{user_nick}'"""

    result = pd.read_sql(logIn_query, engine_connector())

    db_pass = result.user_pass[0]
    db_pass_salt = binascii.unhexlify(result.up_salt[0])

    if pablo_hasher(user_pass, db_pass_salt) == db_pass:
        return f'{user_nick} succesfully loggd in!'

    else:
        return f'{user_nick} not logged in. Either user or password is incorrect'
