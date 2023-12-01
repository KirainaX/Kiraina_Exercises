#include <stdio.h>
#include <time.h>
#include <stdlib.h>

/*Write a program that prints the alphabet in lowercase, followed by a new line.*/

int main()
{
    char z;

    for(z = 'a'; z <= 'z'; z++)
    {
        putchar(z);
    }
    putchar('\n');

    return 0;
}
