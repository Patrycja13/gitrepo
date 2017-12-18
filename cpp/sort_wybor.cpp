/*
 * sort_wybor.cpp
 * 
 */


#include <iostream>
using namespace std;

void wypelnij(int t[], int n, int maks)
{
    srand(time(NULL)); // INICJACJA GENERATORA LICZB PSEUDOLOSOWYCH
    for(int i =0; i<n;i++)
        {
            t[i]=1+rand() % maks;// dzielimy modulo przez górną granicę... to losowanie liczb całkowitych z <0, max>
            
        }
}
void drukuj(int t[], int n, int maks)
{
    srand(time(NULL)); 
    for(int i =0; i<n;i++)
        {
            cout<<t[i]<<" ";
        }
    cout << endl;
}

void zamien(int&a, int&b)
{
    int tmp=a;
    a=b;
    b=tmp;
    
    
}
void sort_wybor(int t[], int n)
{
    cout<<"----- Sortowanie przez wybieranie-----"<<endl;
    int i, j, k;
    for (i=0; i<n; i++){
        k=1;
        for (j=i+1;j<n; j++){
            if (t[j]<t[k])
             k=j;
            
            }
            zamien(t[i], t[k]);
    }
}
    

int main(int argc, char **argv)
{
	const int ile = 10;
    int tab[ile];
    wypelnij(tab, ile, 20);
    drukuj(tab, ile);
    sort_wybor(tab, ile);
    drukuj(tab, ile);
	return 0;
}

