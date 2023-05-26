from scipy import constants
from math import sqrt

def time_dilation(t: float, r: float, M: float) -> float:
    """
    ∆t' = ∆t • sqrt(1 - (2MG / r • c^2))
    """
    G = constants.G
    c = constants.c
    t_prime = t * sqrt(1 - ((2 * M * G) / (r * c**2)))
    return t_prime

def main():
    t = 86400
    r = 0.387 * constants.au
    M = 4.385 * 10**30 * constants.lb
    print(time_dilation(t, r, M))

if __name__ == "__main__":
    main()
