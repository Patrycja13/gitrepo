#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  quiz.py
#  
from peewee import *

baza_nazwa = 'quiz.db'
baza = SqliteDatabase(baza_nazwa)  # instancja bazy

### MODELE #
class BazaModel(Model):
    class Meta:
        database = baza

class Klasa(BazaModel):
    klasa = CharField(null=False)
    rok_naboru = IntegerField(default=0)
    rok_matury = IntegerField(default=0)

class Uczen(BazaModel):
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    plec = IntegerField()
    klasa = ForeignKeyField(Klasa, related_name='uczniowie')
    egz_hum = DecimalField(default=0)
    egz_mat = DecimalField(default=0)
    egz_jez = DecimalField(default=0)


def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
