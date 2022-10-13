#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int main() 
{
    double a, b, c, x, y, z, r1, r2, r3;

    scanf("%lf %lf %lf", &a, &b, &c);
    scanf("%lf %lf %lf", &x, &y, &z);
    
    r1= floor(x/a);
    r2= floor(y/b);
    r3= floor(z/c);

    int h = r1*r2*r3;
    printf("%d\n", h);

    return 0;
}