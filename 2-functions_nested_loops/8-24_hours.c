#include "main.h"

/*Write a function that prints every minute of the day of Jack Bauer, starting from 00:00 to 23:59.*/

void jack_bauer(void)
{
    int i = 0;
    int j = 0;

    for(i = 0; i <= 23; i++)
    {
        for(j = 0; i <= 59; j++)
        {
            printf("%d", i/10);
            printf("%d", i%10);
            putchar(':');
            printf("%d", j/10);
            printf("%d", j%10);
            putchar('\n');
        }
    }
}

int main()
{
    jack_bauer();
    return 0;
}
