/*
 * potęga.cpp
 * a0 = 1
 * a1 = a
 * an = a*...*a (n-czynników) dla n zawiera N+ - {1}
 */


#include <iostream>

using namespace std;

float potega_it(float x, int n) {
    float wynik = 1;
    for (int i=0 ; i>=1 ; i++ )
        {
        cout << i << endl;
        }
}        


int main(int argc, char **argv)
{
    float a = 0;
    int b = 0;
    cout<<"Podaj podstawę: "<< a << endl;
    cin >> a
    cout<<"Podaj wykładnik: "<< b << endl;
    cin >> b
    cout<< "Potęga:" << potega_it(float a, int b) << endl; 
	
	return 0;
}

