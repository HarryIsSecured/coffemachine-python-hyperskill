class Painting:
    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year
        print(f'"{self.title}" by {self.artist} ({self.year}) hangs in the Louvre.')


l_title = input()
l_artist = input()
l_year = input()

l_painting = Painting(l_title, l_artist, l_year)
