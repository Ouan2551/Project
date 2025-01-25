#include <iostream>
#include <vector>
using namespace std;
int main()
{
    // first line
    int n, q;
    cin >> n >> q;
    
    vector<vector<int>> arrays(n);
    for (int i = 0; i < n; i++)
    {
        int k;
        cin >> k;
        arrays[i].resize(k);
        for (int j = 0; j < k; j++)
        {
            cin >> arrays[i][j];
        }
    }
    for (int query = 0; query < q; query++)
    {
        int i, j;
        cin >> i >> j;
        cout << arrays[i][j] << endl;
    }
    return 0;
}