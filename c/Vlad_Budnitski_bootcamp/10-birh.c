#include <stdio.h>
#include <stdlib.h>

int main(){
	int year_of_birth;
	int current_year;
	int age;
	char name[15];

	printf("What's your name? ");
	fgets(name, 15, stdin);

	printf("What year is it? ");
	scanf("%4i", &current_year);

	printf("How old are you? ");
	scanf("%3i", &age);

	year_of_birth = current_year - age;

	printf("Name: %sBorn: %i", name, year_of_birth);

	return 0;
}
