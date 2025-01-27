#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'miniMaxSum' function below.
 *
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

void miniMaxSum(vector<int> arr) {
    int m = arr.size(), count = 0;
    long long sum = 0;
    vector<long long> sum_all(5);
    // check all member is not all same
    for (int i = 0; i < m; i++)
    {
        if (arr[0] == arr[i])
        {
            count++;
        }
    }
    if (count == 1)
    {
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < m; j++)
            {
                if (arr[j] == arr[i])
                {
                    continue;
                }
                else
                {
                    sum += arr[j];
                }
                sum_all[i] = sum;
            }
            sum = 0;
        }
        
        // find min max value
        long long min_value = LONG_LONG_MAX, max_value = LONG_LONG_MIN;
        for (int i = 0; i < m; i++)
        {
            min_value = min(min_value, sum_all[i]);
        }
        for (int i = 0; i < m; i++)
        {
            max_value = max(max_value, sum_all[i]);
        }
        cout << min_value << ' ' << max_value;
        }
    else
    {
        cout << arr[0] + arr[0] + arr[0] + arr[0]
        << ' ' << arr[0] + arr[0] + arr[0] + arr[0];
    }

}

int main()
{
    ios::sync_with_stdio(0);cout.tie(0);cin.tie(0);
    string arr_temp_temp;
    getline(cin, arr_temp_temp);

    vector<string> arr_temp = split(rtrim(arr_temp_temp));

    vector<int> arr(5);

    for (int i = 0; i < 5; i++) {
        int arr_item = stoi(arr_temp[i]);

        arr[i] = arr_item;
    }

    miniMaxSum(arr);

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
