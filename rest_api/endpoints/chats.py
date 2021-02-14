from rest_api.app import *

@app.route('/home/<username>/chats', methods=['POST', 'GET'])
@login_required
def chats(username):

    get_chats = Chat.query.filter(or_(
        Chat.user_a_id == current_user.id, 
        Chat.user_b_id == current_user.id)
        ).all()

    other_user = [e.other_user(current_user.id) for e in get_chats]
    other_user_nicks = [User.query.filter_by(id=e).first().username for e in other_user]

    return render_template('chats.html', chats=other_user_nicks)