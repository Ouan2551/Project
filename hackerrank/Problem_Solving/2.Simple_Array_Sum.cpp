#include <bits/stdc++.h>
using namespace std;
int main()
{
    ios::sync_with_stdio(0);cout.tie(0);cin.tie(0);
    int size; cin >> size; int a[size] = {0}, sum = 0;
    for (int i = 0; i < size; i++)
    {
        cin >> a[i]; sum += a[i];
    }
    cout << sum;
    return 0;
}