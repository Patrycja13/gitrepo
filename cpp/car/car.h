// car.h
#include <iostream>
#include <cstdlib>

#ifndef __CAR_H_
#define __CAR_H_


using namespace std;

class Osoba {
    private:
        string imie ;
        string nazwisko;
        int wiek;
        bool plec;
      
    public:
        Osoba();  // konstruktor
        Osoba(string, string, int, bool); // konstruktor
};

class Car {
    private:
        string marka;
        string model;
        int rocznik;
        int przebieg;
        Osoba osoby[3];
        int rozmiar = 50;
    public:
        Car();  // konstruktor
        Car(string, string, int, int); // konstruktor
        void dodaj();
        void dane();
        void laduj(ile);
        void pasazerowie();
};
#endif
