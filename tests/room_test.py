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

        self.open_mic_01.check_in('Robin')

        self.open_mic_02.check_in('John')
        self.open_mic_02.check_in('Paul')
        self.open_mic_02.check_in('George')
        self.open_mic_02.check_in('Ringo')
        self.open_mic_02.check_out('John')

        self.open_mic_02.check_in('Bubbles')
        self.open_mic_02.check_in('Micheal Jackson')


    def test_room_has_name(self):
        self.assertEqual('Wembley', self.wembley.name)

    def test_room_has_capacity(self):
        self.assertEqual(21, self.glasto.capacity)

    def test_no_of_guests(self):
        no_of_guests = self.open_mic_01.guests
        self.assertEqual(1, len(no_of_guests))
    
    def test_check_in(self):
        self.open_mic_01.check_in('Bob')
        no_of_guests = self.open_mic_01.guests
        self.assertEqual(2, len(no_of_guests))

    def add_song(self):
        self.assertEqual('She Drives Me Crazy', self.open_mic_01.add_song)

    def test_check_out(self):
        guest_left = [] 
        
        for guest in self.open_mic_02.guests:
            if guest == 'John':
                guest_left.append(guest)

        self.assertEqual(0, len(guest_left))

    def test_too_many_guests(self):
        guests_in_room = len(self.open_mic_02.guests)
        capacity = self.open_mic_02.capacity
        self.assertLessEqual(capacity, guests_in_room)