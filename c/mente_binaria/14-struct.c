#include <stdio.h>

struct st {	// creates a structure named st
	unsigned char id;
	unsigned int num;
};

int main(void) {
	struct st s;	// initializes the struct
	
	s.id = 4;
	s.num = 2024;
	
	printf("s.id = %d\n", s.id);
	printf("s.num = %d\n", s.num);
	
	return 0;
}
