from rest_api.app import db
from flask_login import UserMixin

class User(UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.LargeBinary, nullable=False)
    un_salt = db.Column(db.LargeBinary, nullable=False)
    user_lastname = db.Column(db.LargeBinary, nullable=False)
    uln_salt = db.Column(db.LargeBinary, nullable=False)
    user_mail = db.Column(db.LargeBinary, nullable=False)
    um_salt = db.Column(db.LargeBinary, nullable=False)
    user_nick = db.Column(db.String(80), nullable=False, unique=True)
    user_pass = db.Column(db.LargeBinary, nullable=False)
    up_salt = db.Column(db.LargeBinary, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.user_name