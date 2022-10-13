#include <stdio.h>
 
int main() 
{
    int x;
    scanf("%d", &x);
    int vet[x];
    for(int i=0; i<x; i++){
        scanf("%d", &vet[i]);
    }

    
    while(x>=1){
        for(int j=0; j<x-1; j++){
            
            if(vet[j]==vet[j+1]){
                vet[j] = -1;
            }else{
                vet[j] = 1;
            }
        }
        x--;
    }
    if(vet[0]==-1){
        printf("preta\n");
    }else{
        printf("branca\n");
    }

    return 0;
}