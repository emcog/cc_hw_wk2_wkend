import unittest
from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song_01 = Song('Micheal Jackson', 'Smooth Criminal')

    def test_song_has_name(self):
        self.assertEqual('Smooth Criminal', self.song_01.name)

    def test_song_has_artist(self):
        self.assertEqual('Micheal Jackson', self.song_01.artist)

