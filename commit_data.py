from app.models import Voter, President, Senator, Governor
from app import db

voters = [Voter(national_id="12345678", first_name="John", last_name="Joe"),
          Voter(national_id="23456789",
                first_name="Jane", last_name="Joe"),
          Voter(national_id="45656764",
                first_name="Michael", last_name="Joe"),
          Voter(national_id="34567891", first_name="Andrew", last_name="Does")]


presidents = [
    President(first_name="John", last_name="Joe", location="Kenya", votes=0),
    President(first_name="Jane", last_name="Joe", location="Kenya", votes=0),
    President(first_name="Uhuru", last_name="Kenyatta",
              location="Kenya", votes=0),
    President(first_name="Raila", last_name="Odinga",
              location="Kenya", votes=0),
    President(first_name="William", last_name="Ruto",
              location="Kenya", votes=0),
    President(first_name="Kalonzo", last_name="Musyoka",
              location="Kenya", votes=0,)
]

governors = [
    Governor(first_name="Lee", last_name="Kinyanjui",
             location="Nyeri", votes=0),
    Governor(first_name="Samuel", last_name="Kamau",
             location="Nairobi", votes=0),
    Governor(first_name="Agnes", last_name="Joe", location="Kisumu", votes=0),
    Governor(first_name="Andrew", last_name="Onyango",
             location="Mombasa", votes=0),
    Governor(first_name="Sandra", last_name="Kyalo",
             location="Kwale", votes=0),
    Governor(first_name="Nancy", last_name="Kamulu",
             location="Nairobi", votes=0,),
    Governor(first_name="Mark", last_name="Owiti",
             location="Mombasa", votes=0,),
    Governor(first_name="Amina", last_name="Kitui",
             location="Nyeri", votes=0,),
    Governor(first_name="Luca", last_name="Kitui", location="Kwale", votes=0,),
    Governor(first_name="Felista", last_name="Toms",
             location="Kisumu", votes=0,)
]

senators = [
    Senator(first_name="Alice", last_name="Kipkoech",
            location="Nyeri", votes=0),
    Senator(first_name="Jane", last_name="Oyando",
            location="Nairobi", votes=0),
    Senator(first_name="Michael", last_name="Mwaura",
            location="Kisumu", votes=0),
    Senator(first_name="Andrew", last_name="Juma",
            location="Mombasa", votes=0),
    Senator(first_name="Sandra", last_name="Mwikali",
            location="Kwale", votes=0),
    Senator(first_name="Lisa", last_name="Ali", location="Nairobi", votes=0,),
    Senator(first_name="Kipkurui", last_name="Mercy",
            location="Mombasa", votes=0,),
    Senator(first_name="Sandy", last_name="Maalim",
            location="Nyeri", votes=0,),
    Senator(first_name="Abdi", last_name="Hussein",
            location="Kwale", votes=0,),
    Senator(first_name="Erick", last_name="Boaz", location="Kisumu", votes=0,)
]


def commit_data():
    data = [voters, governors, presidents, senators]
    for list in data:
        for person in list:
            db.session.add(person)
    db.session.commit()
