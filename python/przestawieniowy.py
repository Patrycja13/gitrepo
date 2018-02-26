#!/usr/bin/env python
# -*- coding: utf-8 -*-

def szyfruj(tekst, klucz):

    reszta = len(tekst) % klucz
    if reszta:'''  jeżeli reszta 0 to się nie wykona, jeśli nie to wykona'''
        tekst += (klucz - reszta) * "."

        szygrogram = ""
        for i in range(klucz):
            for j in range(int(len(tekst) / klucz)):

            szyfrogram += tekst[i + klucz]

def deszyfruj(szyfrogram, klucz):
    tekst = ""
    for i in range(int(len(szyfrogram) / klucz)):
        for j in range(klucz):
            # print (i + j * klucz, szyfrogram[j + i * klucz])
            tekst += szyfrogram[i + (j * int(len(szyfrogram) / klucz))]

    return tekst

def main(args):

    tekst = input("Podaj tekst: ")
    klucz = int(input("Klucz: "))
    while 2 * klucz > len(tekst):
        klucz = int(input("Klucz "))

    szyfrogram = szyfruj_cezar(tekst, klucz)
    print(szyfrogram)
    print(deszyfruj(szyfrogram, klucz))
    return 0



if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
