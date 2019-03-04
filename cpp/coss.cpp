/*
 * coss.cpp
 * 
 * Copyright 2019  <>
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
 * 
 */


#include <iostream>
using namespace std;

int main()
{

    string s1;
    string samogloski= "aeiouy";
    int pozycja = 0;
    int suma = 0;
    int zmiana = 0;

    cout << "Podaj ciag znakow (maksymalnie 32 znaki):" << endl;
    getline(cin,s1);

    if (s1.size()>32)
    {
       cout << "Ciag znakow jest za dlugi. Podaj ciag znakow: " << endl;
       getline(cin,s1);
    }

    for (int i = 1 ; i <= samogloski.size() ; i++)
    {                     
        for (int j = 1; j <= s1.size() ; j++)
        {
            pozycja = s1.find(samogloski[i],pozycja) + 1;
            if (pozycja!=zmiana)
            { 
               zmiana = pozycja;
               suma++;
            } 

        }
        pozycja = 0;
    }

    cout << "W podanym ciagu znakow wystepuje " << suma << " samoglosek" << endl;

    system ("pause");
    return 0;
}
