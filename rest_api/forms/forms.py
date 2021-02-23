from flask_wtf import FlaskForm
from wtforms.fields import StringField, SelectMultipleField, SubmitField, TextAreaField
from wtforms.validators import InputRequired
from rest_api.forms.chosenselect import ChosenSelect


class NewGroup(FlaskForm):
    group_name = StringField(
        'group_name',
        render_kw={'class':'group_name'}, 
        validators=[InputRequired(message='Group needs a name!')])
    users = SelectMultipleField(
        'users_selected',
        widget=ChosenSelect(multiple=True, options={'width': '180px', 'height': '30px', 'padding-left': '20px'}),
        validators=[InputRequired(message='Select at least one user')])
    create = SubmitField(
        'Create',
        render_kw={'class':'input_newg'})

class AddUser(FlaskForm):
    new_user = SelectMultipleField(
        'users_selected', 
        widget=ChosenSelect(multiple=True, options={'width': '180px', 'height': '30px', 'padding-left': '20px'}),
        validators=[InputRequired(message='Select at least one user')])
    add = SubmitField(
        'Add',
        render_kw={'class':'input_newg'})

    def is_on_limit(self, limit):
        n_selected = len(self.new_user.data)

        if n_selected > limit:
            self.new_user.errors.append(f'No space for {n_selected} more users, select just {limit} users')
            return False
        return True

class RemoveUser(FlaskForm):
    remove_user = SelectMultipleField(
        'users_selected', 
        widget=ChosenSelect(multiple=True, options={'width': '180px', 'height': '30px', 'padding-left': '20px'}),
        validators=[InputRequired(message='Select at least one user')])
    remove = SubmitField(
        'Remove',
        render_kw={'class':'input_newg'})

class NewMessage(FlaskForm):
    message = TextAreaField(
        'message',
        render_kw={'class':'textinput', 'placeholder':'Type a message'},
        validators=[InputRequired(message='You must write something!')])
    send = SubmitField(
        'Send',
        render_kw={'class':'send', 'type':'submit'})

class ExitGroup(FlaskForm):
    exit_ = SubmitField(
        'Exit Group',
        render_kw={'class':'exit_group'}
    )