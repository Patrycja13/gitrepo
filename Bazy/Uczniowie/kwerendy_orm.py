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
    # i po ile ocen mają uczniowie 
    query = (Ocena
        .select(Ocena.uczen.nazwisko, fn.Count(Ocena.ocena).alias('ile'))
        .join(Uczen)
        .group_by(Ocena.uczen.nazwisko)
        .order_by(SQL('ile').asc())
    )
    
    for obj in query:
        print(obj.uczen.nazwisko, obj.ile)
                
def main(args):
    baza.connect()
    
    # kw01()
    # kw02()
    # kw03()
    kw04()
    
    baza.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
