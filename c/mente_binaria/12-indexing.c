#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
	char s[10] = "Alfredo";
	
	printf("%x\n", s[20]);	// prints the value that in the memory location of s+20
	printf("%x\n", *(s+20));	// does the same
	
	return 0;
}
