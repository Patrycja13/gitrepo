/*
 * sort_wstaw.cpp
 * 
 */


#include <iostream>

void sort_wstaw(int lista[], int n)
{
    int el = 0;
    int k = 0;
    
    for(int i=1;i<n;i++)
    {
        el = lista[i];
        k = i - 1;
        
        while (k>=0 && lista[k] > el)
        {
            lista[k+1] = lista[k];
            k--;
        }
        lista[k+1] = el;
    }
    
    
}

void drukuj(int t[], int n)
{
    for(int i=0; i<n; i++)
    {
        cout<<t[i];
    }
}

int main(int argc, char **argv)
{
    int ile = 7;
    int lista[ile];
    
    lista[0]= 7; 
    lista[1]= 1; 
    lista[2]= 8; 
    lista[3]= 3; 
    lista[4]= 0; 
    lista[5]= 2; 
    lista[6]= 6;
	

    cout<<"Lista "<<lista[i]<<endl;
    
    cout<<"Posortowane: "<<drukuj(t[], n)<<endl;
    
    sort_wstaw(lista, ile);
    drukuj(lista,ile);
	return 0;
}

