#include <bits/stdc++.h>
using namespace std;
int main()
{
    ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    int count; cin >> count; int a[count] = {0};
    for (int i = 0; i < count; i++)
    {
        cin >> a[i];
    }
    for (int i = count - 1; i >= 0; i--)
    {
        cout << a[i] << " ";
    }
    return 0;
}