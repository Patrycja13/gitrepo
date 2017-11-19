/*
 * funkcje.cpp
 */


#include <iostream>
using namespace std;
int sumuj(int a, int b) // jeśli void to funkcja nie zwraca wyniku, jęsli co innego niż void np int to return musi być w następnym
{
    return a + b;
}

int odejmij(int a, int b) 
{
     return a - b ;
}

int mnozenie(int a, int b) 
{
    return a * b ; 
}

int podziel(int a, int b) 
{
    if(b<0 && b>0);
    return a / b;
}
    
int main(int argc, char **argv)

{
	int a,b ;
    cout <<"Podaj liczby";
    cin >> a >> b;
    
    int suma = sumuj(a,b);// wynik tej funkcji przypisz do zmiennej 
    int roznica = odejmij(a,b);

   
    cout <<"Suma "<<suma<<endl;//te zmienne są całkiem w innym miejscu niż te z void
    cout <<"Różnica"<<roznica<<endl;
    cout <<"Iloczyn"<<mnozenie (a,b)<<endl;
    cout <<"Iloraz"<<podziel (a,b)<<endl;
     
	return 0;
}

