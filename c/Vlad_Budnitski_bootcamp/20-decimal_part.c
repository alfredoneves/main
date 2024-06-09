#include <stdio.h>

int main(void){
	float num;

	printf("Enter a float number: ");
	scanf("%10f", &num);

	printf("Decimal part = %f", num - (int)num);
	
	return 0;
}
