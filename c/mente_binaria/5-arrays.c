#include <stdio.h>
#include <limits.h>
#include <stdint.h>
#include <stdlib.h>

int main(void){
	char c[3];
	
	printf("The size of c is %zu bytes\n", sizeof(c));
	printf("the number of elements of c is %zu\n", sizeof(c) / sizeof(c[0]));	// way to check the number of elements
	
	c[0] = 'A';
	c[1] = 'B';
	c[2] = 0xff;
	
	printf("The memory address of c is %p\n", &c);	// takes the memory address
	printf("The memory address of the first element of c is %p\n", &c[0]);	// the array starts in the first element
	
	// c just grabs the value in memory without warning that you exceeded the array, be careful 
	printf("The value stored in the next position after the array is %p\n", c[4]);
	
	return 0;
}
