#include <stdio.h>

int main(void){
	float salary_ph;
	float hours;
	float total_salary;

	printf("Enter the salary per hour: ");
	scanf("%10f", &salary_ph);

	printf("Enter the hours worked in the month: ");
	scanf("%3f", &hours);

	total_salary = salary_ph * hours;
	printf("Total salary = %.2f USD\n", total_salary);

	return 0;
}
