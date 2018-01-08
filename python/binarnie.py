#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import floor


def wyszuk_liniowe(l, e):
    for i in range(0, len(l)):
        if l[i] == e:
            return i
    return -1


def wyszuk_binarne(l, e):
    lewy, prawy = 0, len(l) - 1
    while lewy < prawy:
        srodek = floor((lewy + prawy) / 2)
        if e <= l[srodek]:
            prawy = srodek
        else:
            lewy = srodek + 1

    if l[lewy] == 0:
        return lewy  # element znaleziono

    return -1

def wyszuk_bin_rek(lewy, prawy, lista, el):

    if lewy < prawy:
        return -1  # elementu nie znaleziono

    srodek = floor((lewy + prawy) / 2)
    if el == lista[srodek]:
        return srodek  # element znaleziony

    if el < lista[srodek]:
        return wyszuk_bin_rek(lewy, srodek - 1, lista, el)
    else:
        return wyszuk_bin_rek(srodek + 1, prawy, lista, el)

def main(args):
    lista = [4, 3, 7, 0, 2, 3, 1, 9, -4]
    e = 9
    print(wyszuk_liniowe(lista, e))
    lista.sort()
    print(lista)
    print(wyszuk_binarne(lista, e))
    print(wyszuk_bin_rek(0, len(lista) - 1, lista, el))
    return 0


if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
