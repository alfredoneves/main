#include <stdio.h>

int main(void){
	double first;
	double second;

	printf("Calculator started!\n");
	printf("Enter the first number: ");
	scanf("%lf", &first);

	printf("Enter the seconds number: ");
	scanf("%lf", &second);

	printf("%lf + %lf = %lf", first, second, (first+second));

	return 0;
}
