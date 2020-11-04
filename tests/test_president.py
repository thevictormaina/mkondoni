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