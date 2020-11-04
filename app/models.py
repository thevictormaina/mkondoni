from . import db 
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_voter(voter_id):
    return voter.query.get(int(voter_id))


class Voter(UserMixin,db.Model):
    __tablename__ = 'voters'

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

    def add_vote(self):
        self.votes+=1
        db.session.add(self)
        db.session.commit()

class Sentor(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    location = db.Column(db.String(255))
    votes = db.Column(db.Integer)

    def add_vote(self):
        self.votes+=1
        db.session.add(self)
        db.session.commit()


class Governor(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    location = db.Column(db.String(255))
    votes = db.Column(db.Integer)

    def add_vote(self):
        self.votes+=1
        db.session.add(self)
        db.session.commit()