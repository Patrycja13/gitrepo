#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Wersja optymalna 

def nwd_v1(a, b):

    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def nwd_v2(a, b):
    
    while a > 0:
        a = a % b
        b = b - a
        
    return b
    
            
def main(args):

    a = int(input("Podaj liczbę"))
    b = int(input("Podaj liczbę"))
    assert nwd_v2(5, 10) == 5
    assert nwd_v2(2, 5) == 1
    assert nwd_v2(4, 10) == 2
    print ("NWD({:d}, {:d}) = {:d}".format(a, b, nwd_v2(a, b)))
    print("Największy spólny dzielnik ", nwd_v2(a, b))

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
