/*
 * potęga.cpp
 * a0 = 1
 * a1 = a
 * an = a*...*a (n-czynników) dla n zawiera N+ - {1}
 */


#include <iostream>

using namespace std;

float potega_it(float a, int n){
    float wynik = 1;
    for(int i=0;i<n;i++){
        cout<< i <<endl;
        wynik = wynik*a;
    }
    return wynik;
}

int potega_rek( float a, int n)
{
    if (n == 0)
        return 1;
    else 
        return potega_rek(a, n-1) * a;
}

int main(int argc, char **argv)
{
    //pobierz od użytkownika podstawę i wykładnik
    float a = 0;
    int n = 0;
    cout<<"podaj podstawę"<<endl;
    cin>>a;
    cout<<"podaj wykładnik"<<endl;
    cin>>n;
    cout<<"potęga: "<<potega_rek(a,n)<<endl;
        
    return 0;
}

