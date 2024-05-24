#include <stdio.h>

int main(){
	double height;
	double width;

	printf("Rectangle area calculator!\n");
	
	printf("Height(m): ");
	scanf("%10lf", &height);
	
	printf("width(m): ");
	scanf("%10lf", &width);

	printf("Area = %lf square meters\n", height * width);

	return 0;
}
