from scipy import constants

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
