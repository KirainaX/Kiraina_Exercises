#include "main.h"

/*Write a function that prints all natural numbers from n to 98, followed by a new line.*/

void print_to_98(int n)
{
	if(n <= 0)
	{
		while(n <= 98)
		{
			if(n < 0)
			{
				printf("%d, ", n);
				n++;
			}
			else if(n < 10)
			{
				printf("%d, ", n);
				n++;
			}
			else if(n >= 10)
			{
				printf("%d, ", n);
				n++;
			}
		}
		printf("\n");
	}
	else if(n == 98)
	{
		printf("%d\n", n);
	}
	else if(n > 98)
	{
		while(n >= 98)
		{
			printf("%d, ", n);
			n--;
		}
		printf("\n");
	}
	else if(n < 98)
	{
		while(n <= 98)
		{
			printf("%d, ", n);
			n++;
		}
		printf("\n");
	}
}

int main(void)
{
	print_to_98(0);
    	print_to_98(98);
    	print_to_98(111);
    	print_to_98(81);
    	print_to_98(-10);
    return (0);
}
