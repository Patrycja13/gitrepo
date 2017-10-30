#!/usr/bin/env python
# -*- coding: utf-8 -*-

#osoba = "Adam Słodowy" #zmiennych nie deklarujemy 
#osoba = 'Adam Słodowy' #zmiennych nie deklarujemy, cudzysłów jaki chcesz 
osoba= input ("Jak się nazywasz ?")#input pobiera dane
wiek= input ("Ile masz lat ?")
 
print("Witaj, ",osoba, "!")#print wyprowadza 
print ("Urodziłeś się w ", 2017 - int (wiek)  )
rok_pythona = 1991
wiek_pythona = 2017 - rok_pythona
if wiek_pythona > int (wiek): # nie ma nawiasów tylko wcięcia na 4 spacje pod spodem 
    print ("Jestem starszy! ")
elif wiek_pythona < int (wiek):
    print ("Jestem młodszy! ")
else :
    print ("Mamy tyle samo lat! ")
    

