#include "main.h"

/*Write a function that prints an integer.*/

void print_number(int n)
{
    if(n < 0)
    {
        n = -n;
        _putchar('-');    
    }
    if (n > 9)
    {
        print_number(n / 10);
    }
    _putchar(n % 10 + '0');
    
}
/*/////////////////////////////////////////////////*/
    /*int num = n;
    if (n < 0)
    {
        _putchar('-');
        num = -num;
    }
    if (num > 9)
    {
        print_number(num / 10);
    }
    _putchar(num % 10 + '0');
}*/

int main(void)
{
    print_number(98);
    _putchar('\n');
    print_number(402);
    _putchar('\n');
    print_number(1024);
    _putchar('\n');
    print_number(0);
    _putchar('\n');
    print_number(-98);
    _putchar('\n');
    return (0);
}