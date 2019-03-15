/*
 * car.cpp
 * 
 */


#include <iostream>
#include <cstdlib>
#include "car.h"

Car:: Car(){
    rocznik=przebieg=0;
    
}

Car:: Car(string mr, string ml, int r, int p){
    if (r<= 1970) r = 1990; // zasady co do poprawności danych
    marka = mr;
    model = ml;
    rocznik = r;
    przebieg= p;
    
}

void Car::dodaj(){
    cout << "Dodaj samochód "<< endl;
    cout << "Podaj markę "; cin.getline(marka, rozmiar);
    cout << "Podaj model "; cin.getline(model, rozmiar);
    cout << "Podaj rocznik "; cin >> rocznik;
    cout << "Podaj przebieg "; cin >> przebieg;
    
    
}


void Car::dane(){
    cout << endl;
    cout << "Twój samochód "<< endl;
    cout << " Marka " << marka << endl;
    cout << " Model " << model << endl;
    cout << " Rocznik " << rocznik << endl;
    cout << " Przebieg " << przebieg << endl;
    
    
}

