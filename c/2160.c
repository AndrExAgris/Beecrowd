#include <stdio.h>
#include <string.h>

int main()
{
    char input[502];

    fgets(input, sizeof(input), stdin);

    if(strlen(input) <= 81)
    {
        printf("YES\n");
    } else {
        printf("NO\n");
    }

    return 0;
}