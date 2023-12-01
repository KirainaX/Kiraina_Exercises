#include "main.h"

/**Write a function that compares two strings.
 * Prototype: int _strcmp(char *s1, char *s2);
 * Your function should work exactly like strcmp*/

int _strcmp(char *s1, char *s2)
{
    /*while (*s1 != '\0' && *s1 == *s2)
    {
        s1++;
        s2++;
    }
    
    return *(unsigned char *)s1 - *(unsigned char *)s2;*/
    /*/////////////////////////////////////////////////////////*/
    int i, j;

	i = 0;

	while (s1[i] == s2[i] && s1[i] != '\0')
		i++;

	j = s1[i] - s2[i];
	return (j);
}

int main(void)
{
    char s1[] = "Hello";
    char s2[] = "World!";

    printf("%d\n", _strcmp(s1, s2));
    printf("%d\n", _strcmp(s2, s1));
    printf("%d\n", _strcmp(s1, s1));
    return (0);
}