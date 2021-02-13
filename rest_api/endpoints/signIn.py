from rest_api.app import *
from flask import request
from hasher.hasher import pablo_hasher

@app.route('/signin')
def signIn():

    user_name_, un_salt_ = pablo_hasher(str(request.args.get('user_name')))
    user_lastname_, uln_salt_ = pablo_hasher(str(request.args.get('user_lastname')))
    user_mail_, um_salt_ = pablo_hasher(str(request.args.get('user_mail')))
    user_nick_ = request.args.get('user_nick')
    user_pass_, up_salt_ = pablo_hasher(str(request.args.get('user_pass')))

    new_user = User(user_name=user_name_, 
                    un_salt=un_salt_, 
                    user_lastname=user_lastname_, 
                    uln_salt=uln_salt_, 
                    user_mail=user_mail_, 
                    um_salt=um_salt_, 
                    user_nick=user_nick_, 
                    user_pass=user_pass_, 
                    up_salt=up_salt_)

    db.session.add(new_user)
    db.session.commit()

    return f"User '{user_nick_}' succesfully signed in"

