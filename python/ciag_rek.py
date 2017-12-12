#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ciag_rek.py
#  
# a1 =2 
# an = an - 1*n^ + 1


def rek(n):
    if n == 1:
        return 2
    return rek(rek*n - 1*n^ + 1)
    
def main(args):
    
    n = int(input("Podaj liczbę"))
    print(" ", rek(n))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
