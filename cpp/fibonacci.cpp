/*
 * fibonacci.cpp
 *
 * 
 */


#include <iostream>
#include <cstdlib>
using namespace std;


void fib_iter(int n)
{
    int a=0;
    int b=1;
    //int wynik;
    
    for(int i=0;i<n;i++ )
    {
        
        cout<<b<<" ";
        b += a;
        a = b-a;
            // wynik = a + b;
            // a = b;
            //b = wynik;
    }
}
int main(int argc, char **argv)
{
	int n;
    cout<<"Podaj liczbę"<<endl;
    cin>>n;
    
    fib_iter(n);
	return 0;
}

