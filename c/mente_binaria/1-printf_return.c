#include <stdio.h>

int main(void){
	int ret;
	int test = 0;
	
	ret = printf("saving the return of printf\n");	// printf returns the number of bytes printed, except 0x00 NULL byte
	printf("return from printf: %i\n", ret);
	
	// converting to decimal, 'A' is converted according to the ASCII table
	printf("printing decimals: %d - %d - %d - %d - %x - %c", test, 10, 0xa, 'A', 0xa, 65);
	printf("%c", 10);	// character 10 = \n
	
	return 0;
}
