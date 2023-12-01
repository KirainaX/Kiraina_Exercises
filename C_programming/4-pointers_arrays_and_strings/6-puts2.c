#include "main.h"

/*Write a function that prints every other character of a string, starting with the first character, followed by a new line.*/

void puts2(char *str)
{
    int j, i;

	j = 0;

	while (str[j] != '\0')
	{
		j++;
	}
	for (i = 0; i < j; i += 2)
	{
		_putchar(str[i]);
	}
	_putchar('\n');
}

int main(void)
{
    char *str;

    str = "0123456789";
    puts2(str);
    return (0);
}