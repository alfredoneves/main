#include <stdio.h>

int main(void){
	int port = 80;
	char ip[] = "192.168.0.1";	// the number of bytes of the variable can be specified in the []
	float version = 1.0;
	
	printf("scanning ...\n");
	printf("scan version: %.1f\n",version);	// .1 for the number of decimals
	printf("scanning ip: %s in the port: %i\n",ip, port);

	return 0;
}
