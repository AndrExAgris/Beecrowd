#include <stdio.h>
 
int main() {
 
    double n, vetor[100];

    scanf("%lf", &n);

    for(int i=0; i<100; i++)
    {
        vetor[i] = n;
        n = n/2;
    }

    for(int i=0; i<100; i++)
    {
        printf("N[%d] = %.4lf\n", i, vetor[i]);
    }

 
    return 0;
}