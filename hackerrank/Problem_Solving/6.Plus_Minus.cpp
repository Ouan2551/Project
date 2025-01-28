#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'plusMinus' function below.
 *
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

void plusMinus(vector<int> arr) {
    double m = arr.size(), positive_count, negative_count, zero_count;
    positive_count = negative_count = zero_count = 0;
    double result1, result2, result3; result1 = result2 = result3 = 0.000000;
    for (int i = 0; i < m; i++)
    {
        if (arr[i] > 0)
        {
            positive_count++;
        }
        else if (arr[i] < 0)
        {
            negative_count++;
        }
        else if (arr[i] == 0)
        {
            zero_count++;
        }
    }
    result1 = positive_count/m; result2 = negative_count/m; result3 = zero_count/m;
    cout << fixed << setprecision(6) << result1 << '\n';
    cout << fixed << setprecision(6) << result2 << '\n';
    cout << fixed << setprecision(6) << result3;
}

int main()
{
    ios::sync_with_stdio(0);cout.tie(0);cin.tie(0);
    string n_temp;
    getline(cin, n_temp);

    int n = stoi(ltrim(rtrim(n_temp)));

    string arr_temp_temp;
    getline(cin, arr_temp_temp);

    vector<string> arr_temp = split(rtrim(arr_temp_temp));

    vector<int> arr(n);

    for (int i = 0; i < n; i++) {
        int arr_item = stoi(arr_temp[i]);

        arr[i] = arr_item;
    }

    plusMinus(arr);

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
