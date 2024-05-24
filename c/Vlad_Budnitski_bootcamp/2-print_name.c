#include <stdio.h>

int main(){
	char name[15];
	char surname[15];
	char sex[8];

	printf("Whats is your name? ");
	fgets(name,15,stdin);
	
	printf("What is your surname? ");
	fgets(surname,15,stdin);
	
	printf("What is your sex? ");
	fgets(sex,8,stdin);

	printf("Name: %sSurname: %sSex: %s",name,surname,sex);

	return 0;
}
