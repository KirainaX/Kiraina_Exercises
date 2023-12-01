#include <stdio.h>
#include <time.h>
#include <stdlib.h>

/*This program will assign a random number to the variable n each time it is executed.
  Complete the source code in order to print whether the number stored in the variable {n} is positive or negative.*/

int main()
{
    int n;

    //srand(time(0));
	//n = rand() - RAND_MAX / 2;
	/* your code goes there */
    printf("Enter the value of n : ");
    scanf("%d", &n);

    if(n > 0)
    {
        printf("%d is positive", n);
    }
    else if(n < 0)
    {
        printf("%d is negative", n);
    }
    else
    {
        printf("%d is zero", n);
    }

    return 0;
}
