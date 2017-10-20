/*
 * tabele.cpp
 * 
 */


#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
	int liczby [10];
    int i = 0;
    int suma =0;
    int licznik = 0;
    for(i=0;i<10;i++) {// i () zmienna interacyjjna)w tablicach od 0, 
                        //jeśli tablica ma 10 komórek to indeks ostatnoego elementu jest mniejszo o 1 od ilości elementów w tablicy 
    cout<<"Podaj liczbę ";
    cin >> liczby[i];
    
   } 
   
     for(i=0;i<10;i++) 
     {
        
        //cout<<liczby[i]<<" ";
        suma += liczby[i];
        if (liczby[i]%2==0)// liczba zawarta w tabeli dzieli się modulo przez 2 i da resztę 0 to jest parzysta
            licznik++;
    }  
    
    cout<<"Suma liczb "<< suma <<endl;
    cout<<" Ilość liczb parzystych "<< licznik <<endl;
    
	return 0;
}

