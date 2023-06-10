from scipy import constants
from math import sqrt
from planets import Planet, MassiveObject, System
import argparse


def time_dilation(t: float, planet: Planet, massive_body: MassiveObject) -> float:
    """
    ∆t' = ∆t • sqrt(1 - (2MG / r • c^2))
    """
    G = constants.G
    c = constants.c
    t_prime = t * sqrt(1 - ((2 * massive_body.mass * G) / (planet.r * c**2)))
    return t_prime


def get_system(file: str) -> System:
    system = System()
    with open(file, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip("\n")
            name, num = line.split()
            if not system.massive_object:
                system.add_massive_object(MassiveObject(name, float(num)))
            else:
                system.add_planet(Planet(name, float(num)))
    return system


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", "-f", type=str)
    args = parser.parse_args()

    star_system = get_system(args.file)
    print(star_system)

    while True:
        try:
            print("\nEnter two planets to calculate time dilation difference:")
            p1 = None
            while p1 not in star_system.planets:
                p1 = input("Planet 1: ")
            p2 = None
            while  p2 not in star_system.planets:
                p2 = input("Planet 2: ")
            time = float(input("Enter time observed in seconds: "))
            print(f"Time on {p1}: {(t1 := time_dilation(time, star_system.planets[p1], star_system.massive_object))}")
            print(f"Time on {p2}: {(t2 := time_dilation(time, star_system.planets[p2], star_system.massive_object))}")
            print(f"Time difference: {(t2 - t1 if t2 > t1 else t1 - t2)}")
            print("\nPress ctrl-c to exit")
        except KeyboardInterrupt:
            exit(0)

if __name__ == "__main__":
    main()
