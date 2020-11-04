import unittest
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

        self.governor = Governor(id=" ", first_name=" ", last_name=" ", location=" ", votes=" ")