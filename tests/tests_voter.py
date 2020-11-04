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