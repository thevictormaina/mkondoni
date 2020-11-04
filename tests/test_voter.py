import unittest
from app.models import *
from app import db

class TestVoter(unittest.TestCase):
    """
    Class for testing Voter properties and methods. Inherits from unittest.TestCase
    """
    def setUp(self):
        """
        Runs before each test
        """
        db.create_all()
        self.voter = Voter(national_id="12345678", first_name="John", last_name="Doe", location="Nairobi")

        db.session.add(self.voter)
        db.session.commit()

    def tearDown(self):
        """
        Runs after each test
        """
        db.session.commit()
        db.drop_all()

    def test_voter_instance(self):
        """
        Test cases to check if voter instance is created and commited correctly
        """

        voter = Voter.query.first()

        self.assertEqual(voter.id, 1)
        self.assertEqual(voter.national_id, "12345678")
        self.assertEqual(voter.first_name, "John")
        self.assertEqual(voter.last_name, "Doe")
        self.assertEqual(voter.location, "Nairobi")
        self.assertEqual(voter.voted, False)

    def test_has_voted(self):
        """
        Test case to check if Voter.voted is changed to true
        """

        voter = Voter.query.first()
        self.assertEqual(voter.voted, False)

        voter.has_voted()
        self.assertEqual(voter.voted, True)