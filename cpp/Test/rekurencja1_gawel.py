#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  rekurencja1.py



def rek(n):
    if n < 2:
        return 1
    return rek(n - 1) + rek(n - 2)
    
def main(args):
    
    n = int(input("Podaj liczbę"))
    print(rek(n))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
