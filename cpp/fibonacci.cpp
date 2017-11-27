/*
 * fibonacci.cpp
 *
 * 
 */


#include <iostream>
using namespace std;

void fib_iter(int n)
{
    int a=0;
    int b=1;
    
    for(int i=0;i<n;i++ )
    {
        a=b;
        a=a+b;
        }
    
}
int main(int argc, char **argv)
{
	int n;
    cout<<"Podaj liczbę"<<endl;
    cin>>n;
	return 0;
}

