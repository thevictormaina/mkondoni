from app.models import Voter
from app import db

voters = [
    Voter(national_id = "10345343", first_name = "John", last_name="Joe",location="Nairobi"),
    Voter(national_id = "34534454", first_name = "Jane", last_name="Joe",location="Mombasa"),
    Voter(national_id = "45656764", first_name = "Michael", last_name="Joe",location="Kisumu"), 
    Voter(national_id = "23434565", first_name = "Andrew", last_name="Dose",location="Kwale")
    Voter(national_id = "93434565", first_name = "Sandra", last_name="Sandy",location="Nyeri")
    Voter(national_id = "53434565", first_name = "Lisa", last_name="Kitui",location="kitui")
]



def add_voters(voters):
    for voter in voters:
        db.session.add(voter)
        db.session.commit()
        print("\n", voter, "\n")

add_voters(voters)