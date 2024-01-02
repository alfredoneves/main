#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main(void){
	int flag = 18;
	char age[4];
	bool war = false;
	
	printf("How old are you?\n");
	fgets(age, 4, stdin);
	
	int int_age = atoi(age);	// transforming the age into an integer
	
	if (int_age >= 18 || war){
		printf("Welcome to the army!");
	} else {
		printf("You're free to go!");
	}

	return 0;
}
