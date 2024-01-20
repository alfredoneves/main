#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
	int *j = NULL;	// create a pointer and insert the value nil in memory to avoid mistakes
	printf("address of j: %p\n", &j);
	
	j = malloc(sizeof(int));	// alocates the size of an int in bytes to the pointer j
	printf("address of j: %p\n", &j);
	
	*j = 7;	// puts 7 inside the memory address that j points to
	printf("j: %d\n", *j);
	free(j);	// frees the memory and avoid memory leaks
	
	return 0;
}
