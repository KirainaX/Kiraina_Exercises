#include <stdio.h>

/*Write a program that prints all possible different combinations of two digits.*/

int main()
{
    int i = 0;
	int j;
	int count = 0;

	while (i <= 8)
	{
		j = i + 1;
		while (j <= 9)
		{
			putchar(i + '0');
			putchar(j + '0');
			if (count != 44)
			{
				putchar(',');
				putchar(' ');
			}
			j++;
			count++;
		}
		i++;
	}
	putchar('\n');
	return (0);
}
