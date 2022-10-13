#include <stdio.h>
#include <math.h>
 
int main() {
 
    double a, b, total=0 ,aux;

    scanf("%lf %lf", &a, &b);

    aux=(a*b)/10;

    for(int i=0; i<8; i++){
        total= total+aux;
        int h = ceil(total);
        printf("%d ", h);
    }
    total= total+aux;
    int h = ceil(total);
    printf("%d\n", h);
 
    return 0;
}