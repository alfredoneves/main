#include <stdio.h>

int main(void){
	int a = 3;

	printf("size int a = %zu\n", sizeof(a));
	
	printf("double a = %lf\n", (double) a);	// casting doesn't change the original value

	printf("size of double a = %zu\n", sizeof((double) a));
	return 0;
}
