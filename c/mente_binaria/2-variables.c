#include <stdio.h>
#include <stdbool.h>

int main(void){
	char c;
	unsigned char d;
	bool b;
	
	printf("size of c = %lu bytes\n", sizeof(c));
	printf("size of an int = %lu bytes\n", sizeof(int));
	
	// signed X unsigned
	c = 255;
	d = 255;
	printf("c = %i\nd=%i\n", c, d);
	
	// boolean
	b = true;
	printf("size of b: %lu bytes\n", sizeof(b));
	
	return 0;
}
