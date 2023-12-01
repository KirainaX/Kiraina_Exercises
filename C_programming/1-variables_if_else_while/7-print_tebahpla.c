#include <stdio.h>

/*Write a program that prints the lowercase alphabet in reverse, followed by a new line.*/

int main()
{
    char a;
    for(a = 'z'; a >= 'a'; a--)
    {
        putchar(a);
    }
    putchar('\n');

    return 0;
}
