/*
 * pierw_zloz.cpp
 * 
 * 
 */


#include <iostream>
using namespace std;
int main(int argc, char **argv)
{
	int n = 0;
    cout<<"Podaj liczbe: "<<endl;
    cin>>n;
    
    int i = 2;
    while(n % i != 0){
        if(i*i >= n)
            {
                cout<<"Liczba pierwsza "<<endl;
                break;
            }
                i++;
        }
    
    if(n%i == 0){
        cout<<"Liczba złożona"<<endl;
    }
	return 0;
}

