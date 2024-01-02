#include <stdio.h>

int main(void){
	unsigned int i = 0;
	
	my_label:	// creates a label to be executed, this is a form of loop
		printf("i = %u\n", i);
		i++;
		if (i < 3)
			goto my_label;

	for (unsigned int j = 0; j < 3; j++){	// we can declare the variable here to save memory
		printf("j = %u\n", j);
	}
	
	printf("%u\n", i);	// prints i because it's in the main
	// printf("%u\n", j);	throws an error because variable j is local
	
	return 0;
}
