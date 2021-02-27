from flask_wtf import FlaskForm
from wtforms.fields import StringField, SelectMultipleField, SubmitField, TextAreaField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, Email, Length, EqualTo
from rest_api.forms.chosenselect import ChosenSelect

class SignIn(FlaskForm):
    name = StringField('name', validators=[InputRequired()])
    last_name = StringField('last_name', validators=[InputRequired()])
    email = EmailField('email', validators=[Email()])
    username = StringField('username', validators=[InputRequired(), Length(min=6, max=20, message=('Username must have a length of 6 to 20 characters'))])
    password = PasswordField('password', validators=[InputRequired()])
    password_confirm = PasswordField('password_confirm', validators=[InputRequired(), EqualTo('password', message="Passwords don't match!")])
    sign_in = SubmitField('Sign In', render_kw={'class':'submit-'})

class LogIn(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired()])
    log_in = SubmitField('Login', render_kw={'class':'submit-'})

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