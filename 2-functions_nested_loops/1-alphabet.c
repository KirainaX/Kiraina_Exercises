#include "main.h"

/*Write a function that prints the alphabet, in lowercase, followed by a new line.*/

void print_alphabet(void)
{
    char a;
    for(a = 'a'; a <= 'z'; a++)
    {
        _putchar(a);
    }
    _putchar('\n');
}
int main(void)
{
    print_alphabet();
    return (0);
}
