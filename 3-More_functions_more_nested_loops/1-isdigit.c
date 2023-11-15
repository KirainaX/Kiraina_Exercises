#include "main.h"

/*Write a function that checks for a digit (0 through 9).*/

int _isdigit(int c)
{
    if(c >= '0' && c <= '9')
        return 1;
    else
        return 0;
}

int main()
{
    char c;

    c = '0';
    printf("%c: %d\n", c, _isdigit(c));
    c = 'a';
    printf("%c: %d\n", c, _isdigit(c));
    return (0);
}
