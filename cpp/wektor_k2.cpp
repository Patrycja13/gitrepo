/*
 * wektor_k.cpp
 */

#include <iostream>
using namespace std;

class Wektor {
    protected: // pola nie są dziedziczone, to pola statyczne 
        
    
    private:
         double x;
         double y;

    public:
    static int nrw;
        Wektor();
        Wektor(int, int); // konstruktor
        void pobierz();
        void wypisz();
        friend Wektor dodaj(Wektor, Wektor);// funkcja zaprzyjazniona , funkcja działająca na kilku obiektach 
        friend Wektor iloczyn(Wektor, Wektor);
        
};

Wektor::Wektor(){
    x = y = 0;
    Wektor::nrw++;
}
Wektor::Wektor(int a, int b){
    x = a;
    y = b;
    Wektor::nrw++;
    
} 
void Wektor::pobierz() {

    cout << "Podaj wsþółrzędne "<< Wektor::nrw << " wektora " << endl;
    cin >> x;
    cin >> y;
}

void Wektor::wypisz() {
        cout << "Wektor nr "<< Wektor::nrw << ": ";
        cout<< "[" << x << "," << y << "]"<< endl;

        

}

Wektor dodaj(Wektor w1, Wektor w2) {// funkcja zaprzyjaźniona nie jest częścią klasy 
    Wektor w3 = Wektor();
    w3.x = w1.x + w2.x;
    w3.y = w1.y + w2.y;
    return w3;
} 

Wektor iloczyn(Wektor w1, Wektor w2) {// funkcja zaprzyjaźniona nie jest częścią klasy 
    Wektor w3 = Wektor();
    w3.x = w1.x * w2.x;
    w3.y = w1.y * w2.y;
    return w3;
} 

int Wektor::nrw = 0;

int main(int argc, char **argv)
{
    // Wektor w1, w2;
    // w1.x = 10 // jeśli do składowych klasy 
    Wektor w1 = Wektor(1, 5);
    w1.wypisz();
    Wektor w2 = Wektor(2, 4);
    w2.wypisz();
    Wektor w3 = iloczyn(w1, w2);
    w3.wypisz();
    cout << Wektor::nrw << endl;
	return 0;
}

