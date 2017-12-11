#!/usr/bin/env python
# -*- coding: utf-8 -*-
#


def potega(a, n):
    i = 1
    wynik = 1
    while i <= b:
        wynik = wynik * a
        i = i + 1
    return wynik

#  potega_rek(a, 0) = 1 dla a różnego od 0
#  potega_rek(a, n) = potega_rek(a, n-1)*a dla n =  zbiór liczb naturalnych dodatnich

def potega_rek(a, n):
    if n == 0:
        return 1
    return potega_rek(a, n-1) * a


def main(args):

    a = int(input("Podaj podstawę")
    n = int(input("Podaj wykładnik"))

    assert potega(1,1)== 1
    assert potega(2,2)== 4
    assert potega(3,3)== 27

    print ('Potega:', potega(a,b))
    print ('Potega:',potega_rek(a, n))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
