#include "main.h"

/*Write a function that prints a triangle, followed by a new line.*/

void print_triangle(int size)
{  
    int i, j;

    if(size <= 0)
        _putchar('\n');
    for (i = 1; i <= size; i++)
    {
        for ((j = size - i); j > 0; j--)
            _putchar(' ');
        for (j = 0; j < i; j++)
            _putchar('#');
        _putchar('\n');
    }
}

int main(void)
{
    print_triangle(2);
    print_triangle(10);
    print_triangle(1);
    print_triangle(0);
    return (0);
}