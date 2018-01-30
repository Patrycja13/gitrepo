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
""" 745(8) = 7 * 8^2 + 4*8^1 + 5 """

    liczba10 = 0
    potega = len(liczba) - 1
	for cyfra in liczba:
        if not cyfra.isdigit():
            liczba10 += ord(i.upper)  # ord przyjuje znak i zwraca kod, a chr odwrotnie
        liczba10 += int(cyfra) * (podstawa ** potega)
		potega -= 1

def other2dec():

    system = int(input("podaj system: "))
    licz = input("podaj liczbę: ")
print(konwersja2(licz, system))


def main(args):
    print("Zamiana liczby dziesiętnej na liczbe o danej podstawie"
          "<2;16> lub odwrotnie.")
    dec2other()
    other2dec()
    """program porzekształca liczbe o dowolnej podstawie
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv)
