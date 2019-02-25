/*
 * wskazniki.cxx
 * 
 * 
 */


#include <iostream>
using namespace std;

int main(int argc, char **argv)
{   
    int i = 13;
    double y = 10;
    int *wsk1; // zmienna wskaznikowa z *,  zawiera adresy komórek w pamięci
    double *wsk2; 
    wsk1 = &i; // inicjacja wskaznikowa
    cout << i << endl;
    cout << wsk1 << endl;
    cout << &i << endl;
    *wsk1 += 1; // gwiazdka aby odcztywać wartość wskaznika
    cout << *wsk1 << endl; // 
    wsk1 += 1;
    cout << wsk1 << endl;
    
    cout << sizeof(i) << endl; // typ int zajmuje 4 bajty więc dodaje wartość 4 
	cout << sizeof(y) << endl;
	return 0;
}

