class Room:

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.playlist = []
        self.guests = []


    def add_song(self, song):
        # add to playlist using append
        self.playlist.append(song)


    def check_in(self, guest):
        if len(self.guests) < self.capacity:
            self.guests.append(guest)
        else:
            return 'Sorry its one in one out'


    def check_out(self, guest):
        self.guests.remove(guest)