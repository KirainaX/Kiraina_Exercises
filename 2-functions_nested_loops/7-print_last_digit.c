#include "main.h"

/*Write a function that prints the last digit of a number.*/

int print_last_digit(int r)
{
    int a;

    if(r > 0)
    {
        a = r % 10;
        _putchar(a + '0');
    }
    else if(r < 0)
    {
        a = -r % 10;
        _putchar(a + '0');
    }
    else
    {
        putchar(r +'0');
    }
    return a;
}
int main(void)
{
    int r;

    print_last_digit(98);
    print_last_digit(0);
    r = print_last_digit(-1024);
    _putchar('0' + r);
    _putchar('\n');
    return (0);
}
