#include <stdio.h>

int main(void){
	char grade;

	printf("Enter your grade (A,B,C,D,F): ");
	scanf("%1c", &grade);

	switch (grade) {
		case 'A':
			printf("Grade between 90-100\n");
			break;
		case 'B':
			printf("Grade between 80-89\n");
			break;
		case 'C':
			printf("Grade between 70-79\n");
			break;
		case 'D':
			printf("Grade between 60-69\n");
			break;
		case 'F':
			printf("Grade below 60\n");	
			break;
		default:
			printf("Invalid grade!\n");
	}
}
