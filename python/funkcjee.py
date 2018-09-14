#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  funkcjee.py
#  
#  

import random

def wypelnij(lista, ile, maks):
    for i in range(ile):
        lista.append(random.randint(0, maks))
    return lista

def main(args):
    lista = []
    ile = 75
    maks = 100
    wypelnij(lista, ile, maks)
    print(lista )
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
