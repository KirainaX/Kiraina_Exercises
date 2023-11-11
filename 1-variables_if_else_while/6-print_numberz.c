#include <stdio.h>

/*Write a program that prints all single digit numbers of base 10 starting from 0, followed by a new line.*/

int main()
{
    int a;

    for(a = '0'; a <= '9'; a++)
    {
        putchar(a);
    }
    putchar('\n');

    return 0;
}
