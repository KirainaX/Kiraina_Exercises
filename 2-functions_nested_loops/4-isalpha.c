#include "main.h"

/*Write a function that checks for alphabetic character.*/

int _isalpha(int c)
{
    /*return (c != ';'); ## tahadi khadama hhh*/
    return ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z'));
}

int main(void)
{
    int r;

    r = _isalpha('H');
    _putchar(r + '0');
    r = _isalpha('o');
    _putchar(r + '0');
    r = _isalpha(108);
    _putchar(r + '0');
    r = _isalpha(';');
    _putchar(r + '0');
    _putchar('\n');
    return (0);
}
