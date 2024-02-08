#include <stdio.h>

#define square(x) (x*x)

int main(void) {
	int i = 10;
	
	printf("i=10\ni**2=%d\n", square(i));

	printf("%s\n", __TIME__);
	
	printf("%s\n", __unix__);
	
	return 0;
}
