from rest_api.app import app
from flask import request

@app.route('/login')
def logIn():
    user_nick = str(request.args.get('user_nick'))
    user_pass = str(request.args.get('user_pass'))

    return user_nick, user_pass
