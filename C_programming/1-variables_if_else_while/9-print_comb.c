#include <stdio.h>

/*Write a program that prints all possible combinations of single-digit numbers.*/

int main()
{
    int a;

    for(a = '0'; a <= '9'; a++)
    {
        putchar(a);
        if(a != '9')
        {
            putchar(',');
            putchar(' ');
        }
    }
    putchar('\n');

    return 0;
}
