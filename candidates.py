from app.models import PresidentialS,Gubernatorials,Senetorials
from app import db

Presidentials = [
    Presidential(first_name = "John", last_name="Joe",location="Kenya",votes=0),
    Presidential(first_name = "Jane", last_name="Joe",location="Kenya",votes=0),
    Presidential(first_name = "Uhuru", last_name="Kenyatta",location="Kenya",votes=0), 
    Presidential(first_name = "Raila", last_name="Odinga",location="Kenya",votes=0)
    Presidential(first_name = "William", last_name="Ruto",location="Kenya",votes=0)
    Presidential(first_name = "Kalonzo", last_name="Musyoka",location="Kenya",votes=0,)
]

def presidentials_votes(presidentials):
    for Presidential in presidentials:
        db.session.add(Presidential)
        db.session.commit()
        print("\n", voter, "\n")

add_presidents(Presidential)

