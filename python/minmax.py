#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  minmax.py
#  
#  
import random


def losuj(ileliczb, maksliczb):
    liczby = []  # pusta lista

    ile = 0  # liczba unikalnych liczb
    # for i in range (ileliczb):

    while ile < ileliczb:
        liczba = random.randint(0, maksliczb)
        if liczby.count(liczba) == 0:
                liczby.append(liczba)
                ile += 1
    print(liczby)
    return liczby


def minimum(lista):
    """wyszukwanie minimum"""
    min = lista[0]
    for i, el in enumerate(lista):
        if el < min:
            min = el
        print(i, el)

    return min


def maksimum(lista):
    # wyszukwanie minimum
    max = lista[0]
    for i, el in enumerate(lista):
        if el > max:
            max = el
        print(i, el)

    return max


def main(args):
    lista = losuj(20, 50)
    assert minimum([7, 5, 3, 1]) == 1
    assert maksimum([7, 5, 3, 1]) == 7

    print("Min: ", minimum(lista))
    print("Max: ", maksimum(lista))

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
