/*
 * petle_cw7.cpp
 */


#include <iostream>
using namespace std;
int main(int argc, char **argv)
{
	int i=0;//numer miesiąca
    for (int i=0; i<=3 ; i++)
    {
    cout <<"Podaj numer miesiąca";
    cin >> i;
    if (i>0 && i<13) break;
    else cout <<"Błdne dane"<<endl;
        
        }
        switch (i)
        {
           case 1:
                cout<<"styczeń";
                break;
           case 2:
                cout<<"luty";
                break;
           case 3:
                cout<<"marzec";
                break;
           case 4:
                cout<<"kwiecień";
                break;
           case 5:
                cout<<"maj";
                break;
           case 6:
                cout<<"czerwiec";
                break;
           case 7:
                cout<<"lipiec";
                break;
           case 8:
                cout<<"sierpień";
                break;
           case 9:
                cout<<"wrzesień";
                break;
           case 10:
                cout<<"październik";
                break;
           case 11:
                cout<<"listopad";
                break;
           case 12:
                cout<<"grudzień";
                break;
            
            }
    
    
	return 0;
}

