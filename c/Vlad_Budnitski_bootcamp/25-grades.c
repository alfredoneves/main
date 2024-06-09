#include <stdio.h>

int main(void){
	float grade;

	printf("Enter your grade: ");
	scanf("%f", &grade);

	if (grade >= 7){
		printf("Congratulations!\n");
	} else {
		printf("You failed!\n");
	}

	return 0;
}
