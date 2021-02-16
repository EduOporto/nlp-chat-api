from rest_api.app import *

class Chat(db.Model):

    __tablename__ = 'users_has_chats'

    id = db.Column(db.Integer, primary_key=True)
    user_a_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user_a = db.relationship('User', foreign_keys=[user_a_id])

    user_b_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user_b = db.relationship('User', foreign_keys=[user_b_id])

    create_at = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Chat %r>' % self.id

    def other_user(self, user_caller, User): 
        
        if self.user_a_id == user_caller:
            id_ = self.user_b_id
        else:
            id_ = self.user_a_id

        return User.query.filter_by(id=id_).first()