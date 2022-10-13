#include <stdio.h>
#include <math.h>

int main()
{
    long int n, pp, t;

    scanf("%ld", &n);

    for(int i = 0; i < n; i++)
    {
        scanf("%ld", &pp);
        t = 0;

        if(pp==2147483648){ 
            printf("Not Prime\n");
        }
           
        else{
            for(int j = 2; j <= sqrt(pp); j++)
            {
                if(pp % j == 0){
                    t = 1;
                    break;
                }
            }

            if(t==1){
                printf("Not Prime\n");
            }else{
                printf("Prime\n");
            }
        }
        

        


    
    }

    return 0;
}