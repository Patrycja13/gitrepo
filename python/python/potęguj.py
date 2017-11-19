#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  

def potega(a,b);
    wynik = 1
    i = 0
    while i <= b:
        wynik = a ** b 
    return wynik 

def main(args):
    a= int(input("Podaj podstawę"))
    b= int(input("Podaj wykładnik"))
    
    assert type(a)==int
    assert type(b)==int
    assert potega(1)== 1
    assert potega(2)== 4
    assert spotega(3)== 9
    #  while b < 0:
        #  wynik = a ** b
        
    #  (a**b)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
