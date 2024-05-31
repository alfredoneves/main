#include <stdio.h>

int main(void){
	double c_temp, f_temp;

	printf("Enter the temperature in Fahrenheit: ");
	scanf("%lf", &f_temp);

	c_temp = (f_temp - 32) / 1.8;
	printf("Celsius temperature: %lf\n", c_temp);
	return 0;
}
