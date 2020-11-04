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

 Gubernatorials = [
     gubernatorial(first_name = "Lee", last_name="Kinyanjui",location="Nyeri",votes=0),
     gubernatorial(first_name = "Samuel", last_name="Kamau",location="Nairobi",votes=0),
     gubernatorial(first_name = "Agnes", last_name="Joe",location="Kisumu",votes=0), 
     gubernatorial(first_name = "Andrew", last_name="Onyango",location="Mombasa",votes=0)
     gubernatorial(first_name = "Sandra", last_name="Kyalo",location="Kwale",votes=0)
     gubernatorial(first_name = "Nancy", last_name="Kamulu",location="Nairobi",votes=0,)
     gubernatorial(first_name = "Mark", last_name="Owiti",location="Mombasa",votes=0,)
     gubernatorial(first_name = "Amina", last_name="Kitui",location="Nyeri",votes=0,)
     gubernatorial(first_name = "Luca", last_name="Kitui",location="Kwale",votes=0,)
     gubernatorial(first_name = "Felista", last_name="Toms",location="Kisumu",votes=0,)
]

def gubernatorials_votes(gubernatorial):
    for gubernatorial in gubernatorials:
        db.session.add(gubernatorial)
        db.session.commit()
        print("\n", voter, "\n")

add_governors(gubernatorial)

Senatorials = [
     senatorial(first_name = "Alice", last_name="Kipkoech",location="Nyeri",votes=0),
     senatorial(first_name = "Jane", last_name="Oyando",location="Nairobi",votes=0),
     senatorial(first_name = "Michael", last_name="Mwaura",location="Kisumu",votes=0), 
     senatorial(first_name = "Andrew", last_name="Juma",location="Mombasa",votes=0)
     senatorial(first_name = "Sandra", last_name="Mwikali",location="Kwale",votes=0)
     senatorial(first_name = "Lisa", last_name="Ali",location="Nairobi",votes=0,)
     senatorial(first_name = "Kipkurui", last_name="Mercy",location="Mombasa",votes=0,)
     senatorial(first_name = "Sandy", last_name="Maalim",location="Nyeri",votes=0,)
     senatorial(first_name = "Abdi", last_name="Hussein",location="Kwale",votes=0,)
     senatorial(first_name = "Erick", last_name="Boaz",location="Kisumu",votes=0,)
]

def senetarial_votes(senetorial):
    for senetorial in senetorials:
        db.session.add(senetorial)
        db.session.commit()
        print("\n", voter, "\n")

add_senetors(senetarial)