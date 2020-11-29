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
        # guest checks in to room
        self.guests.append(guest)


    def check_out(self, guest):
        # guest checks in to room
        self.guests.remove(guest)