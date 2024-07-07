#include <stdio.h>

int main(void){
	int numbers[5];
	
	numbers[0] = 17;	// assing a value to the position
	printf("%i\n", numbers[0]);

	printf("4 bytes per int X 5 ints = %zu bytes", sizeof(numbers));

	return 0;
}
