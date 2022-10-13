#include <bits/stdc++.h>
using namespace std;

int main()
{

    int n, i;

    cin >> n;

    for(i=0; i<n;i++)
    {
        int x, y, j, count = 0, resp = 0;

        cin >> x;
        cin >> y;

        y = (y*2)+x;

        if(x%2==0)
        {
            x++;
        }

        for(j=x; j<y; j+=2)
        {
            resp+=j;
        } 

        cout << resp << endl;


    }

    return(0);
}