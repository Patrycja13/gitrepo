/*
 * wskazniki.cxx
 * 
 * 
 */


#include <iostream>
using namespace std;

int main(int argc, char **argv)
{   
    int roz = 20;
    int tab [roz];
    int *wsk1; // zmienna wskaznikowa z *,  zawiera adresy komórek w pamięci
    wsk1 = tab ; //  bez & bo nazwa tablicy jest wskaźnikiem a nie zwykłą zmienną
    

    cout << tab << endl;
    cout << wsk1 << endl;
    tab[0]= 10 ;
    *wsk1 = 10; // nazwa tablicy wskaznikiem do pierwszej komórki 
    wsk1++; // wskazuje następną komórkę tablicy bo po 4 większe xddddd 
    *wsk1 = 12;
	return 0;
}

