#include <stdio.h>
#include <limits.h>

int main(void){
	int i = INT_MAX;
	short int j;
	long int k = LONG_MAX;
	register int l;	// the variable is inserted in the register directly to increase the performance, used in counters
	
	printf("The size of int is: %zu bytes\n", sizeof(i));
	printf("The max value of i is: %u\n", i);
	
	printf("The short int j is: %zu bytes\n", sizeof(j));
	
	printf("The long int k is: %zu bytes\n", sizeof(k));
	printf("The max value of the long int k is: %lu", k);
	
	return 0;
}
