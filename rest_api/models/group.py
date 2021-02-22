from rest_api.app import *

class Group(db.Model):

    __tablename__ = 'users_has_groups'

    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(80), nullable=False)
    
    group_admin_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    group_admin = db.relationship('User', foreign_keys=[group_admin_id])

    user_b_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user_b = db.relationship('User', foreign_keys=[user_b_id])

    user_c_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user_c = db.relationship('User', foreign_keys=[user_c_id])

    user_d_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user_d = db.relationship('User', foreign_keys=[user_d_id])

    user_e_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user_e = db.relationship('User', foreign_keys=[user_e_id])

    user_f_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user_f = db.relationship('User', foreign_keys=[user_f_id])

    user_g_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user_g = db.relationship('User', foreign_keys=[user_g_id])

    user_h_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user_h = db.relationship('User', foreign_keys=[user_h_id])

    user_i_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user_i = db.relationship('User', foreign_keys=[user_i_id])

    user_j_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user_j = db.relationship('User', foreign_keys=[user_j_id])

    created_at = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Group %r>' % self.group_name

    def get_users(self):
        places = [self.group_admin, self.user_b, self.user_c, self.user_d, self.user_e, self.user_f, self.user_g, self.user_h, self.user_i, self.user_j]
        return [e for e in places if e != None]

    def get_empties(self):
        places = [
            (self.user_b, 'user_b'),
            (self.user_c, 'user_c'),
            (self.user_d, 'user_d'),
            (self.user_e, 'user_e'),
            (self.user_f, 'user_f'),
            (self.user_g, 'user_g'),
            (self.user_h, 'user_h'),
            (self.user_i, 'user_i'),
            (self.user_j, 'user_j')]
        return [e[1] for e in places if e[0] == None]

