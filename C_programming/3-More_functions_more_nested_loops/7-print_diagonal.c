#include "main.h"

/*Write a function that draws a diagonal line on the terminal.*/

void print_diagonal(int n)
{
    int i, j;
    if(n > 0)
    {
       for(i = 0; i < n; i++)
        {
        for (j = 0; j < i; j++)
        {
            _putchar(' ');
        }
        _putchar('\\');
        _putchar('\n');
        } 
    }
}

/*void print_diagonal(int n)
{
int len, space;

if (n > 0)
{
    for (len = 0; len < n; len++)
    {
        for (space = 0; space < len; space++)
            _putchar(' ');

        _putchar('\\');

        if (len == (n - 1))
            continue;
        _putchar('\n');
    }
}
_putchar('\n');
}*/

int main(void)
{
    print_diagonal(0);
    print_diagonal(2);
    print_diagonal(10);
    print_diagonal(-4);
    return (0);
}