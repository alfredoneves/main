#include <stdio.h>

int main(void){
	int num;

	printf("Enter the value: ");
	scanf("%10i", &num);

	if (num % 2){
		printf("The number %i is odd\n", num);
	} else {
		printf("The number %i is even\n", num);
	}

	return 0;
}
