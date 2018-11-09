#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  orm_peewee.py
#  

import os 
from peewee import * 
 
baza_nazwa = 'test.db' # zmienna globalna
baza = SqliteDatabase(baza_nazwa) # instalacja bazy 


### modele ###

class Klasa(Model): # Definicja klasy o nazwie Klasa
    nazwa = CharField(null=False)
    roknaboru = IntegerField(default=0)
    rokmatury= IntegerField(default=0)
    class Meta:
        database = baza

class Uczen(Model): # Definicja klasy o nazwie Klasa
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    plec = BooleanField()
    klasa = ForeignKeyField(Klasa, related_name='Uczniowie')
    
    class Meta:
        database = baza
        
class Wynik(Model): # Definicja klasy o nazwie Klasa
    egzhum = FloatField(default=0)
    egzmat = FloatField(default=0)
    egzjez = FloatField(default=0)
    uczen = ForeignKeyField(Uczen, related_name='Wyniki')
    class Meta:
        database = baza
        
def main(args):
    
    if os.path.exists(baza_nazwa):
        os.remove(baza_nazwa)
        
    baza.connect() # połączenie z bazą
    baza.create_tables([Klasa, Uczen, Wynik]) # bez '' bo to nie napisy 
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
