#include <stdio.h>

int main(void){
	int a = 7;
	int *pa = &a;	// pointer to the memory address of a

	printf("pa = %d\n", *pa);
	printf("&a = %p\n", &a);

	return 0;
}
