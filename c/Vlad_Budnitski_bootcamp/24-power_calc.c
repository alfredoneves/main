#include <stdio.h>
#include <math.h>

int main(void){
	int x;

	printf("Enter the x: ");
	scanf("%i", &x);

	for(int i = 2; i < 9; i+=2){
		int powx = pow(x, i);
		printf("%i ^ %i = %i\n", x, i, powx);
	}

	return 0;
}
