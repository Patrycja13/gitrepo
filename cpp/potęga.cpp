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
    float wynik = 1;
    for (int i=1 ; i < int n ; i++ )
        {
        i = i*i;
        cout << i << endl;
        }
}        


int main(int argc, char **argv)
{
    float a = 0;
    int b = 0;
    cout<<"Podaj podstawę: "<< endl;
    cin >> a
    cout<<"Podaj wykładnik: "<< endl;
    cin >> b
    cout<< "Potęga:" << potega_it(a,b) << endl; 
	
	return 0;
}

