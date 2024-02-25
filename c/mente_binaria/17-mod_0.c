#include <stdio.h>

int i = 10;	// i must be a global var to be used in 17-mod_1.c too

int main(void) {	
	printf("i = %d\n", i);
	double_i();
	printf("i = %d\n", i);
	
	return 0;
}
