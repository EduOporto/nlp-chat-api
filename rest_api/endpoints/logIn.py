from rest_api.app import *
import binascii

@app.route('/login', methods=['POST', 'GET'])
def logIn():
    if request.method == 'POST':
        username_ = str(request.form.get('Username'))
        password_ = str(request.form.get('Password'))

        get_user = User.query.filter_by(username=username_).first()

        if get_user:

            db_pass = get_user.password
            db_pass_salt = binascii.unhexlify(get_user.p_salt)

            if pablo_hasher(password_, db_pass_salt) == db_pass:
                
                login_user(get_user)

                #return f'{user_nick_} succesfully logged in!'
                return redirect(url_for('home'))
            else:
                return f'{username_} not logged in, wrong password!'

        else:
            return f'{username_} not logged in, wrong username!'

    return render_template('login.html')
