#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  orm_peewee.py
#  

import os 
from peewee import * 

def main(args):
    
    if os.path.exists(baza_nazwa):
        os.remove(baza_nazwa)
        
    baza.connect() # połączenie z bazą
    baza.create_tables([Uczen,Klasa,Przedmiot, Ocena]) # bez ''( nie tak ! 'klasa')  bo to nie napisy - Mapowanie obiektowo relacyjnie OMR - przetłumaczenie z jednego sposobu zapisu do drugiego 
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
