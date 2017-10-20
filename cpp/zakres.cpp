/*
 * funkcje.cpp
 */


#include <iostream>
using namespace std;

//int liczba, krok;//zmienne globalne dostępne w każdej funkcji, każda funkcja ma do niech dostęp
int zwieksz(int liczba, int krok){
    liczba = liczba+krok;
    krok=3*krok;
    return liczba;
}
void zwieksz2(int &a, int &b)
{   a=a+b;
    b = 3*b;
    
    }

int main(int argc, char **argv)

{
    int liczba, krok;//zmienna lokalna widoczna tyko w danej funkcji
    
    cout <<"Podaj liczbę i krok ";
    cin >> liczba >> krok;
    
    cout <<"Liczba i krok "<<liczba<<" "<< krok <<endl;
    //zwieksz();
    //cout <<"Liczba i krok "<<zwieksz()<<" "<< krok <<endl;

	return 0;
}

