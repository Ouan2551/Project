#include <bits/stdc++.h>
using namespace std;
int array1(int array_index, int a[])
{
    int num = a[array_index];
    return num;
}
int array2(int array_index, int b[])
{
    int num = b[array_index];
    return num;
}
int main()
{
    ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    int n, q, k, m; cin >> n >> q; cin >> k; int a[k];
    for (int i = 0; i < k; i++)
    {
        cin >> a[i];
    }
    cin >> m; int b[m];
    for (int i = 0; i < m; i++)
    {
        cin >> b[i];
    }
    int select_array1, array_index1,select_array2, array_index2;
    cin >> select_array1 >> array_index1 >> select_array2 >> array_index2;

    if (select_array1 == 0)
    {
        cout << array1(array_index1, a) << endl;
    }
    else if (select_array1 == 1)
    {
        cout << array2(array_index1, b) << endl;
    }
    if (select_array2 == 0)
    {
        cout << array1(array_index2, a) << endl;
    }
    else if (select_array2 == 1)
    {
        cout << array2(array_index2, b) << endl;
    }
    return 0;
}

// Sample Input

// 2 2 (i,j)
// 3 ,1 5 4 (size_array1, number contain in arrays1)
// 5 ,1 2 8 9 3 (size_array2, number contain in arrays2)
// 0 ,1 (select array1, find character is index equal this number)
// 1 ,3 (select array2, find character is index equal this number)