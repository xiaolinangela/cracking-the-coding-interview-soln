from collections import defaultdict

class Song:
    def __init__(self,title,artist,album):
        self.title = title
        self.artist = artist
        self.album = album
        self.data = data
        self.play_count = 0
    
    def play(self):
        self.is_playing = True
        self.play_count += 1

    def play(self):
        self.is_playing = False

class Jukebox:
    def __init__(self,songs):
        self.songs = {}
        for song in songs:
            self.songs[song.title] = song
        self.playing = None
        self.playlist = defaultdict(list)
        self.queue = deque()

    def play_song(self,title):
        if self.playing:
            self.stop_playing()
        self.playing = self.songs[title]
        self.playing.play()
    
    def stop_song(self):
        if self.playing:
            self.playing.stop()
    
    def make_playlist(self,pl_name,song):
        self.playlist[pl_name] = song
    
    def add_to_playlist(self,pl_name,song):
        self.make_playlist[pl_name].append(song)
    




    


        

