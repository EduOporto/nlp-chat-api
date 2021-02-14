from rest_api.app import *
from flask_login import UserMixin

class User(UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.LargeBinary, nullable=False)
    n_salt = db.Column(db.LargeBinary, nullable=False)
    lastname = db.Column(db.LargeBinary, nullable=False)
    ln_salt = db.Column(db.LargeBinary, nullable=False)
    email = db.Column(db.LargeBinary, nullable=False)
    em_salt = db.Column(db.LargeBinary, nullable=False)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.LargeBinary, nullable=False)
    p_salt = db.Column(db.LargeBinary, nullable=False)
    confirmed_at = db.Column(db.DateTime, nullable=False)
    last_login_at = db.Column(db.DateTime, nullable=True)
    login_count = db.Column(db.Integer)

    def __repr__(self):
        return '<User %r>' % self.user_name

class Chat(db.Model):

    __tablename__ = 'users_has_chats'

    id = db.Column(db.Integer, primary_key=True)
    user_a_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user_b_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return '<Chat %r>' % self.id

class Group(db.Model):

    __tablename__ = 'users_has_groups'

    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(80), nullable=False)
    group_admin_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user_b_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user_c_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user_d_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user_e_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user_f_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user_g_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user_h_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user_i_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user_j_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return '<Group %r>' % self.group_name

class Cmessage(db.Model):

    __tablename__ = 'chat_messages'

    id = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.Integer, db.ForeignKey('users_has_chats.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    message = db.Column(db.Text, nullable=False)
    message_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Cmessage %r>' % self.id

class Gmessage(db.Model):

    __tablename__ = 'group_messages'

    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('users_has_groups.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    message = db.Column(db.Text, nullable=False)
    message_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Gmessage %r>' % self.id