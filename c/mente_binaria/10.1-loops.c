#include <stdio.h>

int main(void){
	unsigned int j = 0;
	
	// break example
	for (unsigned int i = 0; ; i++){
		printf("%u\n", i);
		
		if (i > 2){
			break;
		}
	}
	
	while (j < 3){
		printf("j = %u\n", j++);
	}
	
	do
		printf("j = %u\n", j);
	while (j < 3);
	
	return 0;
}
