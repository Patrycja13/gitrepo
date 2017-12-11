/*
 * Gawel_ulamek.cpp
 *
 * 
 */

#include <iostream>
using namespace std;

int ulamek(int a, int b)
{

    int a;
    int b;
    while (a != b)
        {
        if(a > b)
           a = b - a;
       else
           b = a - a;
    return a;
        }
} 
int main( int argc, char * argv[] )
{ 
    int a;
    int b;
    
    cout << "Podaj licznik: " << endl;
    cin >> a;
    
    cout << "Podaj mianownik: " << endl;
    cin >> b;

    int licznik = a;
    int mianownik = b;
    
    licznik = licznik / a;
    mianownik = mianownik /a;
    
    
    cout << "Wynik " << licznik << " ? "<< mianownik << endl;
   
}
