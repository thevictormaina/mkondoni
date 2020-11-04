import unittest
from app.models import *
from app import db

class TestPresident(unittest.TestCase):
    """
    Class for testing President properties and methods. Inherits from unittest.TestCase
    """
    def setUp(self):
        """
        Runs before each test
        """
        db.create_all()
        self.president = President(first_name="John", last_name="Doe", location="Nairobi", votes=0)

        db.session.add(self.president)
        db.session.commit()

    def tearDown(self):
        """
        Runs after each test
        """
        db.session.commit()
        db.drop_all()

    def test_president_instance(self):
        """
        Test cases to check if president instance is created and commited correctly
        """

        president = President.query.first()

        self.assertEqual(president.id, 1)
        self.assertEqual(president.first_name, "John")
        self.assertEqual(president.last_name, "Doe")
        self.assertEqual(president.location, "Nairobi")
        self.assertEqual(president.votes, 0)

    def test_add_vote(self):
        """
        Test case to check if president.voted is changed to true
        """

        president = President.query.first()
        self.assertEqual(president.votes, 0)

        president.add_vote()
        self.assertEqual(president.votes, 1)