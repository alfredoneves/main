#include <stdio.h>

int swap(int *pa, int *pb){
	int t = *pa;
	*pa = *pb;
	*pb = t;
	return 0;
}

int main(void){
	int a = 21;
	int b = 17;
	
	printf("original values:\n");
	printf("a = %d\nb = %d\n", a, b);
	
	swap(&a, &b);	// the argument is the memory position
	printf("after the swap:\n");
	printf("a = %d\nb = %d\n", a, b);

	return 0;
}
