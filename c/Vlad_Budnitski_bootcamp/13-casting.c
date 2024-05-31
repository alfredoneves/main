#include <stdio.h>

int main(void){
	int a = 5;
	int b = 2;
	double c = 2.0;
	
	printf("a = %i\nb = %i\nc = %lf\n", a, b, c);
	printf("a / b = %d\n", a / b);	// the operation between the same type results in the same type
	printf("a / c = %lf\n", a / c);	// implicit declaration, the program follows the double rule
	printf("(casting) a / b = %lf\n", (double) a / b);
	printf("a = %d", a);
	return 0;
}
