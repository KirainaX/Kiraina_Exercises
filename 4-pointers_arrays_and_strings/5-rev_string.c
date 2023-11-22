#include "main.h"

/*Write a function that reverses a string.*/

void rev_string(char *s)
{
    /*int i , size;
    size = 10;

    for((i = size - 1); i >= 0; i--)
    {
        *s = s[i];
    }*/
    char sp;
	int i, size, size1;

	size = 0;
	size1 = 0;

	while (s[size] != '\0')
	{
		size++;
	}

	size1 = size - 1;

	for (i = 0; i < size / 2; i++)
	{
		sp = s[i];
		s[i] = s[size1];
		s[size1--] = sp;
	}
}

int main(void)
{
    char s[10] = "My School";

    printf("%s\n", s);
    rev_string(s);
    printf("%s\n", s);
    return (0);
}