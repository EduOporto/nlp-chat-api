from rest_api.app import *

def groups_rest_users(current_user):
    # Get list of users for create a new chat
    rest_users = current_user.rest_users()

    # Get existing chats
    get_groups = current_user.get_groups(Group)

    return rest_users, get_groups

def create_group(current_user, name, users):

    # Transform usernames to classes and select the place each user will occupy
    users_classes = [User.query.filter_by(id=int(e)).first() for e in users]

    places = ['user_b', 'user_c', 'user_d', 'user_e', 'user_f', 'user_g', 'user_h', 'user_i', 'user_j']

    kwargs = dict(zip(places[:len(users)], users_classes))
    
    # Create the group
    new_group = Group(
        group_name=name,
        group_admin=current_user,
        **kwargs,
        created_at=datetime.now()
    )
    db.session.add(new_group)
    db.session.commit()

    # Get the created group
    created_group = Group.query.filter_by(group_name=name).first()

    return created_group

def post_message(group, user, message):

    # Message Sentiment analysis
    sentiment = sia(message)

    new_message = Gmessage(
                    group=group,
                    user=user,
                    message=message,
                    message_date=datetime.now(),
                    neg_score=sentiment['neg'],
                    neu_score=sentiment['neu'],
                    pos_score=sentiment['pos'],
                    compound=sentiment['compound'])
    db.session.add(new_message)
    db.session.commit()

def add_users(group, users):

    users_classes = [User.query.filter_by(id=int(e)).first() for e in users]
    places = group.get_empties()

    kwargs = dict(zip(places[:len(users)], users_classes))

    group.update(**kwargs)

def remove_users(group, users):

    users_classes = [User.query.filter_by(id=int(e)).first() for e in users]
    users_places = [group.user_place(u) for u in users_classes]

    kwargs = dict(zip(users_places, [None] * len(users)))

    group.update(**kwargs)

def exit_group(group, user):

    place = group.user_place(user)

    group.update(**{place:None})