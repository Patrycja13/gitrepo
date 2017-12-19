/*
 * sort_bubble.cpp
 *
 * 
 */


#include <iostream>

using namespace std;

void wypelnij(int t[], int n, int maks)
{
    srand(time(NULL)); //inicjacja generatora liczb pseudolosowych
    for(int i = 0; i < n; i++){
        t[i] = 1 + rand() % maks; // losowanie liczb czałowitych >0 
        }
}

void drukuj(int t[], int n)
{
    for(int i = 0; i < n; i++){
        cout << t[i]<<" ";
        }
    cout << endl;
}
void zamien(int &a, int &b){
 
    }
    
void sort_wyb(int t[], int n){
    cout << "-----------sortowanie przez wybieranie------------"<<endl;
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n - 1 - i ; j++){ // n-1-i żeby indeks nie dochodził do elementów już uporządkowanych 
            if (t[j]<t[k])
            zamien (tab[j]>tab[j+1]);
        }
    }
}

int main(int argc, char **argv)
{
	const int ile = 10;
    int tab[ile];
    wypelnij(tab, ile, 20);
    drukuj(tab, ile);
    sort_wyb(tab, ile);
    drukuj(tab, ile);
	return 0;
}
