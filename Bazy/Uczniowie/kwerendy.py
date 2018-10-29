#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kwerendy.db
#  
 
import sqlite3

def kwerenda1(cur):
    cur.execute("""
        SELECT nazwisko, AVG(ocena) AS srednia, klasa FROM uczniowie
        INNER JOIN oceny ON uczniowie.id=oceny.id_uczen
        INNER JOIN klasy ON uczniowie.id_klasa=klasy.id
        GROUP BY uczniowie_id
    """)
    
    # SELECT * FROM nazwiska WHERE nazwisko LIKE 'G*' 
    wyniki = cur.fetchall()
    for row in wyniki:
        print(tuple(row))
        
        
        # SREDNIA KLASY 
        # ~SELECT AVG(ocena) AS srednia, klasa FROM uczniowie
        # ~INNER JOIN oceny ON uczniowie.id=oceny.id_uczen
        # ~INNER JOIN klasy ON uczniowie.id_klasa=klasy.id
        # ~GROUP BY klasa
        # ~ORDER BY srednia DESC
        
        # ~SELECT imie,nazwisko, AVG(ocena), klasa AS srednia FROM uczniowie
        # ~INNER JOIN oceny ON uczniowie.id=oceny.id_uczen
        # ~INNER JOIN klasy ON uczniowie.id_klasa=klasy.id
        # ~GROUP BY klasa
        
        # ZLICZANIE OSÓB Z TAKĄ ŚREDNIĄ 
        # ~WITH srednie AS (
            # ~SELECT imie,nazwisko, AVG(ocena) AS srednia FROM uczniowie
            # ~INNER JOIN oceny ON uczniowie.id=oceny.id_uczen
            # ~GROUP BY id_uczen
        # ~) SELECT COUNT(imie) FROM srednie
          # ~WHERE srednia > 3.8
        
        # WYBIERANIE Z TABELI ŚREDNIEJ POWYŻEJ...
        # ~WITH srednie AS (
            # ~SELECT imie,nazwisko, AVG(ocena) AS srednia FROM uczniowie
            # ~INNER JOIN oceny ON uczniowie.id=oceny.id_uczen
            # ~GROUP BY id_uczen
        # ~) SELECT imie, nazwisko, srednia FROM srednie
          # ~WHERE srednia > 3.8
        
        
        # group by i where nie można stosowac razem ! 
        
        
        # 10 NAJLEPSZYCH UCZNIÓW, GDZY 10 NAJGORSZYCH ZAMIAST DESC - ASC
        # ~SELECT imie,nazwisko, AVG(ocena) AS srednia FROM uczniowie
        # ~INNER JOIN oceny ON uczniowie.id=oceny.id_uczen
        # ~GROUP BY id_uczen
        # ~ORDER BY srednia DESC
        # ~LIMIT 10 
        
        # SORTOWANIE WZGLĘDEM JAKIEGOŚ POLA
        # ~SELECT klasa, nazwisko FROM klasy
        # ~INNER JOIN uczniowie
        # ~ON klasy.id=uczniowie.id_klasa
        # ~ORDER BY klasa ASC
    
        # UCZNIOWIE KLASY 
        # ~SELECT klasa, nazwisko, imie FROM klasy
        # ~INNER JOIN uczniowie
        # ~ON klasy.id=uczniowie.id_klasa
        # ~WHERE klasa='1A'
        
        # oceny z przedmiotu
        # ~SELECT nazwisko, imie1, pol FROM nazwiska
        # ~INNER JOIN oceny
        # ~ON nazwiska.nr_ucznia=oceny.nr_ucznia

        
        #SELECT nazwisko, imie1, dzien, miesiac, rok FROM nazwiska
        #INNER JOIN dane_osobowe ON nazwiska.nr_ucznia=dane_osobowe.nr_ucznia
        #WHERE nazwiska.nr_ucznia=9201
        
        # Kwerenda wyświetla numer ucznia
        
        # ~SELECT nazwisko, imie1, dzien, miesiac, rok FROM nazwiska
        # ~INNER JOIN dane_osobowe 
        # ~ON nazwiska.nr_ucznia=dane_osobowe.nr_ucznia
        # ~WHERE nazwiska.nr_ucznia=
        # ~(SELECT nr_ucznia FROM nazwiska WHERE nazwisko= "Gryczon" AND imie1= "Agata")
        
def main(args):
    ### KONFIGURACJA ###
    baza_nazwa = 'uczniowie'
    tabele = ['uczniowie', 'klasy', 'przedmioty', 'oceny']
    roz = '.csv'
    naglowki = True
    ####################
    
    con = sqlite3.connect(baza_nazwa + '.db')
    cur = con.cursor()  # obiekt tzw. kursora
    
    kwerenda1(cur)
    
    con.commit()
    con.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
