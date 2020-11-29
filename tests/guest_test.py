import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest_01 = Guest('Robin', 30)

    def test_guest_has_name(self):
        self.assertEqual('Robin', self.guest_01.name)

    def test_guest_has_cash(self):
        self.assertLessEqual(0, self.guest_01.cash)