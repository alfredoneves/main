#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void *malloc_s(size_t size) {	// creating a pointer to test if the memory is allocated correctly
	void *p;
	p = malloc(size);
	
	if (p == NULL) {
		fprintf(stderr, "Insuficient memory\n");
		exit(1);
	}
	
	return p;
}

int main(int argc, char *argv[]) {
	int *p;
	
	p = malloc_s(3 * sizeof(int));	// allocates 24 bytes (3 * the size of the int)
	memset(p, 0, 3 * sizeof(int));	// clears the memory
	
	*p = 7;
	*(p+1) = 13;
	*(p+2) = 23;
	
	for (int i=0; i<4; i++) {	// printing +1 to show that memset set it to 0
		printf("%d\n", *(p+i));
	}
	
	free(p);
	return 0;
}
