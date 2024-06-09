#include <stdio.h>

int main(void){
	int num1, num2;

	printf("Enter the number 1: ");
	scanf("%10i", &num1);
	printf("Enter the number 2: ");
	scanf("%10i", &num2);

	if (num1 > num2){
		printf("Max = %i\n", num1);
	} else if (num2 > num1){
		printf("Max = %i\n", num2);
	} else {
		printf("The numbers are equal!\n");
	}
	
	return 0;
}
