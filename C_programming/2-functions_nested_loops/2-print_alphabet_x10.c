#include "main.h"

/*Write a function that prints 10 times the alphabet, in lowercase, followed by a new line.*/

void print_alphabet_x10(void)
{
    int i = 0;
    char a;

    for(i = 0; i < 10; i++)
    {
        for(a = 'a'; a <= 'z'; a++)
        {
            _putchar(a);
        }
        _putchar('\n');
    }
}
int main(void)
{
    print_alphabet_x10();
    return (0);
}
