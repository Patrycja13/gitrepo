/*
 * silnia.cpp
 * 
 * 
 */


#include <iostream>
using namespace std;

int silnia(int(n)){
    int wynik = 1;
    for(int i=2; i<= n ; i++ )
    {
        wynik=wynik*i;
        cout << wynik << endl;
    }
        
    return wynik;
}
    
int main(int argc, char **argv)
{
    int n = 1;
    cout << "Podaj liczbę"<< n << endl;
    cin>> n ;
    cout <<"Silnia "<< silnia(int(n)) <<endl;
	
	return 0;
}

