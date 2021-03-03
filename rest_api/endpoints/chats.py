from rest_api.app import *
from rest_api.rest_api_functions.chats_functions import chats_rest_users, post_message, create_chat, messages_byDate

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

    # Get list of users for new chat and existing chats
    rest_users, get_chats = chats_rest_users(current_user)

    # Get receiver user and its chats
    receiver = User.query.filter_by(id=new_chat_user).first()

    # Check wether the user has already a chat with that receiver. If so, redirects directly to that chat
    chat_id = current_user.chat_exists(receiver, Chat)
    if chat_id:
        return redirect(url_for('chat', username=current_user.username, chat_e=chat_id))

    ## FORMS ##

    # New Message Form
    new_message = NewMessage()

    # Forms dict compilation
    forms = {'new_message':new_message}

    ## CHECK FORMS ##

    # New Message
    if new_message.send.data:

        # Create and get the chat
        chat = create_chat(current_user, receiver)
        # Get the message
        message = new_message.message.data
        # Post message in the new chat
        post_message(chat, current_user, message)

        return redirect(url_for('chat', username=current_user.username, chat_e=chat.id))

    return render_template('chat.html', 
                            chats=get_chats, 
                            rest_users=rest_users,
                            receiver=receiver,
                            messages=[],
                            User=User, 
                            Chat=Chat,
                            forms=forms)


@app.route('/home/<username>/chats/<chat_e>', methods=['POST', 'GET'])
@login_required
def chat(username, chat_e):

    # Get list of users for new chat and existing chats
    rest_users, get_chats = chats_rest_users(current_user)

    # Get chat
    chat = Chat.query.filter_by(id=chat_e).first()

    # Get messages
    messages = messages_byDate(chat)

    ## FORMS ##

    # New Message Form
    new_message = NewMessage()

    # Forms dict compilation
    forms = {'new_message':new_message}

    ## CHECK FORMS ##

    # New Message
    if new_message.send.data:
        
        # Get the message
        message = new_message.message.data
        # Post the message in the chat
        post_message(chat, current_user, message)

        return redirect(url_for('chat', username=current_user.username, chat_e=chat.id))

    return render_template('chat.html', 
                            chats=get_chats, 
                            rest_users=rest_users,
                            receiver=chat.other_user(current_user.id, User),
                            messages=messages,
                            User=User, 
                            Chat=Chat,
                            forms=forms)