import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest_01 = Guest('Robin')

    # def test_guest_has_name(self):
    #     self.assertEqual('Robin', self.guest_01.name)