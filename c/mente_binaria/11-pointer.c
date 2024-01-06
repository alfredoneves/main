#include <stdio.h>

void my_print(char *s){	// receives a char by accessing the address of a pointer
	while (*s)
		putchar(*s++);
}

int main(void){
	int my_list[] = {2021, 2022, 2023};
	
	/*for (int i=0; i<3; i++){
		printf("%d\n", my_list[i]);
	}*/
	
	printf("%p\n", &my_list);	// address
	printf("%d\n", *my_list + 1);	// value
	
	int j = 2024;
	int *p;	// creating pointer
	p = &j;
	
	printf("The address of j is %p\n", &j);
	printf("The address of p is %p\n", p);
	printf("So they are at the same place in memory, storing %d\n", *p);
	
	// c strings
	
	char name[] = { 0x41, 0x6c, 0x66, 0x72, 0x65, 0x64, 0x6f, 0x0A, 0x00 };
	char n[] = "Alfredo"; 
	my_print(name);
	
	return 0;
}
