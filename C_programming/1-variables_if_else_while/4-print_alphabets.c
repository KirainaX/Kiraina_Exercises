#include <stdio.h>

/*Write a program that prints the alphabet in lowercase, followed by a new line.*/

int main()
{
    char a;

    for(a = 'a'; a <= 'z'; a++)
    {
        if(a == 'e' || a == 'q')
            continue;
        putchar(a);
        
    }

    return 0;
}
