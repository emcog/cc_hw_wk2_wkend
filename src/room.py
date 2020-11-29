class Room:

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.playlist = []


    def add_song(self, song):
        # add to playlist using append
        self.playlist.append(song)


        