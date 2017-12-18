/*
 * ciag.cpp
 */


#include <iostream>

int wyraz(int a, int b)
{
     if(n==1)
         return 2;
      return ciag(n -1) * ciag (n * n) + 1
}  
int main(int argc, char **argv)
{
    int n=0;
	cout<<"Podaj 2 liczbe: ";
    cin>>n;
    cout<<wyraz(n);
    
	return 0;
}

