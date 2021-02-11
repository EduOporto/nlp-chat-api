from rest_api.app import *
from flask import request
from hasher.hasher import pablo_hasher

@app.route('/signin')
def signIn():

    user_name, un_salt = pablo_hasher(str(request.args.get('user_name')))
    user_lastname, uln_salt = pablo_hasher(str(request.args.get('user_lastname')))
    user_mail, um_salt = pablo_hasher(str(request.args.get('user_mail')))
    user_nick = request.args.get('user_nick')
    user_pass, up_salt = pablo_hasher(str(request.args.get('user_pass')))

    signIn_query = """INSERT INTO nlp_chat_api.users 
                    (user_name, un_salt, user_lastname, uln_salt, user_mail, um_salt, user_nick, user_pass, up_salt)
                  VALUES
                    (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    values = (user_name, un_salt, user_lastname, uln_salt, user_mail, um_salt, user_nick, user_pass, up_salt)

    engine_connector().execute(signIn_query, values)

    return 'Succesfully Signed In'

