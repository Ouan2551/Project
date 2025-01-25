#include <bits/stdc++.h>
using namespace std;

// Function to get valid input from the user
int input_index(set<int>& index_used) {
    int index;
    while (true) {
        cout << "Select location you want to place: ";
        cin >> index;

        // Validate input range
        if (index < 1 || index > 9) {
            cout << "Invalid location. Please choose a number between 1 and 9." << endl;
        }
        // Check if the location is already used
        else if (index_used.count(index)) {
            cout << "You cannot use the same location. Choose another." << endl;
        } else {
            break; // Valid input
        }
    }
    index_used.insert(index); // Mark the position as used
    return index;
}

// Function to display the tic-tac-toe board
void output_tic_tac_toe(char a[]) {
    for (int i = 0; i < 9; i += 3) {
        cout << " " << a[i] << " | " << a[i + 1] << " | " << a[i + 2] << endl;
        if (i < 6) cout << "---|---|---" << endl;
    }
    cout << endl;
}

int main() {
    ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

    // Introduction
    cout << "TIC-TAC-TOE Game (2 Players)" << endl;
    cout << "Use the numbers shown below to place your mark (X or O):" << endl;
    cout << " 1 | 2 | 3" << endl;
    cout << "---|---|---" << endl;
    cout << " 4 | 5 | 6" << endl;
    cout << "---|---|---" << endl;
    cout << " 7 | 8 | 9" << endl;
    cout << "*******************************************************" << endl;

    // Initialize the board and used indices
    char a[9] = {'1', '2', '3', '4', '5', '6', '7', '8', '9'};
    set<int> index_used; // To track used positions
    char used;

    // Game loop
    for (int turn = 1; turn <= 9; ++turn) {
        // Determine the current player
        if (turn % 2 == 1) {
            cout << "Player 1 (X): ";
            used = 'X';
        } else {
            cout << "Player 2 (O): ";
            used = 'O';
        }

        // Get a valid index from the player
        int index = input_index(index_used);

        // Update the board and display it
        a[index - 1] = used; // Adjust for 0-based indexing
        output_tic_tac_toe(a);
    }

    cout << "Game over! Thanks for playing." << endl;
    return 0;
}
