/*
 * funkcje.cpp
 */


#include <iostream>
using namespace std;
void sumuj(int a, int b) //w funkcjii zawsze nawiasy () , funkcja do działania potrzebuje dwóch zmiennych całkowitych o nazwie a i b, zmienne nazywamy jak chcemy i są całkiem inne niż w int ai int b 
{
    cout << "Suma: "<< a + b << endl; //nazwa parametru fukcji taka sama jak przy void sumuj 
    
}

void odejmij(int a, int b) //w funkcjii zawsze nawiasy () , funkcja do działania potrzebuje dwóch zmiennych całkowitych o nazwie a i b, zmienne nazywamy jak chcemy i są całkiem inne niż w int ai int b 
{
    cout << "Różnica: "<< a - b << endl;
}

void mnozenie(int a, int b) //w funkcjii zawsze nawiasy () , funkcja do działania potrzebuje dwóch zmiennych całkowitych o nazwie a i b, zmienne nazywamy jak chcemy i są całkiem inne niż w int ai int b 
{
    cout << "Iloczyn: "<< a * b << endl; //nazwa parametru fukcji taka sama jak przy void sumuj 
    
}

void podziel(int a, int b) //w funkcjii zawsze nawiasy () , funkcja do działania potrzebuje dwóch zmiennych całkowitych o nazwie a i b, zmienne nazywamy jak chcemy i są całkiem inne niż w int ai int b 
{
    if 
    cout << "Iloraz "<< a / b << endl; //nazwa parametru fukcji taka sama jak przy void sumuj 
    
    cout <<"Nie dziel przez 0 !"<<endl;
    
}
    
int main(int argc, char **argv)

{
	int a,b ;
    cout <<"Podaj liczby";
    cin >> a >> b;
   
    sumuj (a,b);//te zmienne są całkiem w innym miejscu niż te z void
    odejmij (a,b);
    mnozenie (a,b);
    podziel (a,b);
     
	return 0;
}

