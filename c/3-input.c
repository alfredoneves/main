#include <stdio.h>

int main(void){
	int port;
	char ip[16];
	
	printf("IP:");
	fgets(ip,16,stdin);
	
	printf("Port:");
	scanf("%i",&port);
	
	printf("scanning %s in port %i",ip,port);
	return 0;
}
