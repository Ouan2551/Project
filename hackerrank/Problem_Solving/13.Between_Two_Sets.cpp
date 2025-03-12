#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'getTotalX' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY a
 *  2. INTEGER_ARRAY b
 */

int getTotalX(vector<int> a, vector<int> b)
{
    int a_size = a.size(), b_size = b.size();
    // find min vector b
    int min_b = INT_MAX;
    for (int i = 0; i < b_size; i++)
    {
        min_b = min(min_b, b[i]);
    }
        
    // b zone
    vector<int> b_divisible;
    for (int i = 2; i <= min_b; i++)
    {
        int count = 0;
        for (int j = 0; j < b_size; j++)
        {
            if (b[j] % i == 0)
            {
                count++;
            }
            else
            {
                count = 0;
            }
        }
        if (count == b_size)
        {
            b_divisible.push_back(i);
        }
    }

    int count = 0, b_divisible_size = b_divisible.size();
    // check
    // for (int i = 0; i < b_divisible_size; i++)
    // {
    //     cout << b_divisible[i] << '\n';
    // }

    // a zone
    // check a[m] to main loop
    int count_chk = 0;
    for (int i = 0; i <= b_divisible_size; i++)
    {
        int j = 1;
            for (int m = 1; m <= a_size; m++)
            {
                if (a[m] * j == b_divisible[i])
                {
                    count++;
                    cout << "a[m] * j => " << a[m] * j << '\n';
                    cout << "b_divisible[i]" << b_divisible[i] << '\n';
                    cout << "chk : " << count << '\n';
                    cout << "__________________" << '\n';
                }
            }
            if (count == a_size)
            {
                count_chk++; count = 0; 
            }
            count = 0;
        j++;
    }
    cout << "count_chk : " << count_chk;
    return count_chk;
}

int main()
{
    ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    ofstream fout(getenv("OUTPUT_PATH"));

    string first_multiple_input_temp;
    getline(cin, first_multiple_input_temp);

    vector<string> first_multiple_input = split(rtrim(first_multiple_input_temp));

    int n = stoi(first_multiple_input[0]);

    int m = stoi(first_multiple_input[1]);

    string arr_temp_temp;
    getline(cin, arr_temp_temp);

    vector<string> arr_temp = split(rtrim(arr_temp_temp));

    vector<int> arr(n);

    for (int i = 0; i < n; i++) {
        int arr_item = stoi(arr_temp[i]);

        arr[i] = arr_item;
    }

    string brr_temp_temp;
    getline(cin, brr_temp_temp);

    vector<string> brr_temp = split(rtrim(brr_temp_temp));

    vector<int> brr(m);

    for (int i = 0; i < m; i++) {
        int brr_item = stoi(brr_temp[i]);

        brr[i] = brr_item;
    }

    int total = getTotalX(arr, brr);

    fout << total << "\n";

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
