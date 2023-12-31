#include "main.h"

/*If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
 * The sum of these multiples is 23.
 * Write a program that computes and prints the sum of all the multiples of 3 or 5 below 1024 (excluded).
 * Followed by a new line.*/

int main()
{
	unsigned long int a = 0, b = 0, c = 0;
	int i;

	for(i = 0; i < 1024; ++i)
	{
		if((i % 3) == 0)
		{
			a = a + i;
		}
		else if((i % 5) == 0)
		{
			b = b + i;
		}
	}
	c = a + b;
	printf("%ld\n", c);

	return 0;
}
