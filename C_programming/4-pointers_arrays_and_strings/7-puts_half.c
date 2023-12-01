#include "main.h"

/*Write a function that prints half of a string, followed by a new line.*/

void puts_half(char *str)
{
    int j, n, i;

	j = 0;

	while (str[j] != '\0')
		j++;

	if (j % 2 == 0)
	{
		for (i = j / 2; str[i] != '\0'; i++)
			_putchar(str[i]);
	}
    else if (j % 2)
	{
		for (n = (j - 1) / 2; n < j - 1; n++)
			_putchar(str[n + 1]);
	}
	_putchar('\n');
}

int main(void)
{
    char *str;

    str = "0123456789";
    puts_half(str);
    return (0);
}