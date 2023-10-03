// float is not an exact number, it it's precise, but you should be carefull when doing operations
#include <stdio.h>
#include <limits.h>
#include <stdint.h>
#include <stdlib.h>

int main(void){
	float f = 3e2;	// 3 * (10 ** 2), just another way of writing
	double d = 1;
	float a = 10;
	float b = 3;
	float c;
	
	printf("The size of float f is: %zu bytes\n", f);
	printf("Float f = %f\n", f);
	
	c = a / b;
	printf("a = %f\nb = %f\nc = a / b\nc = %.20f\n", a, b, c);

	return 0;
}
