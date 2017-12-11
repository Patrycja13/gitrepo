/*
 * Gawel_dzielniki.cpp
 * 
 * Copyright 2017  <>

 */


#include <iostream>
using namespace std;
int main(int argc, char **argv)
{
	int x;
    
    cout << "Podaj wartość";
    cin >> x;
    
    cout<<"Dzielniki liczby "<< x << "wynoszą ";
    
    for (int i=x;i>0;i-- )
    {
        if (x % i ==0)
        cout << x /i<< " ";
    }
	return 0;
}

