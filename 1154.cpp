#include <bits/stdc++.h>
using namespace std;

int main()
{
  int x;
  double soma = 0, count = 0, media = 0;

  while (1)
  {

    cin >> x;

    if (x < 0)
    {
      break;
    }
    else
    {
      soma += x;
      count += 1;
    }
  }

  media = soma / count;

  printf("%.2f\n", media);

  return (0);
}