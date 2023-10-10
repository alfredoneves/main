#include <stdio.h>

int main(void){
	int a = 1;
	int b = 2;
	int c = 1;
	int d;
	
	printf("a = %d\nb = %d\nc = %d\n", a, b, c);
	printf("a == b: %d\n", a == b);
	printf("a == c: %d\n", a == c);
	printf("a == d: %d\n", a == d);
	printf("a && d: %d\n", a && d);	// tests if they both have values different of 0
	printf("a && b: %d\n", a && b);
	printf("a || d: %d\n", a || d);
	
	return 0;
}
