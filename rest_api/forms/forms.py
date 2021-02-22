from flask_wtf import FlaskForm
from wtforms.fields import StringField, SelectMultipleField, SubmitField, TextAreaField
from wtforms.validators import InputRequired
from rest_api.forms.chosenselect import ChosenSelect


class NewGroup(FlaskForm):
    group_name = StringField(
        'group_name',
        render_kw={'class':'group_name'}, 
        validators=[InputRequired()])
    users = SelectMultipleField(
        'users_selected',
        widget=ChosenSelect(multiple=True, options={'width': '180px', 'height': '30px', 'padding-left': '20px'}),
        validators=[InputRequired()])
    create = SubmitField(
        'Create',
        render_kw={'class':'input_newg'})

class AddUser(FlaskForm):
    new_user = SelectMultipleField(
        'users_selected', 
        widget=ChosenSelect(multiple=True, options={'width': '180px', 'height': '30px', 'padding-left': '20px'}),
        validators=[InputRequired()])
    add = SubmitField(
        'Add',
        render_kw={'class':'input_newg'})

class RemoveUser(FlaskForm):
    remove_user = SelectMultipleField(
        'users_selected', 
        widget=ChosenSelect(multiple=True, options={'width': '180px', 'height': '30px', 'padding-left': '20px'}),
        validators=[InputRequired()])
    remove = SubmitField(
        'Remove',
        render_kw={'class':'input_newg'})

class NewMessage(FlaskForm):
    message = TextAreaField(
        'message',
        render_kw={'class':'textinput'})
    send = SubmitField(
        'Send',
        render_kw={'class':'send'})