from rest_api.app import *
from rest_api.rest_api_functions.groups_functions import groups_rest_users, create_group, post_message


@app.route('/home/<username>/groups', methods=['POST', 'GET'])
@login_required
def groups(username):

    # Get list of users for new chat and existing groups
    rest_users, get_groups = groups_rest_users(current_user)

    if request.method == 'POST':
        new_group_name = str(request.form.get('Group Name'))
        new_group_users = str(request.form.getlist('Chosen Users'))

        # Create the new group
        create_group(current_user, new_group_name, new_group_users)

        # Get the new chat
        group = Group.query.filter_by(group_name=new_group_name).first()

        return redirect(url_for('group', username=current_user.username, group=group.id))

    return render_template('groups.html',
                            groups=get_groups,
                            rest_users=rest_users,
                            User=User,
                            Group=Group)

@app.route('/home/<username>/groups/<group>', methods=['POST', 'GET'])
@login_required
def group(username, group):

    # Get list of users for new chat and existing groups
    rest_users, get_groups = groups_rest_users(current_user)
    
    # Get group
    group_ = Group.query.filter_by(id=group).first()

    # Get the users that are not in the actual chat, in order to add them
    rest_users_add = [u for u in rest_users if u not in group_.get_users()]

    # Get messages
    messages = Gmessage.query.filter_by(group=group_).all()

    # Send message
    if request.method == 'POST':
        
        # Get the message
        message = str(request.form.get('message'))

        # Post the message in the chat
        post_message(group_, current_user, message)

        return redirect(url_for('group', username=current_user.username, group=group_.id))

    return render_template('group.html',
                            groups=get_groups,
                            rest_users_new=rest_users,
                            rest_users_add=rest_users_add,
                            group=group_,
                            messages=messages,
                            User=User,
                            Group=Group)