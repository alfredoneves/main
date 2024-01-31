#include <stdio.h>

union st {	// the union is used to select only one attribute because it only allocates the bytes for the greater
	unsigned char id;
	unsigned int num;
};

int main(void) {
	union st s;
	
	s.id = 2024;
	
	printf("s.num = %d\n", s.num);
	printf("sizeof(s) = %d\n", sizeof(s));
	
	return 0;
}
