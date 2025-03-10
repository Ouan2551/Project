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
    // p.m.
    if (s == "12:00:00AM")
    {
        s = "00:00:00"; return s;
    }
    
    if (s[8] == 'P')
    {
        s.erase(remove(s.begin(), s.end(), 'P'), s.end());
        s.erase(remove(s.begin(), s.end(), 'M'), s.end());
        
        // 00 - 09
        if (s[0] == '0')
        {
            if (s[1] == '0')
            {
                s[0] = '1'; s[1] = '2';
            }
            else if (s[1] == '1')
            {
                s[0] = '1'; s[1] = '3';
            }
            else if (s[1] == '2')
            {
                s[0] = '1'; s[1] = '4';
            }
            else if (s[1] == '3')
            {
                s[0] = '1'; s[1] = '5';
            }
            else if (s[1] == '4')
            {
                s[0] = '1'; s[1] = '6';
            }
            else if (s[1] == '5')
            {
                s[0] = '1'; s[1] = '7';
            }
            else if (s[1] == '6')
            {
                s[0] = '1'; s[1] = '8';
            }
            else if (s[1] == '7')
            {
                s[0] = '1'; s[1] = '9';
            }
            else if (s[1] == '8')
            {
                s[0] = '2'; s[1] = '0';
            }
            else if (s[1] == '9')
            {
                s[0] = '2'; s[1] = '1';
            }
        }
        // 10 - 12
        else if (s[0] == '1')
        {
            if (s[1] == '0')
            {
                s[0] = '2'; s[1] = '2';
            }
            if (s[1] == '1')
            {
                s[0] = '2'; s[1] = '3';
            }
            else if (s[1] == '2')
            {
                if (s[3] != '0' || s[4] != '0' || s[6] != '0' || s[7] != '0')
                {
                    return s;
                }
                // if (s[3] == '0' && s[4] == '0' && s[6] == '0' && s[7] == '0')
                // {
                //     s[0] = '0'; s[1] = '0'; return s;
                // }
                s[0] = '2'; s[1] = '4';
            }
        }
    }

    // a.m.
    else if (s[8] == 'A')
    {
        s.erase(remove(s.begin(), s.end(), 'A'), s.end());
        s.erase(remove(s.begin(), s.end(), 'M'), s.end());
        if (s[0] == '1' && s[1] == '2' && (s[3] != '0' || s[4] != '0'))
        {
            s[0] = '0', s[1] = '0';
        }
        return s;
        // // 00 - 09
        // if (s[0] == '0')
        // {
        //     if (s[1] == '0')
        //     {
        //     }
        //     else if (s[1] == '1')
        //     {
        //     }
        //     else if (s[1] == '2')
        //     {
        //     }
        //     else if (s[1] == '3')
        //     {
        //     }
        //     else if (s[1] == '4')
        //     {
        //     }
        //     else if (s[1] == '5')
        //     {
        //     }
        //     else if (s[1] == '6')
        //     {
        //     }
        //     else if (s[1] == '7')
        //     {
        //     }
        //     else if (s[1] == '8')
        //     {

        //     }
        //     else if (s[1] == '9')
        //     {
        //     }
        // }
        // // 10 - 12
        // else if (s[0] == '1')
        // {
        //     if (s[1] == '0')
        //     {

        //     }
        //     if (s[1] == '1')
        //     {

        //     }
        //     else if (s[1] == '2')
        //     {

        //     }
        // }
    }
    cout << s;
    return s;
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
