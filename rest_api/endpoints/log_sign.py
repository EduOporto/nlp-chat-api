from rest_api.app import *

@app.route('/', methods=['POST', 'GET'])
def logIn():

    log_in = LogIn()

    if log_in.validate_on_submit():

        user = User.query.filter_by(username=log_in.username.data).first()

        login_user(user)

        # Update user's last login and login count
        user.last_login_at = datetime.now()
        user.login_count = user.login_count + 1
        db.session.commit()

        return redirect(url_for('home', username=user.username))    

    elif log_in.validate_on_submit() == False: 
        
        return render_template('login.html', forms=log_in)
    
    return render_template('login.html', forms=log_in)

@app.route('/signin', methods=['POST', 'GET'])
def signIn():

    sign_in = SignIn()

    if sign_in.is_submitted():

        if sign_in.validate_on_submit():

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

            flash(f"User '{username_}' succesfully created! You can LogIn now")
            return redirect(url_for('logIn'))

        elif sign_in.validate_on_submit() == False:

            return render_template('signin.html', forms=sign_in)

    return render_template('signin.html', forms=sign_in)

