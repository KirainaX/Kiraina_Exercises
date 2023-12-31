#include "main.h"

/**Write a function that reverses the content of an array of integers.
 * Prototype: void reverse_array(int *a, int n);
 * Where n is the number of elements of the array*/

void reverse_array(int *a, int n)
{
    int i, j;

	n = n - 1;
	j = 0;
    
	while (j <= n)
	{
		i = a[j];
		a[j++] = a[n];
		a[n--] = i;
	}
}

void print_array(int *a, int n)
{
    int i;

    i = 0;
    while (i < n)
    {
        if (i != 0)
        {
            printf(", ");
        }
        printf("%d", a[i]);
        i++;
    }
    printf("\n");
}

int main(void)
{
    int a[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 98, 1024, 1337};

    print_array(a, sizeof(a) / sizeof(int));
    reverse_array(a, sizeof(a) / sizeof(int));
    print_array(a, sizeof(a) / sizeof(int));
    return (0);
}