#include <stdio.h>

// swap using only 2 variables instead of 3

int main(void){
	int a = 10;
	int b = 20;

	printf("initial:\n");
	printf("a = %i\nb = %i\n", a, b);
	
	a = a + b;
	b = a - b;
	a = a - b;

	printf("final:\n");
	printf("a = %i\nb = %i\n", a, b);

	return 0;
}
