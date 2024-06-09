#include <stdio.h>
#include <math.h>

int main(void){
	float x1,y1,x2,y2;
	
	printf("Difference between points calculator!\n");
	
	printf("Enter the value x for point 1: ");
	scanf("%f", &x1);
	
	printf("Enter the value y for point 1: ");
	scanf("%f", &y1);
	
	printf("Enter the value x for point 2: ");
	scanf("%f", &x2);

	printf("Enter the value y for point 2: ");
	scanf("%f", &y2);

	printf("The distance between points 1 and 2 is %f", pow(pow(x1-x2, 2) + pow(y1-y2, 2), 0.5));
	return 0;
}
