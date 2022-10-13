#include <stdio.h>
 
int main() 
{
    int valor, vv, n100=0, n50=0, n20=0, n10=0, n5=0, n2=0, n1=0;

    scanf("%d", &valor);  

    vv = valor;

    while(vv > 0)
    {
        if(vv >= 100){
            vv = vv-100;
            n100+=1;
        }
        else if(vv >= 50){
            vv = vv-50;
            n50+=1;
        }
        else if(vv >= 20){
            vv = vv-20;
            n20+=1;
        }
        else if(vv >= 10){
            vv = vv-10;
            n10+=1;
        }
        else if(vv >= 5){
            vv = vv-5;
            n5+=1;
        }
        else if(vv >= 2){
            vv = vv-2;
            n2+=1;
        }
        else if(vv >= 1){
            vv = vv-1;
            n1+=1;
        }
    }  

    printf("%d\n", valor);
    printf("%d nota(s) de R$ 100,00\n", n100);
    printf("%d nota(s) de R$ 50,00\n", n50);
    printf("%d nota(s) de R$ 20,00\n", n20);
    printf("%d nota(s) de R$ 10,00\n", n10);
    printf("%d nota(s) de R$ 5,00\n", n5);
    printf("%d nota(s) de R$ 2,00\n", n2);
    printf("%d nota(s) de R$ 1,00\n", n1);

    return 0;
}