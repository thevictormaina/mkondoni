import unittest
from app.models import *
from app import db

class TestSenator(unittest.TestCase):
    """
    Class for testing senator properties and methods. Inherits from unittest.TestCase
    """
    def setUp(self):
        """
        Runs before each test
        """
        db.create_all()
        self.senator = Senator(first_name="John", last_name="Doe", location="Nairobi", votes=0)

        db.session.add(self.senator)
        db.session.commit()

    def tearDown(self):
        """
        Runs after each test
        """
        db.session.commit()
        db.drop_all()

    def test_senator_instance(self):
        """
        Test cases to check if senator instance is created and commited correctly
        """

        senator = Senator.query.first()

        self.assertEqual(senator.id, 1)
        self.assertEqual(senator.first_name, "John")
        self.assertEqual(senator.last_name, "Doe")
        self.assertEqual(senator.location, "Nairobi")
        self.assertEqual(senator.votes, 0)

    def test_add_vote(self):
        """
        Test case to check if senator.voted is changed to true
        """

        senator = Senator.query.first()
        self.assertEqual(senator.votes, 0)

        senator.add_vote()
        self.assertEqual(senator.votes, 1)