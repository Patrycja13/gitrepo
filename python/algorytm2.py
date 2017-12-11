#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  algorytm2.py
#  

def parzyste(n):
    a = 0
    while n%a == 0:
        return n

def main(args):
     n = int(input("Podaj liczbę"))


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
