#include <stdio.h>
 
int main() {
 
    int i, patu=0, pmaior=0, natu=0, nmaior=0;

    for( i=0; i<100; i++)
    {
        patu++;
        scanf("%d", &natu);

        if(natu>nmaior){
            nmaior = natu;
            pmaior = patu;
        }
    }
    
    printf("%d\n", nmaior);
    printf("%d\n", pmaior);

    return 0;
}