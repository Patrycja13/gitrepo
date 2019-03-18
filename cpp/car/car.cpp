/*
 * car.cpp
 * 
 */
#include <iostream>
#include <cstdlib>
#include "car.h"
#include "osoba.h"

Car::Car() {
    rocznik=przebieg=0;
}

Car::Car(string mr, string ml, int r, int p) {
    if (r <= 1970) r = 1990;
    marka = mr;
    model = ml;
    rocznik = r;
    przebieg = p;
}

void Car::dodaj() {
    cout << "Dodaj samchód:" << endl;
    cout << "Marka: "; cin >> marka;
    cout << "Model: "; cin >> model;
    cout << "Rocznik: "; cin >> rocznik;
    cout << "Przebieg: "; cin >> przebieg;
}

void Car::dane() {
    cout << endl;
    cout << "Twój samchód:" << endl;
    cout << "Marka: " << marka << endl;
    cout << "Model: " << model << endl;
    cout << "Rocznik: " << rocznik << endl;
    cout << "Przebieg: " << przebieg << endl;
}

void Osoba::() {
    cout << "Podaj dane:" << endl;
    cout << "Imie: "; cin >> imie;
    cout << "Nazwisko: "; cin >> nazwisko;
    cout << "Wiek: "; cin >> wiek;
    cout << "Płeć: "; cin >> plec;

}

void Osoba::pasazerowie() {
    cout << endl;
    cout << "Twoje dane :" << endl;
    cout << "Imie: " << imie << endl;
    cout << "Nazwisko: " << nazwisko << endl;
    cout << "Wiek: " << wiek<< endl;
    cout << "Płeć: " << plec << endl;
}

