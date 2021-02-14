from rest_api.app import *

@app.route('/login', methods=['POST', 'GET'])
def logIn():
    if request.method == 'POST':
        username_ = str(request.form.get('Username'))
        password_ = str(request.form.get('Password'))

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

        else:
            flash(f'{username_} not logged in, wrong username!')

    return render_template('login.html')
