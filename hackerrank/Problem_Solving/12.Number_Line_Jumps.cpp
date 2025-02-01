#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'kangaroo' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts following parameters:
 *  1. INTEGER x1
 *  2. INTEGER v1
 *  3. INTEGER x2
 *  4. INTEGER v2
 */
// x1 and v1 is first position and speed kangaroo1
// x2 and v2 is second position and speed kangaroo2
string kangaroo(int x1, int v1, int x2, int v2) {
    string can_do = "";
    // just chk x1 v1 x2 v2 normal
    if (x1 > x2 && v1 > v2)
    {
        can_do = "NO";
    }
    else if (x2 > x1 && v2 > v1)
    {
        can_do = "NO";
    }
    // use loop check
    else
    {
        int time1, time2;
        while (x1 != x2)
        {
            x1 += v1; x2 += v2; time1++; time2++;
            if (x1 == x2 && time1 == time2)
            {
                can_do = "YES";
            }
            else if (x1 != x2 || time1 != time2)
            {
                can_do = "NO";
            }
        }
        // loop check overthere
    }
    return can_do;
}

int main()
{
    ios::sync_with_stdio(0);cout.tie(0);cin.tie(0);
    ofstream fout(getenv("OUTPUT_PATH"));

    string first_multiple_input_temp;
    getline(cin, first_multiple_input_temp);

    vector<string> first_multiple_input = split(rtrim(first_multiple_input_temp));

    int x1 = stoi(first_multiple_input[0]);

    int v1 = stoi(first_multiple_input[1]);

    int x2 = stoi(first_multiple_input[2]);

    int v2 = stoi(first_multiple_input[3]);

    string result = kangaroo(x1, v1, x2, v2);

    fout << result << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}
