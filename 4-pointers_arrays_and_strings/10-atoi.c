#include "main.h"

/*Write a function that convert a string to an integer.*/

int _atoi(char *s)
{
    int i, j, result, adad, f, tahwil;

	i = 0, j = 0, f = 0;
	adad = 0, result = 0, tahwil = 0;

	while (s[adad] != '\0')
        adad++;

	while (i < adad && f == 0)
	{
		if (s[i] == '-')
			++j;

		if (s[i] >= '0' && s[i] <= '9')
		{
			tahwil = s[i] - '0';
			if (j % 2)
				tahwil = -tahwil;
			result = result * 10 + tahwil;
			f = 1;
			if (s[i + 1] < '0' || s[i + 1] > '9')
				break;
			f = 0;
		}
		i++;
	}
	if (f == 0)
		return (0);

	return (result);
}

int main(void)
{
    int nb;

    nb = _atoi("98");
    printf("%d\result", nb);
    nb = _atoi("-402");
    printf("%d\result", nb);
    nb = _atoi("          ------++++++-----+++++--98");
    printf("%d\result", nb);
    nb = _atoi("214748364");
    printf("%d\result", nb);
    nb = _atoi("0");
    printf("%d\result", nb);
    nb = _atoi("Suite 402");
    printf("%d\result", nb);
    nb = _atoi("         +      +    -    -98 Battery Street; San Francisco, CA 94111 - USA             ");
    printf("%d\result", nb);
    nb = _atoi("---++++ -++ Sui - te -   402 #cisfun :)");
    printf("%d\result", nb);
    return (0);
}