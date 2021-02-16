from rest_api.app import *

def chats_rest_users(current_user):
    # Get list of users for create a new chat
    rest_users = current_user.rest_users()

    # Get existing chats
    get_chats = current_user.get_chats(Chat)

    return rest_users, get_chats

def post_message(chat, user, message):
    new_message = Cmessage(
                    chat=chat,
                    user=current_user,
                    message=message,
                    message_date=datetime.now())
    db.session.add(new_message)
    db.session.commit()

@app.route('/home/<username>/chats', methods=['POST', 'GET'])
@login_required
def chats(username):

    # Get list of users for new chat and existing chats
    rest_users, get_chats = chats_rest_users(current_user)

    return render_template('chats.html', 
                            chats=get_chats, 
                            rest_users=rest_users, 
                            User=User, 
                            Chat=Chat)


@app.route('/home/<username>/chats/new_chat/<new_chat_user>', methods=['POST', 'GET'])
@login_required
def new_chat(username, new_chat_user): 

    # Get receiver user and its chats
    receiver = User.query.filter_by(id=new_chat_user).first()

    # Check wether the user has already a chat with that receiver. If so, redirects directly to that chat
    chat_id = current_user.chat_exists(receiver, Chat)
    if chat_id:
        return redirect(url_for('chat', username=current_user.username, chat_e=chat_id))

    # Get list of users for new chat and existing chats
    rest_users, get_chats = chats_rest_users(current_user)

    if request.method == 'POST':

        # Create chat
        create_chat = Chat(user_a=current_user, user_b=receiver, create_at=datetime.now())
        db.session.add(create_chat)
        db.session.commit()

        # Get chat
        chat = Chat.query.filter_by(user_a=current_user, user_b=receiver).first()

        # Create message
        message = str(request.form.get('message'))
        post_message(chat, current_user, message)

        return redirect(url_for('chat', username=current_user.username, chat_e=chat.id))

    return render_template('chat.html', 
                            chats=get_chats, 
                            rest_users=rest_users,
                            receiver=receiver,
                            messages=[],
                            User=User, 
                            Chat=Chat)


@app.route('/home/<username>/chats/<chat_e>', methods=['POST', 'GET'])
@login_required
def chat(username, chat_e):

    # Get list of users for new chat and existing chats
    rest_users, get_chats = chats_rest_users(current_user)

    # Get chat
    chat = Chat.query.filter_by(id=chat_e).first()

    # Get messages
    messages = Cmessage.query.filter_by(chat=chat).all()

    # Send message
    if request.method == 'POST':
        
        # Create message
        message = str(request.form.get('message'))
        post_message(chat, current_user, message)

        return redirect(url_for('chat', username=current_user.username, chat_e=chat.id))

    return render_template('chat.html', 
                            chats=get_chats, 
                            rest_users=rest_users,
                            receiver=chat.other_user(current_user.id, User),
                            messages=messages,
                            User=User, 
                            Chat=Chat)
    

