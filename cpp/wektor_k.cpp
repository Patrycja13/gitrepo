/*
 * wektor_k.cpp
 */

#include <iostream>
using namespace std;

class Wektor {
    private:
         double x;
         double y;
         int nrw;
    public:
        Wektor(int); // konstruktor
        void pobierz();
        void wypisz();
        friend Wektor dodaj(Wektor, Wektor);// funkcja zaprzyjazniona , funkcja działająca na kilku obiektach 
        
};

Wektor::Wektor(int nr){
    x = y = 0;
    nrw = nr;
    
    
} 
void Wektor::pobierz() {

    cout << "Podaj wsþółrzędne "<< nrw << " wektora " << endl;
    cin >> x;
    cin >> y;
}

void Wektor::wypisz() {
        cout << "Wektor nr "<< nrw << ": ";
        cout<< "[" << x << "," << y << "]"<< endl;

        

}

Wektor dodaj(Wektor w1, Wektor w2) {// funkcja zaprzyjaźniona nie jest częścią klasy 
    Wektor w3 = Wektor(3);
    w3.x = w1.x + w2.x;
    w3.y = w1.y + w2.y;
    return w3;
} 

int main(int argc, char **argv)
{
    // Wektor w1, w2;
    // w1.x = 10 // jeśli do składowych klasy 
    Wektor w1 = Wektor(1);
    Wektor w2 = Wektor(2);
    Wektor w3 = Wektor(3);
	w1.pobierz();
	w2.pobierz();
    w1.wypisz();
    w2.wypisz();
    w3 = dodaj(w1, w2);
    w3.wypisz();
	return 0;
}

