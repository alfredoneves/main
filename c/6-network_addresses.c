#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){	// permits the use of arguments
	int i;
	char *ip;
	ip = argv[1];
	if(argc<2){
		printf("you need to give the ip corresponding the netmask\n");
		printf("example: ./ping_sweep 192.168.0\n");
	}else{
		printf("addresses in the network ...\n");
		for(i=0;i<=255;i++){
			printf("%s.%i\n",ip,i);
		}
	}
}
