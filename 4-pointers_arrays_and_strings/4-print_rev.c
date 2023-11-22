#include "main.h"

/*Write a function that prints a string, in reverse, followed by a new line.*/

void print_rev(char *s)
{
    int i, size;
    
    /*size = strlen(s);*/

    while(s[size] != '\0')
    {
        size++;
    }

    for((i = size  -1); i >= 0; i--)
    {
        _putchar(s[i]);
    }
    _putchar('\n');
}

int main(void)
{
    char *str;

    str = "I do not fear computers. I fear the lack of them - Isaac Asimov";
    print_rev(str);
    return (0);
}