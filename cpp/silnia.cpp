/*
 * silnia.cpp
 * 
 * 
 */


#include <iostream>
using namespace std;

int silnia (int(n));
{

    int wynik = 1 
    for (int i=2; i<= int n ; i++ )
    {
        wynik=wynik*i
        cout << wynik << endl;
    }
        
    return wynik;
}
    
int main(int argc, char **argv)
{
    int n = 0
    cout<<"Podaj liczbę"<<endl;
    cin>> n 
    cout<<"Silnia"<< silnia_it(n) <<endl;
	
	return 0;
}

