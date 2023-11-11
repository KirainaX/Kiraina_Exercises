#include <stdio.h>

/*Write a program that prints the alphabet in lowercase, and then in uppercase, followed by a new line.*/

int main()
{
    char a, z;

    for(a = 'a'; a <= 'z'; a++)
        putchar(a);
    for(z = 'A'; z <= 'Z'; z++)
        putchar(z);
    putchar('\n');

    return 0;
}
