import math
import sys
import random

class Ułamek:
    #Wersja2__slots__ = ('licznik', 'mianownik')
    def __init__(self, licznik, mianownik):
        self.licznik = licznik
        self.mianownik = mianownik
        assert mianownik != 0
        self.skróć()

    def skróć(self):
        gcd = math.gcd(self.licznik, self.mianownik)
        self.licznik = int(self.licznik / gcd)
        self.mianownik = int(self.mianownik / gcd)
        if self.licznik / self.mianownik > 0:
            self.licznik = abs(self.licznik)
            self.mianownik = abs(self.mianownik)
        else:
            self.licznik = -abs(self.licznik)
            self.mianownik = abs(self.mianownik)

    def __str__(self):
        if self.licznik == 0 or self.mianownik == 1:
            return str(self.licznik)
        return str(self.licznik) + "/" + str(self.mianownik)

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        return self.licznik * other.mianownik < other.licznik * self.mianownik

    def __le__(self, other):
        return self.licznik * other.mianownik <= other.licznik * self.mianownik

    def __eq__(self, other):
        return self.licznik * other.mianownik == other.licznik * self.mianownik

    def __ne__(self, other):
        return self.licznik * other.mianownik != other.licznik * self.mianownik

    def __gt__(self, other):
        return self.licznik * other.mianownik > other.licznik * self.mianownik

    def __ge__(self, other):
        return self.licznik * other.mianownik >= other.licznik * self.mianownik

    def __add__(self, other):
        return Ułamek((self.licznik * other.mianownik + self.mianownik * other.licznik), self.mianownik * other.mianownik)

    def __sub__(self, other):
        return Ułamek((self.licznik * other.mianownik - self.mianownik * other.licznik), self.mianownik * other.mianownik)

    def __mul__(self, other):
        return Ułamek(self.licznik * other.licznik, self.mianownik * other.mianownik)

    def __truediv__(self, other):
        return Ułamek(self.licznik * other.mianownik, self.mianownik * other.licznik)

if __name__ == '__main__':
    # u1 = Ułamek(5, 3)
    # u2 = Ułamek(-2,1)
    # nap = str(u1)
    # print(f"{u1} {nap=}")
    # print(f"{u1=}")
    # print(f"{u2=}")
    # print(u1 + u2)
    # print(u1 - u2)
    # print(u1 + u2 + Ułamek(1, 3))
    # print(u1 * u2)
    # print(u1 / u2)
    # print(Ułamek(6, 0))
    # print(u1 < u2)
    # print(Ułamek(2, 0))
    n = int(sys.argv[1])
    k = int(sys.argv[2])
    ułamki = [Ułamek(random.randrange(1000000), i + 1) for i in range(n)]
    for i in range(k):
        ułamki[i % n] += ułamki[(i + 1) % n]




