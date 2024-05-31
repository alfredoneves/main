#include <stdio.h>

int main(void){
	double c_temp, f_temp;

	printf("Enter the temperature in Celsius: ");
	scanf("%4lf", &c_temp);

	f_temp = c_temp * 1.8 + 32;
	printf("Fahrenheit: %lf\n", f_temp);
	return 0;
}
