#include <bits/stdc++.h>
using namespace std;

int input_index(void)
{
    cout << "Select location you want to place : ";
    int index; cin >> index; return index;
}

// index can not replacement
int check_index_used(int index)
{
    vector<int> index_used;
    for (int i = 0; i < 9; i++)
    {
        if (index == index_used[i])
        {
            cout << "You can not use same location" << endl;
            index = input_index(); index = check_index_used(index);
            break;
        }
        else if (index < 1 || index > 9)
        {
            cout << "Please type correct location" << endl;
            index = input_index(); index = check_index_used(index);
            break;
        }
        else
        {
            index_used.push_back(index);
        }
    }
    return index;
}

void output_tic_tac_toe(int index, char a[], char used)
{
    a[index - 1] = used;

    for (int i = 1; i <= 9; i = i + 3)
    {
        cout << a[i] << "|" << a[i+1] << "|" << a[i+2] << endl;
    }
    cout << endl;
}

int main()
{
    ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

    // use interface section
    cout << "TIC-TAC-TOE Game 2 player" << endl;
    cout << "Number showing on screen use for location you want to place x or o" << endl;
    cout << "Example    " ;
    cout << "1  |  2  |  3" << endl;
    cout << "           4  |  5  |  6" << endl;
    cout << "           7  |  8  |  9" << endl; cout << endl;
    cout << "**************************************************************" << endl;

    // section input from user
    int index = 0; char a[9] = {'1','2','3','4','5','6','7','8','9'};
    char used;
    for (int i = 1; i <= 9; i++)
    {
        // for user interface
        if (i % 2 == 1)
        {
            cout << "Player 1 : "; used = 'X';
        }
        else
        {
            cout << "Player 2 : "; used = 'O';
        }
        index = input_index(); index = check_index_used(index);
        output_tic_tac_toe(index, a, used);
    }
    
    return 0;
}

//this version start from player 1 only