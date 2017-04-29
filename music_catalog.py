import linked_list.py, array_list.py

# a SongCatalog is a data type of SongCatalog(title, artist, album)
class SongCatalog:
    def __init__(self, songList, sortType):
        self.songList = songList # a List
        self.sortType = sortType # an integer
        self.sortedSongs = songList # a List (not yet sorted at time of object construction)
    def __eq__(self, other):
        return (type(other) == Song
            and self.songList == other.songList
            and self.sortType == other.sortType
            and self.sortedSongs == other.sortedSongs)
    def __repr__(self):
        return "Song({!r}, {!r}, {!r})".format(self.title, self.artist, self.album)

# None -> None
# displays a menu to carry out various actions involving a song catalog
def song_catalog():
    print("Song Catalog \
        \n   1) Print Catalog \
        \n   2) Song Information \
        \n   3) Sort \
        \n   4) Add Songs \
        \n   0) Quit \
        Enter selection: ")
    userIn = input()
    if(userIn == 1):
        print_songs()

# List value -> str
# returns a string of songs from the given list that is sorted by the given input value
def print_songs(l, sortType):
