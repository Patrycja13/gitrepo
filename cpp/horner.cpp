/*
 * horner.cpp
 * 
 */


#include <iostream>
using namespace std;

// W(x) = 2X^3 + 3X^2 + 5X + 4 
// W(x) = x(2x^2 + 3x + 5) + 4
// W(x) = x (x (2x + 3) +5) +4

float horner_it(int k, float tbwsp[],float x)
{
    int i;
    float wynik = tbwsp[0];//tbwsp[0]-   0 - pierwsza wartość w tabeli
    for (i=1;i<k+1;i++){
    //k+1 bo bo k to 3 i skończyłoby się na 3 
        wynik = wynik*x + tbwsp[i];
    }
    return wynik;
}

int horner_rek(int k, float tbwsp[],float x)
{
    if (k==0)
        return tbwsp[0] * x;
    return horner_rek(k-1,tbwsp,x) * x + tbwsp[k];
}
int main(int argc, char **argv)
{
    int stopien = 3;
    float x;
    float tbwsp[4];
    int i;
    cout<<"Podaj wartość x "<<endl;
    cin>> x;
    
    for(i=0; i<4 ;i++)// 2 człon oznacza ile razy !!!
     {
        cout<<"Podaj współczynniki ";
        cin>>tbwsp[4];
}
    
    //cout<<horner_it(stopien,tbwsp,x)<<endl;
    cout<<horner_rek(stopien,tbwsp,x)<<endl;
    
    
	
	return 0;
}

