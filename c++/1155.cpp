#include <bits/stdc++.h>
using namespace std;

int main()
{
  double i, resp = 0;

  for (i = 1; i <= 100; i++)
  {
    resp += 1 / i;
  }

  printf("%.2f\n", resp);

  return (0);
}