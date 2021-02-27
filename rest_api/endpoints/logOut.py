from rest_api.app import *

@app.route('/logout')
@login_required
def logOut():

    current_ = current_user.username

    logout_user()

    flash(f"User '{current_}' logged out, see you next time!")

    return redirect(url_for('log_sign'))