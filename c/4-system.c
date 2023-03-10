#include <stdio.h>
#include <stdlib.h>

int main(void){
	printf("checking open TCP ports:\n");
	system("netstat -nlpt");
	return 0;
}
