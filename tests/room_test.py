import unittest
from src.room import Room
from src.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.wembley = Room('Wembley', 9)
        self.glasto = Room('Glastonbury', 21)
        self.open_mic_01 = Room('Open mic Monday', 4)
        self.open_mic_02 = Room('Open mic Tuesday', 5)
        self.open_mic_03 = Room('Open mic Wednesday', 6)

    def test_room_has_name(self):
        self.assertEqual('Wembley', self.wembley.name)

    def test_room_has_capacity(self):
        self.assertEqual(21, self.glasto.capacity)

    def add_song(self):
        self.assertEqual('She Drives Me Crazy', self.open_mic_01.add_song)

    # def test_check_in(self):
    #   self.assertEqual(4, self.open_mic_01.check_in)

    # def test_check_out(self):
    #     self.assertEqual(4, self.open_mic_01.check_out)
