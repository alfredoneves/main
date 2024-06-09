#include <stdio.h>

int main(void){
	float num1, num2;

	printf("Enter the number 1: ");
	scanf("%10f", &num1);
	printf("Enter the number 2: ");
	scanf("%10f", &num2);

	if (num1 > num2){
		printf("maximum: %f\n", num1);
		printf("minimum: %f\n", num2);
	} else if (num1 == num2){
		printf("The numbers are equal!\n");
	} else {
		printf("maximum: %f\n", num2);
		printf("minimum: %f\n", num1);
	}

	return 0;
}
