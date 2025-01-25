#include <bits/stdc++.h>
using namespace std;
int main()
{
    ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    int n = 0, q = 0; cin >> n >> q;
    int size1 = 0, size2 = 0, a[size1][size2] = {0};
    cin >> size1;
    for (int i = 0; i < size1; i++)
    {
        cin >> a[0][i];
    }
    cin >> size2;
    for (int i = 0; i < size2; i++)
    {
        cin >> a[1][i];
    }

    int select_array1 = 0, pointer1 = 0;
    cin >> select_array1; cin >> pointer1;

    int select_array2 = 0, pointer2 = 0;
    cin >> select_array2; cin >> pointer2;
    
    cout << a[select_array1][pointer1] << endl;
    cout << a[select_array2][pointer2] << endl;
    
    return 0;
}