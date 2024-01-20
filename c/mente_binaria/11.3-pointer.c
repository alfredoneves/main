#include <stdio.h>

int main(int argc, char *argv[]) {
	printf("We can know the architecture of the processor by the size of the pointer\n");
	printf("32 bits - int = 4 bytes\n 64 bits - int = 8 bytes\n");
	int *i;
	printf("size of i: %zu", sizeof(i));
	
	return 0;
}
