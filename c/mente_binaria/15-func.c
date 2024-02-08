#include <stdio.h>
#include <stdlib.h>

int my_sum(int n1, int n2, int n3) {
	return n1 + n2 + n3;
}

void error(char msg[]) {
	fprintf(stderr, "%s\n", msg);	// used to output error in stderr or 2>
	exit(1);
}
int main(void) {
	char n1[5];
	char n2[5];
	char n3[5];
	
	printf("Type the value of n1: ");
	fgets(n1, 5, stdin);
	error("error code some_code_here");
	printf("Type the value of n2: ");
	fgets(n2, 5, stdin);
	printf("Type the value of n3: ");
	fgets(n3, 5, stdin);
	
	printf("Sum = %i\n", my_sum(atoi(n1), atoi(n2), atoi(n3)));
	
	return 0;
}
