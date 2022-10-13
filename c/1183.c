#include <stdio.h>
#include <string.h>
 
int main() 
{
    double m[12][12], valor=0;
    char op;

    scanf("%c", &op);

    for(int i=0; i<12; i++)
    {
        for(int j=0; j<12; j++)
        {
            scanf("%lf", &m[i][j]);
            if(i<j){
                valor+=m[i][j];
            }
        }
    }

    if(op == 'S'){
        printf("%.1lf\n", valor);
    }else if(op == 'M'){
        valor=valor/66;
        printf("%.1lf\n", valor);
    }

 
    return 0;
}