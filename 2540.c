#include <stdio.h>

int main()
{
	int input;
	while(scanf("%d", &input) == 1)
	{
	int i, count= 0, x;
	for(i = 1; i <= input; i++)
	{
	scanf("%d", &x);
	count += x;
	}
	
	float temer = ((float)input/3) * 2;
		
	if(count >= temer) {
		printf("impeachment\n");
	} else 
	{
		printf("acusacao arquivada\n");
	}

	}
	
	return 0;
}