import unittest
from app.models import Voter

class TestVoter(unittest.TestCase):
    """
    Class for testing Voter properties and methods. Inherits from unittest.TestCase
    """
    def setUp(self):
        """
        Runs before each test
        """
        db.create_all()

        self.voter = Voter(id=" ", national_id=" ", passport=" ", first_name=" ", last_name=" ", location=" ")

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
        db.session.add(self.governor)
        db.session.commit()

        voter = Voter.query.filter_by(first_name = " ").first()

        self.assertEqual(voter.id,1)
        self.assertEqual(voter.national_id)
        self.assertEqual(voter.passport)
        self.assertEqual(voter.first_name, " ")
        self.assertEqual(voter.last_name, " ")
        self.assertEqual(voter.location, " ")
        self.assertEqual(voter.voted)
       