#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){
	
	if(argc<2){
		printf("Uso: %s [REDE_ALVO]\n", argv[0]);
		printf("Exp: %s 192.168.0\n", argv[0]);
		exit(1);
	}
	
	for(int i=0;i<=10;i++){
		printf("Varrendo alvo: %s.%i\n",argv[1],i);
	}
	
	
	
	return 0;
}
