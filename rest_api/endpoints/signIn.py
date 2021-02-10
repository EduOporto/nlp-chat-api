from rest_api.app import app
from flask import request
from hasher.hasher import pablo_hasher
from sql_db.sql_engine_conector.sql_engine_conector import *

@app.route('/signin')
def signIn():

    user_name, un_salt = pablo_hasher(str(request.args.get('user_name')))
    user_lastname, uln_salt = pablo_hasher(str(request.args.get('user_lastname')))
    user_mail, um_salt = pablo_hasher(str(request.args.get('user_mail')))
    user_nick, un_salt = pablo_hasher(str(request.args.get('user_nick')))
    user_pass, up_salt = pablo_hasher(str(request.args.get('user_pass')))

    signIn_query = f"""INSERT INTO nlp_chat_api.users 
                        (user_name, un_salt, user_lastname, uln_salt, user_mail, um_salt, user_nick, user_pass, up_salt)
                        VALUES
                        ('{user_name}', 
                        '{un_salt}', 
                        '{user_lastname}', 
                        '{uln_salt}', 
                        '{user_mail}', 
                        '{um_salt}', 
                        '{user_nick}', 
                        '{un_salt}', 
                        '{user_pass}', 
                        '{up_salt}')"""

    engine_connector().execute(signIn_query)

    return 'Succesfully Signed In'

