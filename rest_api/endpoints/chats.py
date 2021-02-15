from rest_api.app import *

@app.route('/home/<username>/chats', methods=['POST', 'GET'])
@login_required
def chats(username):

    # Get list of users for create a new chat
    rest_users = current_user.rest_users()

    # Get existing chats
    get_chats = current_user.get_chats(Chat)

    return render_template('chats.html', chats=get_chats, rest_users=rest_users, User=User, Chat=Chat)


@app.route('/home/<username>/chats/<chat_e>', methods=['POST', 'GET'])
@login_required
def chat(username, chat_e):

    # Get list of users for create a new chat
    rest_users = current_user.rest_users()

    # Get existing chats
    get_chats = current_user.get_chats(Chat)



    return render_template('chat.html', chats=get_chats, rest_users=rest_users, User=User, Chat=Chat)

    

