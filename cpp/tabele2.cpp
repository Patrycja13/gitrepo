/*
 * tabele.cpp
 * 
 */
 
#include <iostream>
using namespace std;
void pobierzLiczby(int tab[], int ile )//po nazwie tabeli nawias kwadratowy 
{
    int i =0;
    for(i=0;i<ile;i++) {
        cout<<"Podaj liczbę ";
        cin >> tab[i];
        }
}

void sumuj(int tab[], int rozmiar)
{
    int i =0;
    int suma =0;
    for(i=0 ; i < rozmiar ; i++) {
    suma += tab[i];
    }
    cout<<"Suma liczb : "<<suma<<endl;
}
void najmniejsza(int tab[], int min)
{//funkcja znajduje i drukuje najmniejszą liczbę z tabeli
    int i =0;
    //int min = 0;
    for(i=0 ; i < min ; i++) {
    //min > tab[i];
    if(min > tab[i])
    min = tab[i];
    }
    cout<<"Najmniejsza wczytana liczba : "<<min<<endl;
}
int main(int argc, char **argv)
{
    int rozmiar = 0;
    cout<<"Ile liczb podasz? ";
    cin >>rozmiar;
	
    int liczby [rozmiar];
    
    pobierzLiczby(liczby, rozmiar);
    sumuj(liczby, rozmiar);
    najmniejsza(liczby, rozmiar);
    
	return 0;
}

