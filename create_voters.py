from app.models import Voter
from app import db



def add_voters():
    voters = [Voter(national_id = "10345343", passport="", first_name = "John", last_name="Joe"), Voter(national_id = "34534454", passport="", first_name = "Jane", last_name="Joe"), Voter(national_id = "45656764", passport="", first_name = "Michael", last_name="Joe"), Voter(national_id = "23434565", passport="", first_name = "Andrew", last_name="Does")]
                
    for voter in voters:
        db.session.add(voter)
        db.session.commit()
        print("\n", voter, "\n")

