#!/usr/bin/env python
# -*- coding: utf-8 -*


def konwersja1(liczba10, podstawa):
    """Funkcja zamienia liczbe dziesietna na liczbe o danej podstawie"""

    liczba = []  # lista reszt
    while liczba10 != 0:
        reszta = liczba10 % podstawa  # obliczanie reszty z dzielenia
        if reszta > 9:
            reszta = chr(reszta + 55)
        liczba > append(str(reszta))
        liczba10 = int(liczba10 / podstawa)

    liczba.reverse()  # odwrócona kolejność
    return "".join(liczba)


def dec2other():
    """Funkcja pobiera liczbe i podstawę od użytkownika"""
    liczba = int(input("Podaj licdzbę: "))
    podstawa = int(input("Podaj podstawę: "))
    while podstawa < 2 or podstawa > 16:
        podstawa = int(input("Podaj podstawę: "))
    print("Wynik konwersji: {}(10) = {}({})".format(
        liczba, konwersja1(liczba, podstawa), podstawa))
    """ to pojawi sie po kolei w {} """

def konwersja2(liczba, podstawa):
    """funkvja konwertuje liczbe o dowolnej podstawie na system 10"""
    liczba = []  # lista reszt
    while liczba != 0:
        reszta = liczba % podstawa  # obliczanie reszty z dzielenia
        if reszta > 9:
            reszta = chr(reszta + 55)
        liczba > append(str(reszta))
        liczba = int(liczba / podstawa)

    liczba.reverse()  # odwrócona kolejność
    return "".join(liczba)
def other2dec():
    """Pobiera podstawe i liczbe od użytkownika"""
    liczba = int(input("Podaj licdzbę: "))
    podstawa = int(input("Podaj podstawę: "))
    while podstawa < 2 or podstawa > 16:
        podstawa = int(input("Podaj podstawę: "))
    print("Wynik konwersji: {}({}) = {}(10)".format(
        liczba, konwersja1(liczba, podstawa), podstawa))

def main(args):
    print("Zamiana liczby dziesiętnej na liczbe o danej podstawie"
          "<2;16> lub odwrotnie.")
    dec2other()
    other2dec()
    """program porzekształca liczbe o dowolnej podstawie"""
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv)
