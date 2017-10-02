/*
 * petla_for.cpp
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int i ;
    for ( i = 1; i < 101; i+=2 ) 
        {//umieszczamy blok kodu który ma się powtarzać
           
            cout << '*' ;
            if ( i % 10 == 0 )
                
                {  
                for (j=0; j<9 ; j++)    
                cout << "#" ;
                cout << endl;
                }
            
            
       }
       
       
    return 0;
}

