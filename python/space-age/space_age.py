EARTH_YEAR = 31557600
ORBITAL_PERIODS = {
    'earth': 1,
    'mercury': 0.2408467,
    'venus': 0.61519726,
    'mars': 1.8808158,
    'jupiter': 11.862615,
    'saturn': 29.447498,
    'uranus': 84.016846,
    'neptune': 164.79132
}


class SpaceAge:
    seconds = 0

    def __init__(self, seconds):
        self.seconds = seconds

    def on_planet(self, planet):
        def fn():
            return round(self.seconds/(ORBITAL_PERIODS[planet]*EARTH_YEAR), 2)
        return fn

    def __getattr__(self, name):
        planet = name[3:]
        if planet in ORBITAL_PERIODS:
            return self.on_planet(planet)
        raise AttributeError
