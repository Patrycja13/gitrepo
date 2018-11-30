#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  str.py
#  
#  


def push(stos, rozmiar, SP,dane):
    if SP < rozmiar:
        stos[SP]= dane
        SP += 1 # inkrementacja
    else:
        print("Stack overflow")
    return SP

def pop(rozmiar):
    element = None
    SP -= 1
    if SP > -1:
        element = (stos[SP])
        stos[SP] = None
    else:
        print("Stack overflow")
        
    return SP, element
        
def main(args):
    stos = [] # pusta lista, zasięg globalny 
    SP = 0 # wskażnik wierzchołka
    rozmiar = 3
    stos = [None] * rozmiar
    SP = push(stos, rozmiar, SP, 2)
    SP = push(stos, rozmiar, SP, 5)
    SP, element = pop(stos, rozmiar, SP, 4 )
    print(element)
    print(SP)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
