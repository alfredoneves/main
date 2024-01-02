#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int main(void){
	unsigned int i = 4;
	unsigned int k;
	char j[3];
	
	
	while (true){
		printf("Guess my number (1-10)\n");
		fgets(j, 3, stdin);
		k = atoi(j);
		
		if ( i == k){
			printf("Right answer!\n");
			break;
		} else if ( i <= k) {
			printf("My number is lower!\n");
		} else {
			printf("My number is bigger!\n");
		}
	}
	
	return 0;
}
