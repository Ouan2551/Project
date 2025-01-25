#include <bits/stdc++.h>
using namespace std;
int main()
{
    ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    
    // setup zone
    string txt[2] = {""};
    for (int i = 0; i < 2; i++)
    {
        cin >> txt[i];
    }

    // character zone
    int size_1 = txt[0].size(), size_2 = txt[1].size();
    int size[2] = {size_1, size_2}; vector <char> all_consonant;
    char first[2];

    //add all consonant
    for (int i = 0; i < 2; i++)
    {
        string txt_use = txt[i];
        first[i] = txt_use[0];
        for (int j = 0; j < size[i]; j++)
        {
            all_consonant.push_back(txt_use[j]);
        }
    }

    // output
    cout << size[0] << " " << size[1] << endl;
    for (int i = 0; i < size[0] + size[1]; i++)
    {
        cout << all_consonant[i];
    }
    cout << endl;

    for (int i = 0; i < 2; i++)
    {
        string txt_use = txt[i];
        cout << first[1-i];
        for (int j = 1; j < size[i]; j++)
        {
            cout << txt_use[j];
        }
        cout << " ";
    }
    return 0;
}