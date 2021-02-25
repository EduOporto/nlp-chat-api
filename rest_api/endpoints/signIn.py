from rest_api.app import *

@app.route('/signin', methods=['POST', 'GET'])
def signIn():

    form = SignIn()

    if form.sign_in.data and form.password == form.password_confirm:

        name_, n_salt_ = pablo_hasher(form.name)
        lastname_, ln_salt_ = pablo_hasher(form.last_name)
        email_, em_salt_ = pablo_hasher(form.email)
        username_ = form.username
        password_, p_salt_ = pablo_hasher(form.password)

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

        return redirect(url_for('logIn'))

    return render_template('register.html', form=form)

