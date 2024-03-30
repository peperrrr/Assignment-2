class Exhibition:
    def __init__(self, name, start_date, end_date, location):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.location = location
        self.artworks = []
#Creating a method to add the artworks to a certain exhibition easier
    def add_artwork(self, artwork):
        self.artworks.append(artwork)