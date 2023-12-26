#include <stdio.h>

int main(void){
	int a = 2;	// 10
	int b = 3;	// 11
	// 	   a & b = 10
	//	   a | b = 11
	//     a ^ b = 01
	
	// int has 32 bits and is signed
	int c = 0b00000000000000000000000000000000;	// 0
	int d = 0b11111111111111111111111111111111; // -1
	int e = 0b1000;	// 8
	
	printf("2 & 3 = %d\n", a & b);
	printf("2 | 3 = %d\n", a | b);
	printf("2 ^ 3 = %d\n", a ^ b);
	printf("~0 = %d\n", ~c);
	printf("8 << 1 = %d\n", e << 1);
	printf("8 >> 1 = %d\n", e >> 1);
	return 0;
}
