#include <bits/stdc++.h>
using namespace std;
int main()
{
    ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    int n1 , n2, divide; n1 = n2 = divide = 0;
    vector<int> numbers;
    cout << "type range number overthere" << endl;
    cin >> n1; cin >> n2;
    cout << "type number you want to divide" << endl;
    cin >> divide;
    for (int i = n1; i <= n2; i++)
    {
        if (i % divide == 0)
        {
            numbers.push_back(i);
        }
    }
    int m = numbers.size(), round = 0;
    for (int i = 0; i < m; i++)
    {
        cout << numbers[i] << " "; round++;
        if (round == 10)
        {
            cout << endl; round = 0;
        }
    }
    return 0;
}