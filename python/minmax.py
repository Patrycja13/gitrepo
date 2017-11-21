#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  minmax.py
#  
#  

import random

def losuj(ileliczb, maksliczb):

    liczby = []  

    ile = 0  
    while ile < ileliczb:
        liczba = random.randint(0, maksliczb)
        if liczby.count(liczba) == 0:
            liczby.append(liczba)
            ile += 1
    print(lista)
    return liczby
    
def minimum(lista):
    """wyszukiwanie minimum"""
    min = lista[0]
    for i, el in enumerate(lista):
        print (i ,el)

def main(args):
    lista = losuj(20, 50)
    print("Min:",minimum(lista))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
