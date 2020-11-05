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

class Party(db.Model):
    __tablename__ = "parties"
    party_name = db.Column(db.String, primary_key = True)
    party_logo_path = db.Column(db.String)

    presidents = db.relationship("President", back_populates="party")
    deputies = db.relationship("Deputy", back_populates="party")
    governors = db.relationship("Governor", back_populates="party")
    senators = db.relationship("Senator", back_populates="party")

class President(db.Model):
    __tablename__="presidents"
    id = db.Column(db.Integer,primary_key = True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    location = db.Column(db.String(255))
    votes = db.Column(db.Integer)
    profile_pic_path= db.Column(db.String(255))
    deputy = db.relationship("Deputy", uselist = False, back_populates = "president")

    party_name = db.Column(db.String, db.ForeignKey("parties.party_name"))
    party = db.relationship("Party", back_populates = "presidents")

    def add_vote(self):
        self.votes+=1
        db.session.add(self)
        db.session.commit()

class Deputy(db.Model):
    __tablename__="deputies"
    id = db.Column(db.Integer,primary_key = True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    location = db.Column(db.String(255))
    profile_pic_path= db.Column(db.String(255))
    president_id = db.Column(db.Integer, db.ForeignKey("presidents.id"))
    president = db.relationship("President", back_populates = "deputy")

    party_name = db.Column(db.String, db.ForeignKey("parties.party_name"))
    party = db.relationship("Party", back_populates = "deputies")

class Senator(db.Model):
    __tablename__="senators"
    id = db.Column(db.Integer,primary_key = True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    location = db.Column(db.String(255))
    profile_pic_path= db.Column(db.String(255))
    votes = db.Column(db.Integer)

    party_name = db.Column(db.String, db.ForeignKey("parties.party_name"))
    party = db.relationship("Party", back_populates = "senators")

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
    profile_pic_path= db.Column(db.String(255))
    votes = db.Column(db.Integer)

    party_name = db.Column(db.String, db.ForeignKey("parties.party_name"))
    party = db.relationship("Party", back_populates = "governors")

    def add_vote(self):
        self.votes+=1
        db.session.add(self)
        db.session.commit()
