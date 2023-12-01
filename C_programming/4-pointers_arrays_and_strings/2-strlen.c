#include "main.h"

/*Write a function that returns the length of a string.*/

int _strlen(char *s)
{
    int i = 0;
    if(s != NULL)
    {
        while (s[i])
            i++;
    }
    
    return i;
}

int main(void)
{
    char *str;
    int len;

    str = "My first strlen!";
    len = _strlen(str);
    printf("%d\n", len);
    return (0);
}