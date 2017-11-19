/*
 * hello.cpp
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
	//char imie; //deklaracja zmiennej znakowej
    int a, b, c;
 a=b=c=0; 

    cout <<" Podaj liczby : " << endl;
    cin >>a >> b>> c;
    if (a > b )
    {
        if ( a>c) cout << "Największe jest a!" ; 
            //a większe od b i od c
        else cout << "Największe jest c!" ;
    }
        else 
        {
            ; // a nie jest większe od b 
            }
 
         
    
	return 0;
}

