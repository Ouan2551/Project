#include <iostream>
#include <vector>
int main()
{
    std::ios::sync_with_stdio(0);std::cin.tie(0);std::cout.tie(0);
    int rows, columns, determinant_value; std::cin >> rows >> columns; 
    std::vector<std::vector<int>> matrix(rows, std::vector<int>(columns));
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < columns; j++)
        {
            std::cin >> matrix[i][j];
        }
    }
    int check_count = rows, check_all = rows*2, x = 0, y = 0, dx = 1, dy = 1;
    for (int i = 0; i < check_all; i++)
    {
        int multiply = 1;
        for (int j = 0; j < check_count; j++)
        {
            multiply *= matrix[x][y]; x += dx; y += dy;
            if (x >= rows)
            {
                x -= rows;
            }
            else if (y > rows)
            {
                y -= rows;
            }
        }
        if (i < rows)
        {
            determinant_value += multiply;
        }
        else
        {
            determinant_value -= multiply;
        }
    }
    std::cout << "determinant_value : " << determinant_value << '\n';
    // for (int i = 0; i < rows; i++)
    // {
    //     for (int j = 0; j < columns; j++)
    //     {
    //         std::cout << matrix[i][j] << ' ';
    //     }
    //     std::cout << '\n';
    // }
    return 0;
}