#include "main.h"

int main()
{
    char s1[98];
    int i, j;
    int count = 0;

    for (i = 0; i < 98 - 1; i++)
        {
            s1[i] = '*';
            count++;
        }

    for (j = 0; j < count; j++)
        printf("[%d] %s\n", j, s1);

    return 0;
}