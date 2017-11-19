/*
 * nwm.cpp
 */


#include <iostream>
using namespace std;
int main(int argc, char **argv)
{
    int n=0;
    int m=0;
    cin >> n;
    cin >> m;
    cout <<" Podaj n " << n << endl;
    cout <<" Podaj m " << m << endl;
	
    for (int i=n ;i < m;i++)
    cout << " " << i << " ";
	return 0;
}

