#include "main.h"

/*Write a function that draws a straight line in the terminal.*/

void print_line(int n)
{
    int i;

    for(i = 0; i < n; i++)
    {
        _putchar('-');
    }
    _putchar('\n');
}

int main(void)
{
    print_line(0);
    print_line(2);
    print_line(10);
    print_line(-4);
    return (0);
}