import unittest
from src.room import Room

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.wembley = Room('Wembley', 9)
        self.glasto = Room('Glastonbury', 21)

    def test_room_has_name(self):
        self.assertEqual('Wembley', self.wembley.name)

    def test_room_has_capacity(self):
        self.assertEqual(21, self.glasto.capacity)

    # def test_check_in(self):
        

    # def test_check_out(self):



# test room has capacity
# test check in method
# test check out method
# test add song method