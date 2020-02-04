/* Rotate nxn 90 degrees */

#include <iostream>

std::vector<std::vector<int>> rotateImage(std::vector<std::vector<int>> a) {
    size_t n = a.size() - 1;
    if (n == 0)
    {
        return a;
    }

    for (int i=0; i < n; i++)
    {
        for (int j=i; j < (n - i); j++)
        {
            int tmp = a[i][j];
            // move bottom left to up left
            a[i][j] = a[n-j][i];

            // move bottom right to bottom left
            a[n-j][i] = a[n-i][n-j];
            
            // move up right to bottom left
            a[n-i][n-j] = a[j][n-i];

            // move up left to up right
            a[j][n-i] = tmp;
        }
    }

    return a;
}
