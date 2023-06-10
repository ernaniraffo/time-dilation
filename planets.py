from scipy import constants

solar_mass = 2 * 10**30


class Planet():
    def __init__(self, name: str, r: int | float):
        self.name = name
        self.r = r * constants.au

    def __str__(self):
        return "name: " + self.name + "\tr: " + str(self.r / constants.au) + " AU"


class MassiveObject():
    def __init__(self, name: str, mass: int | float):
        self.name = name
        self.mass = mass * solar_mass

    def __str__(self) -> str:
        return "name: " + self.name + "\tsolar mass: " + str(self.mass / solar_mass)


class System():
    def __init__(self) -> None:
        self.planets = {}
        self.massive_object = None

    def add_planet(self, planet: Planet):
        self.planets[planet.name] = planet

    def add_massive_object(self, object: MassiveObject):
        self.massive_object = object

    def __str__(self) -> str:
        s = "Massive Object:\n\t" + str(self.massive_object) + "\n"
        s += "Planets:\n"
        for i, p in enumerate(self.planets.values()):
            s += "\t" + str(p)
            if i + 1 < len(self.planets):
                s += "\n"
        return s
