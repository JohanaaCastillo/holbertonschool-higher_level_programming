/**
 * main - entry point
 *
 * Return:always return 0
 *
 */

#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE

int main(void){
	int number;

	srand(time(0));
	number = rand() - RAND_MAX / 2;
	if (number < 0)
	{
		printf("%d is negative\n", number);
	} 
    else if (number == 0)
	{
		printf("%d is zero\n", number);
	} else
	{
		printf("%d is positive\n", number);
	}
	return (0);
}
