#include <stdio.h>

// program to calculate the n-th term of an arithmetic sequenceo
int main(void){
	int d = 2;
	int a1 = 1;
	int n = 9;
	int an;

	an = a1 + (n - 1) * d;
	
	printf("an = %i", an);

	return 0;
}
