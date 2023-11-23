#include "main.h"

/*Write a function that concatenates two strings.*/

char *_strncat(char *dest, char *src, int n)
{
    char *str = dest;
    int i = 0;

    while (*str)
        str++;

    while (*src)
    {
        *str = src[i];
        if(i == n)
            break;
        else if(src[i] == '\0')
            break;
        else
        {
            str++;
            i++;
        }
    }
    *str = '\0';
    return dest;
    /*//////////////////////////////*/
    /*int length, j;*/
/* j is a counter for  n bytes of src to be concatenated */
/* length = length of destination string */
	/*length = 0;

	while (dest[length] != '\0')
        length++;

	for (j = 0; j < n && src[j] != '\0'; j++, length++)
        dest[length] = src[j];

	dest[length] = '\0';
	return (dest);*/
}

int main(void)
{
    char s1[98] = "Hello ";
    char s2[] = "World!\n";
    char *ptr;

    printf("%s\n", s1);
    printf("%s", s2);
    ptr = _strncat(s1, s2, 1);
    printf("%s\n", s1);
    printf("%s", s2);
    printf("%s\n", ptr);
    ptr = _strncat(s1, s2, 1024);
    printf("%s", s1);
    printf("%s", s2);
    printf("%s", ptr);
    return (0);
}