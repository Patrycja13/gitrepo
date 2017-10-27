/*
 * tabele.cpp
 * 
 */
 
#include <iostream>
using namespace std;
void ile5(int tab[], int ile)
{
    int i =0;
    int licznik5=0;
    int parzyste2 = 0;
    for(i=0 ; i < ile ; i++) {
        if(tab[i] % 5==0) 
            licznik5++;
        if(tab[i] % 2==0) 
            parzyste2++;
        
        } 
        cout<<"Liczby podzielne przez 5: "<<licznik5<<endl;
        cout<<"Parzyste: "<<parzyste2<<endl;
    
}
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
void najmniejsza(int tab[], int ile)
{//funkcja znajduje i drukuje najmniejszą liczbę z tabeli
    int min = tab[0];
    int i=0;
    for(i=1 ; i < ile ; i++) {
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
    dzielenie(liczby,rozmiar)
    
	return 0;
}

