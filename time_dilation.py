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
    # earth = Planet("Earth", 1 * constants.au)
    sun = MassiveObject("Sun", 2 * 10**30)

    gargantua = MassiveObject("Gargantua", sun.mass * 100000000)
    print("Mass of %s = %d kg" % (sun.name, sun.mass))
    print("Mass of %s = %d kg" % (gargantua.name, gargantua.mass))

    # figure out distance between Miller and Gargantua
    r = (2 * constants.G * gargantua.mass / constants.c**2)
    miller_time = 0
    while miller_time < constants.hour:
        miller = Planet("Miller", r)
        miller_time = time_dilation(constants.year * 7, miller, gargantua)
        r += 1

    print(miller)
    print("7 years on Earth is", miller_time / 60 / 60, "hours on Miller's planet")


if __name__ == "__main__":
    main()
