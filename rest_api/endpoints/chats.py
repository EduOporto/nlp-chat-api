from rest_api.app import *

@app.route('/home/<username>/chats', methods=['POST', 'GET'])
@login_required
def chats(username):
    return render_template('chats.html')