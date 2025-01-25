#include <bits/stdc++.h>
using namespace std;
int main()
{
    //int, long, char, float, and double
    ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    int num; cin >> num;
    if (num >= 1 && num <= 9) {
        if (num == 1) {
            cout << "one";
        }
        if (num == 2) {
            cout << "two";
        }if (num == 3) {
            cout << "three";
        }if (num == 4) {
            cout << "four";
        }if (num == 5) {
            cout << "five";
        }if (num == 6) {
            cout << "six";
        }if (num == 7) {
            cout << "seven";
        }if (num == 8) {
            cout << "eight";
        }if (num == 9) {
            cout << "nine";
        }
    } else {
    cout << "Greater than 9";
    }
    return 0;
}