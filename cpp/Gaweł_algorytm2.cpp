/*
 * aolgorytm2.cpp
 *
 * 
 * 
 */


#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
	int n;
    cout<<"Podaj n"<<endl;
    cin>>n;
    
    int suma = 0;
    int ile_parzystych;
    
    for (int i=0;i<n;i++)
    {
        int liczba;
        cout<<"Podaj liczbę "<<endl;
        cin >>liczba;
        
        if (liczba % 2 == 0)
            {
            suma += liczba;
            ile_parzystych++;
            }
        
  
 }   
    cout<<"Parzyste"<< ile_parzystych <<endl;
    cout<<"Suma"<<suma<<endl;
    
	return 0;
}

