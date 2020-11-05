from app.models import Voter, President, Senator, Governor
from app import db

voters = [Voter(national_id="12345678", first_name="John", last_name="Joe"),
          Voter(national_id="23456789",
                first_name="Jane", last_name="Joe"),
          Voter(national_id="45656764",
                first_name="Michael", last_name="Joe"),
          Voter(national_id="34567891", first_name="Andrew", last_name="Does")]


presidents = [
    President(first_name="Uhuru", last_name="Kenyatta",
              location="Kenya", votes=0,party="Jubilee"),
    President(first_name="Raila", last_name="Odinga",
              location="Kenya", votes=0, party="ODM"),
    
]


deputies = [
    Deputy(first_name="William", last_name="Ruto",
              location="Kenya",president_id=President.query.filter_by(first_name="Uhuru").first().id),
    Deputy(first_name="Kalonzo", last_name="Musyoka",
              location="Kenya",president_id=President.query.filter_by(first_name="Raila").first().id)
]

governors = [
    Governor(first_name="Lee", last_name="Kinyanjui",
             location="Nakuru", votes=0, party="Jubilee"),
    Governor(first_name="Mike", last_name="Mbuvi",
             location="Nairobi", votes=0, party="jubilee"),
    Governor(first_name="Josphat", last_name="Nanok", location="Turkana", votes=0, party="ODM")
   
]

senators = [
    Senator(first_name="Margaret", last_name="Kamar",
            location="Uasin-Gishu", votes=0,party="ODM"),
    Senator(first_name="Kipchumba", last_name="Murkomen",
            location="Elgeyo-Marakwet", votes=0,party="Jubilee"),
    Senator(first_name="Samuel", last_name="Poghisio",
            location="West-Pokot", votes=0,party="ODM")

]

parties =[
        Party(party_name="ODM",party_logo_path=" "),
        Party(party_name="Jubilee",party_logo_path=" ")
]


def commit_data():
    data = [voters, governors, presidents,deputies, senators, parties]
    for list in data:
        for person in list:
            db.session.add(person)
    db.session.commit()
