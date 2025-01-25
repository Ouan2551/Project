#include <bits/stdc++.h>
using namespace std;
int main()
{
    ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    int a, b; cin >> a >> b;
    if (a < b)
    {
        for (int i = a; i <= b; i++)
        {
            if(i == 1)
            {
                cout << "one" << "\n";
            }
            if (i == 2)
            {
                cout << "two" << "\n";
            }
            if (i == 3)
            {
                cout << "three" << "\n";
            }
            if (i == 4)
            {
                cout << "four" << "\n";
            }
            if (i == 5)
            {
                cout << "five" << "\n";
            }
            if (i == 6)
            {
                cout << "six" << "\n";
            }
            if (i == 7)
            {
                cout << "seven" << "\n";
            }
            if (i == 8)
            {
                cout << "eight" << "\n";
            }
            if (i == 9)
            {
                cout << "nine" << "\n";
            }
            if (i > 9 && i % 2 == 0)
            {
                cout << "even" << "\n";
            }
            if (i > 9 && i % 2 == 1)
            {
                cout << "odd" << "\n";
            }
        }
    }
    return 0;
}