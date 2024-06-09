#include <stdio.h>
#include <stdlib.h>

int main(void){
	printf("Verificando portas TCP escutando:\n");
	system("netstat -nlpt");
	return 0;
}
