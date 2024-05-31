#include <stdio.h>

// c is a call-by-value language, when you call swap passing the variables as arguments
//  it saves the arguments in another place of memory so the original don't change because of the args

int swap(a, b){
	int t = a;
	a = b;
	b = t;
	printf("swap:\na = %i\nb = %i\n", a, b);
	
	return 0;
}

int main(void){
	int a = 10;
	int b = 20;

	swap(a, b);
	printf("main:\na = %i\nb = %i\n", a, b);

	return 0;
}
