#include <bits/stdc++.h>
using namespace std;
int main()
{
    ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    int term1, term2; int num_term1, num_term2;
    cout << "how to type" << endl;
    cout << "(term)" << "  " << "(numbers in this terms)" << endl;
    cin >> term1 >> num_term1;
    cin >> term2 >> num_term2;
    double d = (num_term2 - num_term1)/((term2 - 1) - (term1 - 1));
    double a1 = num_term1 - (term1 - 1)*(d);
    cout << "a(n) = " << a1 << " + " << "(n - 1)" << d;
    return 0;
}