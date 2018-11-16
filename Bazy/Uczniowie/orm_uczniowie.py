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
class KlasaBaza(Model):
     class Meta:
        database = baza
        
class Uczen(KlasaBaza): # Definicja klasy o nazwie Klasa
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    plec = BooleanField()
    egzhum = FloatField(default=0)
    egzmat = FloatField(default=0)
    egzjez = FloatField(default=0)
    klasa = ForeignKeyField(Klasa)


class Klasa(KlasaBaza): # Definicja klasy o nazwie Klasa
    klasa = CharField(null=False)
    rok_naboru = CharField(null=False)
    rok_matury= CharField(null=False)

    
        
class Przedmiot(KlasaBaza): # Definicja klasy o nazwie Klasa
    przedmiot = CharField(null=False)
    imie_naucz = CharField(null=False)
    nazwisko_naucz = CharField(null=False)
    plec_naucz = BooleanField()

    
class Ocena(KlasaBaza): # Definicja klasy o nazwie Klasa
    datad = DateField(null=False)
    ocena = FloatField(default=0)
    uczen = ForeignKeyField(Uczen)
    przedmiot = ForeignKeyField(Przedmiot)

def main(args):
    
    if os.path.exists(baza_nazwa):
        os.remove(baza_nazwa)
        
    baza.connect() # połączenie z bazą
    baza.create_tables([Uczen,Klasa,Przedmiot, Ocena]) # bez ''( nie tak ! 'klasa')  bo to nie napisy - Mapowanie obiektowo relacyjnie OMR - przetłumaczenie z jednego sposobu zapisu do drugiego 
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
