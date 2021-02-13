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
