#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  silnia.py
#  n! = 1 dla n={0,1}
#  n! = 1*...*n dla N+ - {1}


def silnia_it(n):
    wynik = 1
    for i in range(2, n+1):
        wynik = wynik*i
    return wynik 
    
def main(args):

    #pobierz od uzytkownika liczbę naturalna i przypisz ją do zmiennej n 
    # wywołaj funkcje sinia_it() z odpowiednim argumentem 
    n = int(input("Podaj liczbę naturalną"))
    print (silnia_it(n))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
