#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sort_wstaw.py


from random import randint


def sort_wstaw(lista):
    """wersja liniowa"""

    for i in range(1, len(lista)):
        el = lista[i]
        k = i - 1  # k ma wskazać indeks na który należy wstawić pobrana z nieposortowanej strony(prawej) liczbę
            while k >= 0 and lista[k] > el:  # < sortowanie malejące lub > rosnące
            lista[k + 1] = lista[k]  # przesuwanie elementu
            k = k - 1
            lista[k + 1] = el

    return lista

def sort_wstaw_bin(lista):

    for i in range(1, len(lista)):
        el = lista[i]
        k = szukaj_bin(0, i, lista, el )  # wyszukiwanie binarne miejsca do wstawielnia el
        pass

def main(args):
    lista = [4,3,7,0,2,3,1,9]
        #[3,4,7,0,2,3,1,9]
        #[3,4,7,0,2,3,1,9]
        #[0,3,4,7,2,3,1,9]
        #[0,2,3,4,7,3,1,9]
        #[0,2,3,3,4,7,1,9]
        #[0,1,2,3,3,4,7,9]
    print(lista)
    print (sort_wstaw(lista))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
