#include <stdio.h>
 
int main()
{
    double n1, n2, res=0;

    scanf("%lf", &n1);
    scanf("%lf", &n2);

    res = (n1*3.5 + n2*7.5)/11;

    printf("MEDIA = %.5lf\n", res);
 
 
    return 0;
}