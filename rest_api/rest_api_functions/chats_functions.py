from rest_api.app import *

def chats_rest_users(current_user):
    # Get list of users for create a new chat
    rest_users = current_user.rest_users()

    # Get existing chats
    get_chats = current_user.get_chats(Chat)

    return rest_users, get_chats

def post_message(chat, user, message):

    # Message Sentiment analysis
    sentiment = sia.polarity_scores(message)

    new_message = Cmessage(
                    chat=chat,
                    user=current_user,
                    message=message,
                    message_date=datetime.now(),
                    neg_score=sentiment['neg'],
                    neu_score=sentiment['neu'],
                    pos_score=sentiment['pos'],
                    compound=sentiment['compound'])
    db.session.add(new_message)
    db.session.commit()

def create_chat(current_user, receiver):
    # Create chat
    create_chat = Chat(user_a=current_user, user_b=receiver, create_at=datetime.now())
    db.session.add(create_chat)
    db.session.commit()

    # Get chat
    chat = Chat.query.filter_by(user_a=current_user, user_b=receiver).first()

    return chat