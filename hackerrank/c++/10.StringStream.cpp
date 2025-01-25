#include <bits/stdc++.h>
using namespace std;
int main()
{
    ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    string txt = ""; cin >> txt; int m = txt.size();
    vector <int> number;
    for (int i = 0; i <= m - 1; i++)
    {
        if (txt[i] == ',')
        {
            continue;
        }
        number[i] = number[i - 1] + txt[i];
    }
    int n = number.size();
    for (int i = 0; i <= n; i++)
    {
        cout << number[i] << endl;
    }
    return 0;
}