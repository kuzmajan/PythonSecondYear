from functools import *
from itertools import *
import operator


def mult(*args):
    return reduce(lambda x, y: x * y, args, 1)


def potęga(*args):
    return reduce(lambda x, y: pow(x, y), args, 1)


def plateau(arg):
    if len(arg) == 0:
        print(0)
    else:
        print(max(list(map(lambda p: len(list(p[1])), groupby(arg)))))



def funkcja(t1, t2):
    return (t1, t2) + (pow(t1, t2),)
def ex2(iterator):
    return list(starmap(funkcja, iterator))

def z1Lambdy(iterator):
    i1, i2 = tee(iterator)
    return map(lambda tuple: (tuple[0], tuple[1], next(starmap(pow, i1))), i2)

def odpluskw(func):
    mem = {}
    def new_func(*args, **kwargs):
        print(f'function called with args: {args}, kwargs: {kwargs}')
        # if args[0] not in mem:
        #     print(f'function called with args: {args}, kwargs: {kwargs}')
        #     mem[args[0]] = func(*args, **kwargs)
        mem[args[0]] = func(*args, **kwargs)
        return mem[args[0]]

    return new_func


@odpluskw
def fibPierwszy(*args):
    n = args[0]
    return fibPierwszy(n - 1) + fibPierwszy(n - 2) if n >= 2 else n


def obejdź(drzewo, preorder = False, inorder = False, postorder = False):
    licznik = 0
    if preorder == True : licznik += 1
    if inorder == True : licznik += 1
    if postorder == True : licznik += 1
    if licznik != 1:
        return None
    else:
        if inorder == True:
            if drzewo[0] != None:
                yield from obejdź(drzewo[0], inorder = True)
            yield drzewo[1]
            if drzewo[2] != None:
                yield from obejdź(drzewo[2], inorder=True)
        if preorder == True:
            yield drzewo[1]
            if drzewo[0] != None:
                yield from obejdź(drzewo[0], preorder=True)
            if drzewo[2] != None:
                yield from obejdź(drzewo[2], preorder=True)
        if postorder == True:
            if drzewo[0] != None:
                yield from obejdź(drzewo[0], postorder=True)
            if drzewo[2] != None:
                yield from obejdź(drzewo[2], postorder=True)
            yield drzewo[1]


def zrob_drzewo(rozmiar, string):
    iterator = iter(string)
    if rozmiar == 1:
        return (None, next(iterator, None), None)
    elif rozmiar == 2:
        return ((None, next(iterator), None), next(iterator), None)
    else:
        i = 1
        while (i < rozmiar):
            i *= 2
        i = i // 2
        j = i // 2
        i = i - 1
        prawy = rozmiar - i - 1
        if prawy < j:
            temp = j - prawy - 1
            prawy += temp
            i -= temp
        listaL = []
        for z in range (i):
            listaL.append(next(iterator))
        w = next(iterator)
        listaP = []
        for z in range (prawy):
            listaP.append(next(iterator))
        x = zrob_drzewo(prawy, listaP)
        y = zrob_drzewo(i, listaL)
        return (y, w, x)

if __name__ == '__main__':
    # tee, starmap, pow, chain, partial, repeat

    #### Ćwiczenie 1
    # Rozwiąż za pomocą `groupby`, `map` oraz `max` zadanie z o najdłuższym plateau w liście (czyli wyznacz długość najdłuższego spójnego fragmentu listy o równych wartościach), np. `plateau([1,1,1,2,2,2,2,1,1,3,4,5,5,5]) = 4`
    # Nie zapomnij o liście pustej!
    # plateau([1,1,1,2,2,2,2,1,1,3,4,5,5,5])

    #Ćwiczenie 2
    g = [(1, 2), (2, 3), (3, 4)]  # -> (1,2,1), (2,3,8), (3,4,81)
    i = iter(g)
    # print(list(ex2(i)))
    print(list(z1Lambdy(i)))
    print(list(z1Lambdy(i)))


    #Ćwiczenie 3:
    # drzewo = (((None,'a',None),'l',(None,'a',None)),'k',((None,'o',None),'t',(None,'a',None)))
    # d1 = obejdź(drzewo, inorder=True)
    # print(list(d1))
    # d2 = obejdź(drzewo, postorder=True)
    # print(list(d2))
    # d3 = obejdź(drzewo, preorder=True)
    # print(list(d3))
    #
    # print(zrob_drzewo(7, [1,2,3,4,5,6,7]))
    # print(zrob_drzewo(7, 'alakota'))


    # Ćwiczenie 4
    # print(f"Fib(4) to {fibPierwszy(4, 3, 2)}.")
    # print(f"Fib(6) to {fibPierwszy(6)}.")
    # print(f"Fib(5) to {fibPierwszy(5)}.")
