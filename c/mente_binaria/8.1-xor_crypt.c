#include <stdio.h>

int main(void){
	int a = 160;	// value to hide
	int key = 123;	// key
	int b = a ^ key;
	
	printf("original value = %d\n", a);
	printf("encrypted with the key = %d\n", b);
	printf("decrypted with the key = %d\n", b ^ key);
	
	return 0;
}
