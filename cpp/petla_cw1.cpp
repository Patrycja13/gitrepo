/*
 * petla_cw1.cxx
 */


#include <iostream>
using namespace std;
int main(int argc, char **argv)
{
    int suma=0 ;
    int liczba = 0; 
    cout << "Wprowadzaj kolejne liczby: "<< endl;
    
    
        while(1)
        {   
        cin >> liczba ;
        cout << "Podano:" << liczba << endl;
        suma += liczba ;
        if (suma >75)
            break;
        };
        
        cout << "Suma liczb :" << suma << endl;

	return 0;
}

