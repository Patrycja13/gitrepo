/*
 * tablice.cpp
 * 
 */


#include <iostream>


using namespace std;
void wprowadz(float tb[], int ile){
    cout << "Podaj oceny "<< endl;
    for (int i=0; i<ile; i++) {
        cin >> tb[i];
    }

}
void drukuj(float tb[], int ile) {
    cout << "Podane oceny "<< endl;
    for (int i=0; i<ile; i++){
        cout << tb[i] << " ";    
    }
    cout << endl;
}    
int tab1W(){
    float *tab = NULL;
    int ile;
    cout << "Ile podasz ocen ? "<< endl;
    cin >> ile; 
    ile = 5; // na jedną zmienna float 4 komórki pamięci, skoro ile = 5 to 20 komórek
    try {
        tab = new float [ile];
    } catch(bad_alloc) {
        cout<<"Za mało pamięci" ;
        return 1;
        
    }
    
    wprowadz(tab, ile);
    drukuj(tab, ile);
    return 0;
}

void wypelnij2W(int *tb[], int w, int k){
    srand(time(NULL));
    for (int i=1; i<w; i++){
        for (int j=1; j<k; j++){
            tb[i][j]= rand() % 101 ; // losowanie l;iczb od 0 do 100    
        
        }
    }
    
}

void drukuj2W(int *tb[], int w, int k){

    for(int i=1;i<w;i++){
        for(int j=1;j<k;j++){
       cout<<tb[i][j]<<" " <<endl;
    }
    cout << endl;
  }
}

int tab2W(){
    int w, k;
    cout<< "Podaj liczbę wierszy i kolumn"<< endl;
    cin >> w >> k;
    
    int **tab; // wskaznik dla wskaznika 
    try {
        tab = new int *[w]; // z * bo wartości szesnastkowe, alokowanie tablicy wskazników
    } catch(bad_alloc) {
        cout<<"Za mało pamięci" ;
        return 1;
        
    }
    for (int i=0; i<w; i++){
        try {
            tab[i] = new int[k]; // alokowanie tablicy liczb całkowitych
        } catch(bad_alloc) {
            cout<<"Za mało pamięci" ;
            return 1;
        
        }
    }
    
    wypelnij2W(tab, w, k);
    drukuj2W(tab, w, k);
    return 0;
}

int main(int argc, char **argv)
{
	//tab1W();
    tab2W();
	return 0;
}

