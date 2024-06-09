#include <stdio.h>

int main(void){
	int num;
	int num1, num2, num3;

	printf("Enter a number with 3 digits: ");
	scanf("%3i", &num);

	num1 = num / 100;
	num2 = (num - num1 * 100) / 10;
	num3 = num - (num1 * 100 + num2 * 10);
	
	printf("num = %i\n", num);
	printf("num1 = %i\n", num1);
	printf("num2 = %i\n", num2);
	printf("num3 = %i\n", num3);
	printf("num1 + num2 + num3 = %i\n", num1 + num2 + num3);

	return 0;
}
