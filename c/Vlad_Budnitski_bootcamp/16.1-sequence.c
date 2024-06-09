#include <stdio.h>

int main(void){
	float initial;
	float final;
	int number_terms;
	float the_sum;

	printf("Enter the initial value: ");
	scanf("%10f", &initial);

	printf("Enter the final value: ");
	scanf("%10f", &final);

	printf("Enter the number of terms: ");
	scanf("%9i", &number_terms);

	the_sum = (initial + final) * ((float) number_terms / 2); 

	printf("a1 = %f\n", initial);
	printf("n_th = %f\n", final);
	printf("number of terms = %i\n", number_terms);
	printf("sum = %f\n", the_sum);
	return 0;
}
