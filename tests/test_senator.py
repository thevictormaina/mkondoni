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