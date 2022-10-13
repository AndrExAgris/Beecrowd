#include <stdio.h>

int main()
{
	double input, out;
	
	scanf("%lf", &input);
	
	if(input <= 2000)
	{
		printf("Isento\n");
	} else if(input <= 3000)
	{
		out = (input - 2000) * 0.08;
		printf("R$ %.2lf\n", out);
	} else if(input <= 4500)
	{
		out = (input - 3000) * 0.18 + 80;
		printf("R$ %.2lf\n", out);
	}	else 
	{
		out = (input - 4500) * 0.28 + 80 + 270;
		printf("R$ %.2lf\n", out); 
	}
	
	return 0;
}