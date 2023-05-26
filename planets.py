from scipy import constants

distance_to_sun = {"Earth": 1, "Mercury": 0.39, "Venus": 0.72, "Mars": 1.52, "Jupiter": 5.2, "Saturn": 9.54, "Uranus": 19.2, "Neptune": 30.06}

solar_mass = 2 * 10**30


class Planet():
    def __init__(self, name: str, r: int | float):
        self.name = name
        self.r = r

    def __str__(self):
        return "name: " + self.name + ", r: " + str(self.r / constants.au) + " AU"


class MassiveObject():
    def __init__(self, name: str, mass: int | float):
        self.name = name
        self.mass = mass

    def __str__(self) -> str:
        return "name: " + self.name + ", solar mass: " + str(self.mass / solar_mass)
