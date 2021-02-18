from rest_api.app import *
from flask_login import UserMixin
import binascii
from sqlalchemy import or_

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
        return '<User %r>' % self.username

    def password_check(self, password):
        return pablo_hasher(password, binascii.unhexlify(self.p_salt)) == self.password
    
    def email_check(self, email):
        return pablo_hasher(email, binascii.unhexlify(self.em_salt)) == self.email

    def get_chats(self, Chat):
        return Chat.query.filter(or_(Chat.user_a == self, Chat.user_b == self)).all()

    def get_groups(self, Group):
        return Group.query.filter(or_(
                                    Group.group_admin == self,
                                    Group.user_b == self,
                                    Group.user_c == self,
                                    Group.user_d == self,
                                    Group.user_e == self,
                                    Group.user_f == self,
                                    Group.user_g == self,
                                    Group.user_h == self,
                                    Group.user_i == self,
                                    Group.user_j == self)).all()

    def chat_exists(self, receiver, Chat):
        chats = self.get_chats(Chat) 
        chats_dict = {e.other_user(self.id, User).username : e.id for e in chats}

        try:
            chat_id = chats_dict[receiver.username]
        except:
            chat_id = False
        
        return chat_id

    def rest_users(self):
        return  User.query.filter(User.username != self.username).all()