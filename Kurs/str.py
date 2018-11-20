#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  str.py
#  
#  

stos = [] # pusta lista, zasięg globalny 
SP = 0 # wskażnik wierzchołka

def push(rozmiar,dane):
    global stos, SP
    if SP < rozmiar:
        stos[SP]= dane
        SP += 1 # inkrementacja
    else:
        print("Stack overflow")
        

def pop(rozmiar):
    global stos, SP
    SP -= 1
    if SP > -1:
        print(stos[SP])
        stos[SP] = None
    else:
        print("Stack overflow")
def main(args):
    global stos, SP
    rozmiar = int(input("Podaj rozmiar stosu "))
    stos = [None] * rozmiar
    push(rozmiar, 2)
    push(rozmiar, 3)
    pop(rozmiar)
    push(rozmiar, 4)
    pop(rozmiar)
    push(rozmiar, 5)
    print(SP)
    print(stos)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
