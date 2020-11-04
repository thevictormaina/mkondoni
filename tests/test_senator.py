import unittest
from app.models import Senator

class TestSenator(unittest.TestCase):
    """
    Class for testing Senator properties and methods. Inherits from unittest.TestCase
    """
    def setUp(self):
        """
        Runs before each test
        """
        db.create_all()

        self.senator = Senator(id=" ", first_name=" ", last_name=" ", location=" ", votes=" ")

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
        db.session.add(self.senator)
        db.session.commit()

        senator = Senator.query.filter_by(first_name = " ").first()

        self.assertEqual(senator.id,1)
        self.assertEqual(senator.first_name, " ")
        self.assertEqual(senator.last_name, " ")
        self.assertEqual(senator.location, " ")
        self.assertEqual(senator.votes,0)
   