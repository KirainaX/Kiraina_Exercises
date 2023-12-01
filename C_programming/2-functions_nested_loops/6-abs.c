#include "main.h"

/*Write a function that computes the absolute value of an integer.*/

int _abs(int r)
{
    if(r < 0)
    {
        return -r;
    }
    else
    {
        return r;
    }
}
int main(void)
{
    int r;

    r = _abs(-1);
    printf("%d\n", r);
    r = _abs(0);
    printf("%d\n", r);
    r = _abs(1);
    printf("%d\n", r);
    r = _abs(-98);
    printf("%d\n", r);
    return (0);
}
