#include <stdio.h>

/*Write a program that prints all possible combinations of two two-digit numbers.*/

int main()
{
    int i = 0, j, count = 0;

    while (i <= 98)
    {
        j = i + 1;
        while (j <= 99)
        {
            putchar((i / 10) + '0');
            putchar((i % 10) + '0');
            putchar(' ');
            putchar((j / 10) + '0');
            putchar((j % 10) + '0');
            if(count != 4949)
            {
                putchar(',');
                putchar(' ');
            }
            j++;
            count++;
        }
        i++;
    }
    putchar('\n');

    return 0;
}
