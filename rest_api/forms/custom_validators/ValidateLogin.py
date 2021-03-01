from rest_api.models.user import User
from wtforms.validators import ValidationError

def ValidateLogin(form, field):

    username_entered = form.username.data
    password_entered = field.data

    user = User.query.filter_by(username=username_entered).first()

    if user == None:
        raise ValidationError(f"No username registered as {username_entered}")

    elif user.password_check(password_entered) == False:
        raise ValidationError("Wrong password!")