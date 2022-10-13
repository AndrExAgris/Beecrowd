#include <bits/stdc++.h>
using namespace std;

int main()
{

    int x;

    cin >> x;

    while(x != 0)
    {
        int y, j, count = 0, resp = 0;

        y = 10+x;

        if(abs(x)%2==1)
        {
            x++;
        }

        for(j=x; j<y; j+=2)
        {
            resp+=j;
        } 

        cout << resp << endl;

        cin >> x;

    }

    return(0);
}
