/*
 * potęga.cpp
 * a0 = 1
 * a1 = a
 * an = a*...*a (n-czynników) dla n zawiera N+ - {1}
 */


#include <iostream>
using namespace std;

float potega_it(float x, int n) 
{
    int wynik = 1;
    for (int i = O ; i< n; i++ ){
        wynik = wynik*n;
        //cout << i << endl;
    }
    return wynik;
}        


int main(int argc, char **argv)
{
    float x;
    int n;
    
    cout<<"Podaj podstawę: "<< endl;
    cin >> x ;
    cout<<"Podaj wykładnik: "<< endl;
    cin >> n ;
    cout<< "Potęga:" << potega_it(float x, int n) << endl; 
	
	return 0;
}

