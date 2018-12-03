#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kwerendy_orm.py
#  

from uczniowie_model import *

def kw01():
    # SELECT * FROM uczen WHERE imie LIKE 'G%'; w sql
    # query = Uczen.select().where(Uczen.imie.startswith('G'))
    # query = Uczen.select().where(Uczen.imie == 'Rafał')
    # query = Uczen.select().where(Uczen.imie == 'Rafał').count() # jesli interesuje nas tylko liczba wyników 
    # print(query)
    # query = Uczen.select().where(Uczen.egz_mat > 40) # zlicza wyniki powyżej czegoś
    # query = Uczen.select().where(Uczen.egz_mat.between(30,35)) # zlicza wyniki pomiędzy 
    query = (Uczen
        .select()
        .where(Uczen.egz_mat.between(30,35))
        .order_by(Uczen.egz_mat.asc()) # asc rosnące, desc malejące 
    )
    for obj in query:
        print(obj.nazwisko, obj.imie, obj.egz_hum)
       

def kw02():
    #SELECT nazwisko, klasa FROM uczen INNER JOIN klasa ON uczen.id_klasa = klasa.id;
    query = (Uczen
        .select(Uczen.nazwisko, Uczen.klasa.klasa)
        .join(Klasa)
        .where(Uczen.klasa.klasa.startswith('3')) # jeśl nie interesują nas wszyscy tylko dany ktoś
        .order_by(Uczen.klasa.klasa.asc())
    )
    for obj in query:
        print(obj.nazwisko, obj.klasa.klasa)

def kw03():
    # lista nazwisk uczniów na literę d i ich oceny 
    query = (Ocena
        .select(Ocena.uczen.nazwisko, Ocena.ocena)
        .join(Uczen)
        .where(Ocena.uczen.nazwisko.startswith('B'))
    )
    
    for obj in query:
        print(obj.uczen.nazwisko, obj.ocena)
        
def kw04():
    # po ile ocen mają uczniowie 
    query = (Ocena
        .select(Ocena.uczen.nazwisko, fn.Count(Ocena.ocena).alias('ile'))
        .join(Uczen)
        .group_by(Ocena.uczen.nazwisko)
        .order_by(SQL('ile').asc())
    )
    
    for obj in query:
        print(obj.uczen.nazwisko, obj.ile)
        
def kw05(): 
    # po ile uczniów w klasie
    query = (Uczen
        .select(Uczen.klasa.klasa, fn.Count(Uczen.nazwisko).alias('ile'))
        .join(Klasa)
        .group_by(Uczen.klasa.klasa)
        .order_by(SQL('ile').desc())
    )
    
    for obj in query:
        print(obj.ile, obj.klasa.klasa)
        
def kw06():
    # średnia ocen z przedmiotów
    query = (Ocena
        .select(Ocena.przedmiot.przedmiot, fn.AVG(Ocena.ocena).alias('srednia'))
        .join(Przedmiot)
        .group_by(Ocena.przedmiot.przedmiot)
        .order_by(SQL('srednia').asc())
    )
    
    for obj in query:
        print(obj.przedmiot.przedmiot, obj.srednia)

def kw07():
    # średnia ocen uczniów
    query = (Ocena
        .select(Ocena.uczen.nazwisko, fn.AVG(Ocena.ocena).alias('srednia'))
        .join(Uczen)
        .group_by(Ocena.uczen.nazwisko)
        .order_by(SQL('srednia').asc())
    )
    
    for obj in query:
        print(obj.uczen.nazwisko, obj.srednia)

def kw08():
    # oceny konkretnego ucznia ... z poszczególnych przedmiotów 
    query = (Uczen
        .select(Ocena.uczen.nazwisko, Przedmiot.przedmiot)
        .where(Uczen.nazwisko == 'Szymczak')
        .join(Uczen)

    )
    
    for obj in query:
        print(obj.ocena.nazwisko)
        
def main(args):
    baza.connect()
    
    # kw01()
    # kw02()
    # kw03()
    # kw04()
    # kw05()
    # kw06()
    # kw07()
    kw08()
    baza.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
