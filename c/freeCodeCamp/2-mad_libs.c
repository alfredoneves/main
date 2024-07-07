#include <stdio.h>

int main(void){
	char color[15];
	char plural_noun[15];
	char name[30];

	printf("Enter a color: ");
	scanf("%14s", &color);
	
	printf("Enter a plural noun: ");
	scanf("%14s", &plural_noun);
	getchar();	// receives the \n that is left by scanf

	printf("Enter a name: ");
	fgets(name, 30, stdin);

	printf("Roses are %s\n", color);
	printf("%s are blue\n", plural_noun);
	printf("I love %s\n", name);

	return 0;
}
