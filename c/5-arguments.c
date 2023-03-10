#include <stdio.h>

int main(int argc, char *argv[]){	// permits the use of arguments
	if(argc<2){
		printf("you need to give 2 arguments\n");
		printf("example: ./arguments [ip] [port]\n");
	}else{
		printf("scanning host %s in port %s\n",argv[1], argv[2]);
		return 0;
	}
}
