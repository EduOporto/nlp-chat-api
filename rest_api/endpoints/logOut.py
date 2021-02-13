from rest_api.app import *
from flask_login import login_required, current_user, logout_user

@app.route('/logout')
@login_required
def logOut():

    current_ = current_user.user_nick

    logout_user()

    return f"User '{current_}' logged out, see you next time!"