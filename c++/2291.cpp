#include <bits/stdc++.h>
using namespace std;

long long int s[1000006];

int main()
{
    long int i, j, x = 0;

    s[0] = 0;
    for (i = 1; i < 1000006; i++)
    {
        for (j = i; j < 1000006; j += i)
        {
            s[j] += i;
        }
        s[i] += s[i - 1];
    }

    while (1)
    {
        cin >> x;
        if (x == 0)
        {
            break;
        }
        else
        {
            cout << s[x] << endl;
        }
    }
}