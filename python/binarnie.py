#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import floor


def wyszukiwanie_liniowe(l, e):

    for i in range(0, len(l)):
        if l[i] == e:
            return i
    return -1  # 0 nie może być bo to poprawnym indeks tabeli,  musi być
    # dowolna wartość niemożliwa dla indekssu czyli na -


def wyszukiwanie_binarne(l, e):

    lewy, prawy = 0, len(l - 1)  # 0 bo krańcowe po lewej stronie,
    #  prawy - 1 bo indeksy startują od 0
    while lewy < prawy:
        srodek = floor(lewy + prawy) / 2
        print(srodek)
        if e <= 1[srodek]:
            prawy = sredek
        else:
            lewy = srodek + 1

    return -1


def main(args):

    l = [4, 3, 7, 0, 2, 3, 1, 9, -4]
    e = 1
    print(wyszukiwanie_liniowe(l, e))
    print(wyszukiwanie_binarne(l, e))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
