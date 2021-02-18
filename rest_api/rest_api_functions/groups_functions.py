from rest_api.app import *

def groups_rest_users(current_user):
    # Get list of users for create a new chat
    rest_users = current_user.rest_users()

    # Get existing chats
    get_groups = current_user.get_groups(Group)

    return rest_users, get_groups

def create_group(current_user, name, users):

    # Transform usernames to classes and select the place each user will occupy
    users_classes = [User.query.filter_by(username=e).first() for e in users]

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

def post_message(group, user, message):
    new_message = Gmessage(
                    group=group,
                    user=user,
                    message=message,
                    message_date=datetime.now())
    db.session.add(new_message)
    db.session.commit()