#include "main.h"

/*Write a function that concatenates two strings.*/

char *_strcat(char *dest, char *src)
{
    char *str = dest;

    while (*str)
        str++;
    
    while (*src)
    {
        *str = *src;
        str++;
        src++;
    }
    *str = '\0';
    return dest;
}

int main(void)
{
    char s1[98] = "Hello ";
    char s2[] = "World!\n";
    char *ptr;

    printf("%s\n", s1);
    printf("%s", s2);
    ptr = _strcat(s1, s2);
    printf("%s", s1);
    printf("%s", s2);
    printf("%s", ptr);
    return (0);
}