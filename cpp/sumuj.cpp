/*
 * petla_for.cpp
 * Program pobiera i sumuje 10 liczb, wynik drukuje na ekranie
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{

   int suma=0 ;
   int a,b,c,d,e,f,g,h,j,k;
   
    cout<<"Podaj a :";cin>>a;
    cout<<"Podaj b :";cin>>b;
    cout<<"Podaj c :";cin>>c;
    cout<<"Podaj d :";cin>>d;
    cout<<"Podaj e :";cin>>e;
    cout<<"Podaj f :";cin>>f;
    cout<<"Podaj g :";cin>>g;
    cout<<"Podaj h :";cin>>h;
    cout<<"Podaj j :";cin>>j;
    cout<<"Podaj k :";cin>>k;
    
for (int i=10; i<11; i++) suma = suma +1 ;

cout << "Suma :"<< a+b+c+d+e+f+g+h+j+k ;


    return 0;
}

