#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    string txt;
    cin >> txt;

    // Create a string stream to parse the input string
    stringstream ss(txt);
    string temp;

    // Read numbers separated by commas and store them in a vector
    vector<int> numbers;
    while (getline(ss, temp, ',')) {  // Use ',' as the delimiter
        numbers.push_back(stoi(temp));  // Convert the substring to an integer
    }

    // Print the extracted numbers
    for (int number : numbers) {
        cout << number << endl;
    }

    return 0;
}