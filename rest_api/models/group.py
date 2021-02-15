from rest_api.app import *

class Group(db.Model):

    __tablename__ = 'users_has_groups'

    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(80), nullable=False)
    
    group_admin_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    group_admin = db.relationship('User', foreign_keys=[group_admin_id])

    user_b_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user_b = db.relationship('User', foreign_keys=[user_b_id])

    user_c_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user_c = db.relationship('User', foreign_keys=[user_c_id])

    user_d_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user_d = db.relationship('User', foreign_keys=[user_d_id])

    user_e_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user_e = db.relationship('User', foreign_keys=[user_e_id])

    user_f_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user_f = db.relationship('User', foreign_keys=[user_f_id])

    user_g_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user_g = db.relationship('User', foreign_keys=[user_g_id])

    user_h_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user_h = db.relationship('User', foreign_keys=[user_h_id])

    user_i_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user_i = db.relationship('User', foreign_keys=[user_i_id])

    user_j_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user_j = db.relationship('User', foreign_keys=[user_j_id])

    def __repr__(self):
        return '<Group %r>' % self.group_name