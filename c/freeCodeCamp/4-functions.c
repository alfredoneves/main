#include <stdio.h>

void say_hi(char name[15], char country[15]){
	printf("Hello %s from %s\n", name, country);
}

int main(void){
	say_hi("Mike", "UK");
	say_hi("Giuseppe", "France");

	return 0;
}
