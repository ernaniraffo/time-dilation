from planets import Planet, MassiveObject
from time_dilation import time_dilation
from scipy import constants


def main():
    gargantua = MassiveObject("Gargantua", 100000000)

    # figure out distance between Miller and Gargantua
    r = (2 * constants.G * gargantua.mass / constants.c**2)
    event_horizon = r
    print("Gargantua's event horizon:", event_horizon / constants.au, "AU")
    miller_time = 0
    while miller_time < constants.hour:
        miller = Planet("Miller", r / constants.au)
        miller_time = time_dilation(constants.year * 7, miller, gargantua)
        r += 1

    print(gargantua)
    print(miller)
    print("Miller is", miller.r - event_horizon, "meters away from Gargantua")
    print("7 years on Earth is", miller_time / constants.hour, "hours on Miller's planet")


if __name__ == "__main__":
    main()
