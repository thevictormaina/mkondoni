from .. import db 
from flask_login import UserMixin
from .. import login_manager

@login_manager.user_loader
def load_voter(voter_id):
    return Voter.query.get(int(voter_id))


class Voter(UserMixin,db.Model):
    __tablename__ = 'voters'

    id = db.Column(db.Integer,primary_key = True)
    national_id = db.Column(db.String, unique = True)
    passport = db.Column(db.String, unique = True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    location = db.Column(db.String(255))
    voted = db.Column(db.Boolean, default = False)

    def has_voted(self):
        """
        Method to set Voter.voted to true
        """
        self.voted = True
        db.session.commit()

class President(db.Model):
    __tablename__="presidents"
    id = db.Column(db.Integer,primary_key = True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    location = db.Column(db.String(255))
    votes = db.Column(db.Integer)

    def add_vote(self):
        self.votes+=1
        db.session.add(self)
        db.session.commit()

class Senator(db.Model):
    __tablename__="senators"
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
    __tablename__="governors"
    id = db.Column(db.Integer,primary_key = True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    location = db.Column(db.String(255))
    votes = db.Column(db.Integer)

    def add_vote(self):
        self.votes+=1
        db.session.add(self)
        db.session.commit()
