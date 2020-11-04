import unittest
from app.models import President

class TestPresident(unittest.TestCase):
    """
    Class for testing President properties and methods. Inherits from unittest.TestCase
    """
    def setUp(self):
        """
        Runs before each test
        """
        db.create_all()

        self.president = President(id=" ", first_name=" ", last_name=" ", location=" ", votes=" ")

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
        db.session.add(self.president)
        db.session.commit()

        president = President.query.filter_by(first_name = " ").first()

        self.assertEqual(president.id,1)
        self.assertEqual(president.first_name, " ")
        self.assertEqual(president.last_name, " ")
        self.assertEqual(president.location, " ")
        self.assertEqual(president.votes,0)
   