class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_bday = Song(["happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_a_parade = Song(["They rally around the family",
                          "with pockets full nof shells"])

happy_bday.sing_me_a_song()

bulls_on_a_parade.sing_me_a_song()