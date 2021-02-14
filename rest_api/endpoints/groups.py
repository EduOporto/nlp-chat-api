from rest_api.app import *

@app.route('/home/<username>/groups', methods=['POST', 'GET'])
@login_required
def groups(username):
    return render_template('groups.html')