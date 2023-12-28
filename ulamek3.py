import pytest
import math
import os
from unittest.mock import mock_open, patch


class Ułamek:
    # Wersja2__slots__ = ('licznik', 'mianownik')
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
        return Ułamek((self.licznik * other.mianownik + self.mianownik * other.licznik),
                      self.mianownik * other.mianownik)

    def __sub__(self, other):
        return Ułamek((self.licznik * other.mianownik - self.mianownik * other.licznik),
                      self.mianownik * other.mianownik)

    def __mul__(self, other):
        return Ułamek(self.licznik * other.licznik, self.mianownik * other.mianownik)

    def __truediv__(self, other):
        return Ułamek(self.licznik * other.mianownik, self.mianownik * other.licznik)

# Zapisywanie/odczytywanie z pliku.
    def zapiszDoPliku(self, nazwa):
        os.path.join(os.getcwd(), nazwa)
        with open(nazwa, 'w') as plik:
            plik.write(str(self))

    def odczytajZPliku(self, nazwa):
        nazwa = nazwa + '.txt'
        os.path.join(os.getcwd(), nazwa)
        with open(nazwa, 'r') as plik:
            linie = plik.read()
            linie = linie.split('/')
            self.licznik = int(linie[0])
            self.mianownik = int(linie[1])


# Testy parametryzowane, fixture

@pytest.fixture
def arg1():
    return Ułamek(3, 7)


@pytest.mark.parametrize("l1, m1, l2, m2", [[5, 3, 44, 21], [1, 2, 13, 14]])
def test_dodaj(l1, m1, l2, m2, arg1):
    assert Ułamek(l1, m1) + arg1 == Ułamek(l2, m2)


@pytest.mark.parametrize("l1, m1, l2, m2", [[5, 3, 26, 21], [1, 2, 1, 14]])
def test_odejmij(l1, m1, l2, m2, arg1):
    assert Ułamek(l1, m1) - arg1 == Ułamek(l2, m2)


@pytest.mark.parametrize("l1, m1, l2, m2", [[5, 3, 5, 7], [1, 2, 3, 14]])
def test_mnożenie(l1, m1, l2, m2, arg1):
    assert Ułamek(l1, m1) * arg1 == Ułamek(l2, m2)


@pytest.mark.parametrize("l1, m1, l2, m2", [[5, 3, 35, 9], [1, 2, 7, 6]])
def test_dzielenie(l1, m1, l2, m2, arg1):
    assert Ułamek(l1, m1) / arg1 == Ułamek(l2, m2)


@pytest.mark.parametrize("l1, m1, wynik", [[5, 3, False], [1, 4, True]])
def test_mniejsze(l1, m1, arg1, wynik):
    assert (Ułamek(l1, m1) < arg1) == wynik


@pytest.mark.parametrize("l1, m1, wynik", [[5, 3, True], [1, 4, False]])
def test_wieksze(l1, m1, arg1, wynik):
    assert (Ułamek(l1, m1) > arg1) == wynik


@pytest.mark.parametrize("l1, m1, s", [[10, 6, '5/3'], [10, 2, '5'], [0, 10, '0']])
def test_napis(l1, m1, s):
    assert str(Ułamek(l1, m1)) == s

# Test odczytywania/zapisywania do pliku z użyciem mock.


def test_read_file():
    mock_data = '3/7'
    m = mock_open(read_data=mock_data)
    u1 = Ułamek(1, 2)
    with pytest.MonkeyPatch.context() as mpatch:
        mpatch.setattr("builtins.open", m)
        u1.odczytajZPliku('dummy')
    m.assert_called_once_with("dummy.txt", 'r')
    assert str(u1) == mock_data


def test_file_writer():
    fake_file_path = "dummy/file/path"
    content = "3/7"
    u1 = Ułamek(3, 7)
    with patch("builtins.open", mock_open()) as mocked_file:
        u1.zapiszDoPliku(fake_file_path)
        mocked_file.assert_called_once_with(fake_file_path, 'w')
        mocked_file().write.assert_called_once_with(content)
