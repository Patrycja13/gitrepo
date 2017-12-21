/*
 * sort_bubble.cpp
 *
 * 
 */


#include <iostream>

using namespace std;

void wypelnij(int t[], int n, int max)
{
	// srand(time(NULL)); //inicjacja generatora liczb pseudolosowych
	for ( int i = 0; i < n; i++) 
    {   
        t[i] = rand()% max+1; // funkcja losująca liczbę
    }
}

void drukuj(int t[], int n)
{
	for ( int i = 0; i < n; i++) 
    {   
        cout << t[i] << " ";
    }
    cout << endl;
}

void zamien(int &a, int &b)
{
    int tmp = a;
    a = b;
    b = tmp;
}

void sort_bubble(int tab[], int n)
{
    // selection sort
    cout << " ------------- Sortowanie przez bąbelkowanie ---------------" << endl;
    for (int i = 0;i < n; i++){
        for (int j = 0; j < n - 1 - i; j++){
            if(tab[j]>tab[j+1])
                zamien(tab[j], tab[j + 1]);
            }
        }
}


int main(int argc, char **argv)
{
    int ile = 10;
    int tab[ile];
    wypelnij(tab, ile, 20);
	drukuj(tab, ile);
    sort_bubble(tab, ile);
    drukuj(tab, ile);
    return 0;
}
