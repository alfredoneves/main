#include <stdio.h>

int main(void){
	int a, b, c;

	printf("enter grade 1: ");
	scanf("%2i", &a);
	printf("enter grade 2: ");
	scanf("%2i", &b);
	printf("enter grade 3: ");
	scanf("%2i", &c);

	printf("average = %lf\n", (a + b + c) / 3.0 );

	return 0;
}
