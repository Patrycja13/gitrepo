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

int fib_rek(int n)
{
    if (n < 2)
        return 1;
    else
        return fib_rek(n - 1) + fib_rek(n - 2);
    
}
int main(int argc, char **argv)
{
	int n;
    cout<<"Podaj liczbę"<<endl;
    cin>>n;
    
    
    fib_rek(n);
    
	return 0;
}

