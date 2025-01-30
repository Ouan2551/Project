#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the 'timeConversion' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

string timeConversion(string s) {
    // midnight to midday use a.m.
    // midday to midnight use p.m.
    int m = s.size();
    cout << "m : " << m;

    // p.m.
    if (s[8] == 'P')
    {
        // 00 - 09
        if (s[0] == '0')
        {
            if (s[1] == '0')
            {
            }
            else if (s[1] == '1')
            {
            }
            else if (s[1] == '2')
            {
            }
            else if (s[1] == '3')
            {
            }
            else if (s[1] == '4')
            {
            }
            else if (s[1] == '5')
            {
            }
            else if (s[1] == '6')
            {
            }
            else if (s[1] == '7')
            {
            }
            else if (s[1] == '8')
            {

            }
            else if (s[1] == '9')
            {
            }
        }
        // 10 - 12
        else if (s[0] == '1')
        {
            if (s[1] == '0')
            {

            }
            if (s[1] == '1')
            {

            }
            else if (s[1] == '2')
            {

            }
        }
    }

    // a.m.
    else if (s[8] == 'A')
    {
        // 00 - 09
        if (s[0] == '0')
        {
            if (s[1] == '0')
            {
            }
            else if (s[1] == '1')
            {
            }
            else if (s[1] == '2')
            {
            }
            else if (s[1] == '3')
            {
            }
            else if (s[1] == '4')
            {
            }
            else if (s[1] == '5')
            {
            }
            else if (s[1] == '6')
            {
            }
            else if (s[1] == '7')
            {
            }
            else if (s[1] == '8')
            {

            }
            else if (s[1] == '9')
            {
            }
        }
        // 10 - 12
        else if (s[0] == '1')
        {
            if (s[1] == '0')
            {

            }
            if (s[1] == '1')
            {

            }
            else if (s[1] == '2')
            {

            }
        }
    }
    string txt = "hh";
    return txt;
}

int main()
{
    ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    string result = timeConversion(s);

    fout << result << "\n";

    fout.close();

    return 0;
}
