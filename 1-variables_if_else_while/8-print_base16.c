#include <stdio.h>

/*Write a program that prints all the numbers of base 16 in lowercase, followed by a new line.*/

int main()
{
    int a;
    char r;

    for(a = '0'; a <= '9'; a++)
    {
        putchar(a);
    }
    for(r = 'a'; r <= 'f'; r++)
    {
        putchar(r);
    }
    putchar('\n');

    return 0;
}
