#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  

def poteguj_it(a,b):
    #wynik = 1
    while b < 0:
        wynik = a ** b 
   # return wynik 
    print (a**b)
    
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
        
    #  print (a**b)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
