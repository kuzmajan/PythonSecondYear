def sumaListy(lista):
    wynik = 0
    for el in lista:
        if isinstance(el, int):
            wynik += el
        elif isinstance(el, list):
            wynik += sumaListy(el)
    return wynik


if __name__ == '__main__':
    dane = [1, 7, "to", False, [1, [], [12, [1]]], 10]
    print(sumaListy(dane))
