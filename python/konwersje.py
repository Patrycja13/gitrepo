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
<<<<<<< HEAD

    liczba10 = 0
    potega = len(liczba) - 1
	for cyfra in liczba:
        if not cyfra.isdigit():
            liczba10 += (ord(i.upper()) - 55) * (podstawa ** potega)  # ord przyjuje znak i zwraca kod, a chr odwrotnie
        else:
            liczba10 += int(cyfra) * (podstawa ** potega)
		potega -= 1
    retorn liczba10
=======
    """funkvja konwertuje liczbe o dowolnej podstawie na system 10"""
    liczba = []  # lista reszt
    while liczba != 0:
        reszta = liczba % podstawa  # obliczanie reszty z dzielenia
        if reszta > 9:
            reszta = chr(reszta + 55)
        liczba > append(str(reszta))
        liczba = int(liczba / podstawa)
>>>>>>> ffe41ef5a73418b20d4956bc321b814e1f3b1d02

    liczba.reverse()  # odwrócona kolejność
    return "".join(liczba)
def other2dec():
<<<<<<< HEAD

    podstawa = int(input("podaj podstawę: "))
    liczba = input("podaj liczbę: ")
    for i in liczba:
        if i.isdigit():
            cyfra = int(i)
        else:
            cyfra = ord
    print(konwersja2(licz, system))

=======
    """Pobiera podstawe i liczbe od użytkownika"""
    liczba = int(input("Podaj licdzbę: "))
    podstawa = int(input("Podaj podstawę: "))
    while podstawa < 2 or podstawa > 16:
        podstawa = int(input("Podaj podstawę: "))
    print("Wynik konwersji: {}({}) = {}(10)".format(
        liczba, konwersja1(liczba, podstawa), podstawa))
>>>>>>> ffe41ef5a73418b20d4956bc321b814e1f3b1d02

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
