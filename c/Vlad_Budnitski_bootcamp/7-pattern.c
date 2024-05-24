#include <stdio.h>

int main(){
	char *s[5];

	s="a";

	for(int i=0;i<5;i++){
		for(int j=0;j<10;j++){
			printf("*");
		}
		printf("\n");
	}

	return 0;
}
