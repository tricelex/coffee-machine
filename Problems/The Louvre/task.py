class Painting:
    museum = "Louvre"

    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year

    def show(self):
        print(f'"{self.title}" by {self.artist} ({self.year}) hangs in the Louvre.')


# my = Painting(input(), input(), input())
# my.show()

rad = 3

print(4 * (3 + 5))
