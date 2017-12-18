#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sort_wybor.py
# 
#  

def wypelnij(t, n, maks):
    
    srand(time(NULL))
    while i < n:
    t[i] = 1 + rand() % maks
    
def drukuj(t[], n):
    
    while i < n:
    print ("  ", t[i])
    
def zamien(a, b):
    
    tmp = a
    a=b
    b=tmp
    
def sort_wyb(t[], n):
    print("--------Sortowanie przez wybieranie-------")
     
    while i<n:
        k=i
        while j<n:
            j=i+1
            if t[j]<t[k]:
                k=j
        zamien(t[i], t[k]
        
def main(args):
    
    const ile = 10
    tab[ile]
    wypelnij(tab, ile, 20)
    drukuj(tab, ile)
    sort_wyb(tab, ile)
    drukuj(tab, ile)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
