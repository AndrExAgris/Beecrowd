#include <stdio.h>
 
int main() 
{
    int a, b, c, d, e;

    scanf("%d %d %d %d %d", &a, &b, &c, &d, &e);
    
    int x=0,y=0;
    int vet[5];
    vet[0]=a;
    vet[1]=b;
    vet[2]=c;
    vet[3]=d;
    vet[4]=e;

    for(int i=1; i<5; i++){
        if(vet[i-1]<vet[i]){
            x++;
        }
        if(vet[i-1]>vet[i]){
            y++;
        }
    }

    if(x==4){
        printf("C\n");
    }else if(y==4){
        printf("D\n");
    }else{
        printf("N\n");
    }
    return 0;
}