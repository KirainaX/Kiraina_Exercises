#include "main.h"

/*Write a function that prints the numbers, from 0 to 9, followed by a new line.*/

void print_most_numbers(void)
{
    int i;

    for(i = 0; i <= 9; i++)
    {
        if(i % 10 != 0)
            _putchar(i + '0');
    }
    _putchar('\n');
}

int main(void)
{
    print_most_numbers();
    return (0);
}
