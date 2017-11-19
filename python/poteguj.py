#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  

def potega(a,b):
    i = 1
    wynik = 1
    while i <= b:
        wynik = wynik * a
        i = i + 1 
    return wynik 

def main(args):
    a= float(input("Podaj podstawę"))
    b= int(input("Podaj wykładnik"))
    
    assert potega(1,1)== 1
    assert potega(2,2)== 4
    assert potega(3,3)== 27
    
    print ('Potega:', potega(a,b))
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
