from rest_api.app import *
from flask import request
from hasher.hasher import pablo_hasher
import binascii
from flask_login import login_user

@app.route('/login')
def logIn():
    user_nick_ = str(request.args.get('user_nick'))
    user_pass_ = str(request.args.get('user_pass'))

    get_user = User.query.filter_by(user_nick=user_nick_).first()

    if get_user:

        db_pass = get_user.user_pass
        db_pass_salt = binascii.unhexlify(get_user.up_salt)

        if pablo_hasher(user_pass_, db_pass_salt) == db_pass:
            
            login_user(get_user)

            return f'{user_nick_} succesfully logged in!'
        else:
            return f'{user_nick_} not logged in, wrong password!'

    else:
        return f'{user_nick_} not logged in, wrong username!'
