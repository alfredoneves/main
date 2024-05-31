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

	swap(&a, &b);	// the argument is the memory position
	printf("a = %d\nb = %d", a, b);

	return 0;
}
