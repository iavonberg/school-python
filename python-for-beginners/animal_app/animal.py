class Animal:
    planet = 'Earth'

    def __init__(self):
        self.legs = None
        self.wings = None
        self.sounds = None
        self.coordinates = None

    def update_coordinates(self, lat, long):
        self.coordinates = (lat, long)

    def make_sound(self):
        return self.sounds
    
    @classmethod
    def get_planet(cls):
        return cls.planet
