#include <stdio.h>

/*Write a program that prints all possible different combinations of three digits.*/

int main()
{
    int i = 0, j, k, count = 0;

    while(i <= 7)
    {
        j = i + 1;
        while (j <= 8)
        {
            k = j + 1;
            while (k <= 9)
            {
                putchar(i + '0');
                putchar(j + '0');
                putchar(k + '0');
                if(count != 119)
                {
                    putchar(',');
                    putchar(' ');
                }                
                k++;
                count++;
            }
            j++;
        }
        i++;
    }
    putchar('\n');
    return 0;
}
