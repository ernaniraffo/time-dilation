from planets import Planet, MassiveObject
from time_dilation import time_dilation
from scipy import constants


def main():
    earth = Planet("Earth", 1)
    sun = MassiveObject("Sun", 1)

    gargantua = MassiveObject("Gargantua", 100000000)

    # figure out distance between Miller and Gargantua
    r = (2 * constants.G * gargantua.mass / constants.c**2)
    event_horizon = r
    miller_time = 0
    while miller_time < constants.hour:
        miller = Planet("Miller", r / constants.au)
        miller_time = time_dilation(constants.year * 7, miller, gargantua)
        r += 1

    print(earth)
    print(sun)
    print(gargantua)
    print("7 years on Earth is", miller_time / constants.hour, "hours on Miller's planet")


if __name__ == "__main__":
    main()
