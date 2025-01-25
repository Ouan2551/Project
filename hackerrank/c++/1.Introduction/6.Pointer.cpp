#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    int a, b; cin >> a >> b;
    cout << a+b << endl;
    if (a-b < 0)
    {
        cout << -(a-b);
    }
    else
    {
        cout << a-b;
    }
    return 0;
}