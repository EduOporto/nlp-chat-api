from rest_api.app import *

@app.route('/', methods=['POST', 'GET'])
def log_sign():

    log_in = LogIn()
    sign_in = SignIn()

    forms = {'logIn':log_in, 'signIn':sign_in}

    if log_in.validate_on_submit():
        
        username_ = log_in.username.data
        password_ = log_in.password.data

        get_user = User.query.filter_by(username=username_).first()

        if get_user:

            if get_user.password_check(password_):
                
                login_user(get_user)

                # Update user's last login and login count
                get_user.last_login_at = datetime.now()
                get_user.login_count = get_user.login_count + 1
                db.session.commit()

                return redirect(url_for('home', username=get_user.username))
            else:
                flash(f'{username_} not logged in, wrong password!')
                return redirect(url_for('log_sign'))

        else:
            flash(f'{username_} not logged in, wrong username!')
            return redirect(url_for('log_sign'))

    elif sign_in.validate_on_submit():

        name_, n_salt_ = pablo_hasher(sign_in.name.data)
        lastname_, ln_salt_ = pablo_hasher(sign_in.last_name.data)
        email_, em_salt_ = pablo_hasher(sign_in.email.data)
        username_ = sign_in.username.data
        password_, p_salt_ = pablo_hasher(sign_in.password.data)

        new_user = User(
            name=name_, 
            n_salt=n_salt_, 
            lastname=lastname_, 
            ln_salt=ln_salt_, 
            email=email_, 
            em_salt=em_salt_, 
            username=username_, 
            password=password_, 
            p_salt=p_salt_,
            confirmed_at=datetime.now(),
            login_count=0
        )
        
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('log_sign'))

    # Condition when validation is not correct
    

    return render_template('log-sign.html', forms=forms)
