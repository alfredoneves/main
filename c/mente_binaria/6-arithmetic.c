#include <stdio.h>

int main(void){
	float a;
	int b;
	
	a = 10 / 3.0;	// without the .0 the program will consider it int
	printf("%.2f\n", a);

	a *= 10;	// multiplies a for 10
	a -= 1;	// subtracts 1
	a--;	// subtracts 1
	printf("%.2f\n", a);
	
	b = 10 % 3;	// rest of division
	printf("The rest of division 10 / 3 = %i", b);
	
	return 0;
}
