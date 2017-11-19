#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  mlotek.py

import random #biblioteka, modul króry pozwala losować liczby z danego zakresu 



def main(args):
    
    liczba = random.randint(1, 10)
    for i in range(3):
        odp = int (input("Jaką liczbę mam na myśli ? (1-10)"))
        if liczba == int (odp):
            print ("Zgadłeś ")
        else:
            print ("Błąd ")
        
    print(liczba)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
