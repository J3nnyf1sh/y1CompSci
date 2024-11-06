class Song:
    
    def __init__(self, name, artist, seconds):
        self.name = name
        self.artist = artist
        self.seconds = seconds

    def getName(self):
        return self.name
    
    def getArtist(self):
        return self.artist
    
    def getSeconds(self):
        return self.seconds

class Playlist:
    
    def __init__(self):
        self.playlist = []
    
    def addSong(self, song):
        self.playlist.append(song)
    
    def removeSong(self, song):
        self.playlist.remove(song)
    
    def __str__(self):
        Output = ""
        for song in self.playlist:
            Output += f"{song.getName()} by {song.getArtist()}, {song.getSeconds()} seconds\n"
        return Output

def test():
    cut = Song("Cut - 1990 Demo", "The Cure", "213")
    grace = Song("Grace", "Jeff Buckley", "322")
    itsOhSoQuiet = Song("It's Oh So Quiet", "Bjork", "218")

    myPlaylist = Playlist()
    myPlaylist.addSong(cut)
    myPlaylist.addSong(grace)
    myPlaylist.addSong(itsOhSoQuiet)
    print(myPlaylist)
    

test()



        