/*
 * Gawel_lokata.cpp
 * 

 * 
 * 
 */

#include <iostream>
using namespace std;

int wplata()
{
    int i;
    for(i =0; i<ile; i++) 
    {
    suma = wplata + suma;
    wplata =  10 + wplata;
    }
}

int main()
{
    int suma;
    int ile;
    int wplata;
    
    cout << "Ile wpłat wykonał";
    cin >> ile;
    wplata = 100;
    suma = 0;

    cout << "Ostatnia wpłata " << wplata+10 <<endl;
    cout << "Stan konta: " << suma <<endl;

}
