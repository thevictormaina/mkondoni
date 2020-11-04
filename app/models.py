class Voter(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key = True)
    national_id = db.Column(db.Integer)
    passport = db.Column(db.Integer)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    location = db.Column(db.String(255))

class President(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    location = db.Column(db.String(255))
    votes = db.Column(db.Integer)