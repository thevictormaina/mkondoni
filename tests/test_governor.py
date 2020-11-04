import unittest
from app.models import *
from app import db

class TestGovernor(unittest.TestCase):
    """
    Class for testing governor properties and methods. Inherits from unittest.TestCase
    """
    def setUp(self):
        """
        Runs before each test
        """
        db.create_all()
        self.governor = Governor(first_name="John", last_name="Doe", location="Nairobi", votes=0)

        db.session.add(self.governor)
        db.session.commit()

    def tearDown(self):
        """
        Runs after each test
        """
        db.session.commit()
        db.drop_all()

    def test_governor_instance(self):
        """
        Test cases to check if governor instance is created and commited correctly
        """

        governor = Governor.query.first()

        self.assertEqual(governor.id, 1)
        self.assertEqual(governor.first_name, "John")
        self.assertEqual(governor.last_name, "Doe")
        self.assertEqual(governor.location, "Nairobi")
        self.assertEqual(governor.votes, 0)

    def test_add_vote(self):
        """
        Test case to check if governor.voted is changed to true
        """

        governor = Governor.query.first()
        self.assertEqual(governor.votes, 0)

        governor.add_vote()
        self.assertEqual(governor.votes, 1)