import unittest
from app import db
from app.models import Governor

class TestGovernor(unittest.TestCase):
    """
    Class for testing Governor properties and methods. Inherits from unittest.TestCase
    """
    def setUp(self):
        """
        Runs before each test
        """
        db.create_all()

        self.governor = Governor( first_name=" ", last_name=" ", location=" ", votes=0)

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
        db.session.add(self.governor)
        db.session.commit()

        governor = Governor.query.filter_by(first_name = " ").first()

        self.assertEqual(governor.id,1)
        self.assertEqual(governor.first_name, " ")
        self.assertEqual(governor.last_name, " ")
        self.assertEqual(governor.location, " ")
        self.assertEqual(governor.votes,0)
   