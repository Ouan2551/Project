#include <bits/stdc++.h>
using namespace std;
int main()
{
    ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    int a[9] = {0}, sum = 0;
    for (int i = 0; i < 9; i++)
    {
        cin >> a[i]; sum += a[i];
    }
    for (int i = 0; i < 9; i++)
    {
        for (int j = i + 1; j < 9; j++)
        {
            if (sum - 100 == a[i] + a[j])
            {
                for (int k = 0; k < 9; k++)
                {
                    if (k == i || k == j)
                    {
                        continue;
                    }
                    cout << a[k] << endl;
                }
                return 0;
            }
        }
    }
    return 0;
}