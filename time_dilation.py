from scipy import constants
from math import sqrt
from planets import Planet, MassiveObject


def time_dilation(t: float, planet: Planet, massive_body: MassiveObject) -> float:
    """
    ∆t' = ∆t • sqrt(1 - (2MG / r • c^2))
    """
    G = constants.G
    c = constants.c
    t_prime = t * sqrt(1 - ((2 * massive_body.mass * G) / (planet.r * c**2)))
    return t_prime


def main():
    earth = Planet("Earth", 1 * constants.au)
    sun = MassiveObject("Sun", 4.385 * 10**30 * constants.lb)
    print(time_dilation(86400, earth, sun))


if __name__ == "__main__":
    main()
