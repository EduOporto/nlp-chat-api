from rest_api.app import *
from rest_api.rest_api_functions.groups_functions import groups_rest_users, create_group, post_message, add_users, remove_users, exit_group, messages_byDate


@app.route('/home/<username>/groups', methods=['POST', 'GET'])
@login_required
def groups(username):

    # Get list of users for new chat and existing groups
    rest_users, get_groups = groups_rest_users(current_user)

    # New Group Form
    new_group = NewGroup()
    new_group.users.choices = [(u.id, u.username) for u in rest_users]

    if new_group.create.data:

        new_group_name = new_group.group_name.data
        new_group_users = new_group.users.data

        # Create the group and get it
        created_group = create_group(current_user, new_group_name, new_group_users)
        
        return redirect(url_for('group', username=current_user.username, group=created_group.id))

    forms = {'new_group':new_group}

    return render_template('groups.html',
                            groups=get_groups,
                            rest_users=rest_users,
                            User=User,
                            Group=Group,
                            forms=forms)

@app.route('/home/<username>/groups/<group>/admin', methods=['POST', 'GET'])
@login_required
def group_admin(username, group):

    ## PAGE CONTENT ##
    
    # Get list of users for new chat and existing groups
    rest_users, get_groups = groups_rest_users(current_user)
    
    # Get group
    group_ = Group.query.filter_by(id=group).first()

    # Get messages
    messages = messages_byDate(group_)

    ## FORMS ##

    # New Message Form
    new_message = NewMessage()
    
    # Add New User Form
    rest_users_add = [(u.id, u.username) for u in rest_users if u not in group_.get_users()] # Get the users that are not in the actual chat, in order to add them
    new_user = AddUser()
    new_user.new_user.choices = rest_users_add

    # Remove User Form
    remove_user = RemoveUser()
    remove_user.remove_user.choices = [(u.id, u.username) for u in group_.get_users() if u != current_user]

    # New Group Form
    new_group = NewGroup()
    new_group.users.choices = [(u.id, u.username) for u in rest_users]

    # Forms dict compilation
    forms = {'new_group':new_group, 'new_user':new_user, 'new_message':new_message, 'remove_user':remove_user}

    ## CHECK FORMS ##
    
    # New Message
    if new_message.send.data:
        
        message = new_message.message.data

        # Post the message in the chat
        post_message(group_, current_user, message)

        return redirect(url_for('group_admin', username=current_user.username, group=group_.id))

    # Add User
    elif new_user.add.data:
        
        if new_user.is_on_limit(len(group_.get_empties())):
            
            users_to_add = new_user.new_user.data
            add_users(group_, users_to_add)

            return redirect(url_for('group_admin', username=current_user.username, group=group_.id))

    # Remove User
    elif remove_user.remove.data:

        users_to_remove = remove_user.remove_user.data
        remove_users(group_, users_to_remove)

        return redirect(url_for('group_admin', username=current_user.username, group=group_.id))

    # Create New Group
    elif new_group.create.data:

        new_group_name = new_group.group_name.data
        new_group_users = new_group.users.data

        # Create the group and get it
        created_group = create_group(current_user, new_group_name, new_group_users)
        
        return redirect(url_for('group_admin', username=current_user.username, group=created_group.id))

    return render_template('group_admin.html',
                            groups=get_groups,
                            rest_users_new=rest_users,
                            rest_users_add=rest_users_add,
                            group=group_,
                            messages=messages,
                            User=User,
                            Group=Group,
                            forms=forms)

@app.route('/home/<username>/groups/<group>', methods=['POST', 'GET'])
@login_required
def group(username, group):

    ## PAGE CONTENT ##
    
    # Get list of users for new chat and existing groups
    rest_users, get_groups = groups_rest_users(current_user)
    
    # Get group
    group_ = Group.query.filter_by(id=group).first()

    # Get messages
    messages = messages_byDate(group_)

    ## FORMS ##

    # New Message Form
    new_message = NewMessage()

    # Exit Group
    exit_ = ExitGroup()

    # New Group Form
    new_group = NewGroup()
    new_group.users.choices = [(u.id, u.username) for u in rest_users]

    # Forms dict compilation
    forms = {'new_group':new_group, 'new_message':new_message, 'exit_':exit_}

    ## CHECK FORMS ##

    # New Message
    if new_message.send.data:
        
        message = new_message.message.data

        # Post the message in the chat
        post_message(group_, current_user, message)

        return redirect(url_for('group', username=current_user.username, group=group_.id))

    # Exit group
    elif exit_.exit_.data:

        exit_group(group_, current_user)

        return redirect(url_for('groups', username=current_user.username))
    
    # Create New Group
    elif new_group.create.data:

        new_group_name = new_group.group_name.data
        new_group_users = new_group.users.data

        # Create the group and get it
        created_group = create_group(current_user, new_group_name, new_group_users)
        
        return redirect(url_for('group', username=current_user.username, group=created_group.id))

    return render_template('group.html',
                            groups=get_groups,
                            rest_users_new=rest_users,
                            group=group_,
                            messages=messages,
                            User=User,
                            Group=Group,
                            forms=forms)