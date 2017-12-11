/*
 * algorytm.cpp
 * 
 */


#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
	int n,a;
    int iloczyn = 1;
    int i = 1;
    cout<<"Podaju n: "<< endl;
    cin >> n;
    while (i != n)
    {
        cout<<"Podaj a"<< endl;
        cin>>a;
        iloczyn = iloczyn*a ;
        i++;
    }
    
    cout<<"Wynik"<< iloczyn <<endl;
    
	return 0;
}

