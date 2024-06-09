#include <stdio.h>

int main(void){
	char num[] = "123";
	char name[] = "Alfredo";

	printf("%c", name[0]);

	printf("Enter a 3 digits value to be reversed: ");
	fgets(num,4,stdin);

	for (int i = sizeof(num) - 1; i>=0; i--){
		printf("%c", num[i]);
	}

	return 0;
}
