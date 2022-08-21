#include <iostream>
#include <vector>

// Utils functions
#include "headers/utils.h"

int main()
{
    // Checking if the header utils file works
    float a[] = {1, 2, 3};
    float b[] = {1, 4, 3};

    float d = distance(a, b);
    std::cout << "Distance: " << d << "\n";

    // Translation check
    std::vector<std::vector<int>> vect = get_translation_matrix<int>(1, 2, 3);
    for (int i = 0; i < vect.size(); i++)
    {
        for (int j = 0; j < vect[i].size(); j++)
        {
            std::cout << vect[i][j] << " ";
        }
        std::cout << "\n";
    }

    return 0;
}
