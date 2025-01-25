#include <bits/stdc++.h>
using namespace std;
int main()
{
    ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    //INPUT ax^2 + bx + c OUTPUT value of x
    string formula; getline(cin, formula); int m = formula.size();
    vector<char> txt; char a, b, c;
    for (int i = 0; i < m; i++)
    {
        txt.push_back(formula[i]);
    }

    // clear space bar in this vector
    for (int i = 0; i < m; i++)
    {
        if (txt[i] == ' ')
        {
            
        }
        
    }
    

    //find a
    for (int i = 0; i < m; i++)
    {
        if (txt[i] == 'x' && txt[i+1] == '^' && txt[i+2] == '2')
        {
            a = txt[0];
            cout << "a" << endl;
        }
    }

    //find b
    for (int i = 0; i < m; i++)
    {
        if (txt[i] == 'x' && txt[i+1] != '^' && txt[i+2] != '2')
        {
            b = txt[i-1];
            cout << "b" << endl;
        }
        
    }

    //ax^2 + bx + c
    //find c
    for (int i = 0; i < m; i++)
    {
        int chk_plus = 0;
        if (txt[i] == '+')
        {
            chk_plus++;
            if (chk_plus == 2)
            {
                c = txt[13];
            }
            
        }
    }
    
    cout << "a : " << a << endl;
    cout << "b : " << b << endl;
    cout << "c : " << c << endl;
    return 0;
}

//idea
//have mode select real number and complex numbers