from rest_api.app import *

class Cmessage(db.Model):

    __tablename__ = 'chat_messages'

    id = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.Integer, db.ForeignKey('users_has_chats.id'), nullable=False)
    chat = db.relationship('Chat', foreign_keys=[chat_id])

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', foreign_keys=[user_id])

    message = db.Column(db.Text, nullable=False)
    message_date = db.Column(db.DateTime, nullable=False)

    # Sentiment data
    neg_score = db.Column(db.Float, nullable=False)
    neu_score = db.Column(db.Float, nullable=False)
    pos_score = db.Column(db.Float, nullable=False)
    compound = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Cmessage %r>' % self.id

class Gmessage(db.Model):

    __tablename__ = 'group_messages'

    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('users_has_groups.id'), nullable=False)
    group = db.relationship('Group', foreign_keys=[group_id])

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', foreign_keys=[user_id])    

    message = db.Column(db.Text, nullable=False)
    message_date = db.Column(db.DateTime, nullable=False)

    # Sentiment data
    neg_score = db.Column(db.Float, nullable=False)
    neu_score = db.Column(db.Float, nullable=False)
    pos_score = db.Column(db.Float, nullable=False)
    compound = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Gmessage %r>' % self.id