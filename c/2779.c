#include <stdio.h>
 
int main() {
 
    int total, comprada, aux, figurinhas=0;
    
    scanf("%d", &total);
    scanf("%d", &comprada);

    int vet[comprada];
    int auxvet[comprada];

    for(int i=0; i<comprada; i++){
        scanf("%d", &aux);
        vet[i]=aux;
    }
    
    for(int i=0; i<comprada; i++){
        aux=vet[i];
        if(aux!=0){
            figurinhas++;
        }
        for(int j=i; j<comprada; j++){     
            if(vet[j]==aux){
                vet[j]=0;
            }
        }
    }
    int res=total-figurinhas;
    printf("%d\n",res);
 
    return 0;
}