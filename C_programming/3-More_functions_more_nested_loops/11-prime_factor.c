 #include "main.h"

/*Write a program that finds and prints the largest maxPrime factor of the number 612852475143, followed by a new line.*/

int main()
{
    long n;
    int maxPrime, oddPrime;
    n = 612852475143;
    maxPrime = 0;
    oddPrime = 3;

    while((n % 2) == 0)
    {
        maxPrime = 2;
        n /= 2;
    }
    while(n != 1)
    {
        while((n % oddPrime) == 0)
        {
            maxPrime = oddPrime;
            n /= oddPrime;
        }
        oddPrime += 2;
    }
    printf("%d\n", maxPrime);

    return 0;
/*/////////////////////////////////////////////////*/
    /*long number = 600851475143;
    int inc;

    while (inc++ < number / 2)
    {
        if (number % inc == 0)
        {
            number /= 2;
            continue;
        }
        for (inc = 3; inc < number / 2; inc += 2)
        {
            if (number % inc == 0)
                number /= inc;
        }
    }
    printf("%ld\n", number);

    return (0);*/
}