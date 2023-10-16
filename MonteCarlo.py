import random
import math


def dlugosc(x, y):
    return math.sqrt(x**2 + y**2)


if __name__ == '__main__':
    licznik = 0
    n = 100000
    for i in range(n):
        a = random.random() * 2 - 1
        b = random.random() * 2 - 1
        if dlugosc(a, b) <= 1:
            licznik += 1
    print(4 * licznik / n)
