#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <arpa/inet.h>
#include <netdb.h>

// script da desec para testar vários subdomínios de um alvo e retornar o IP dos encontrados

int main(int argc, char *argv[]){
	char *alvo;
	alvo = argv[1];
	struct hostent *host;
	
	char *result;
	char txt[50];
	FILE *rato;
	rato = fopen(argv[2],"r");	// abre o arquivo passado no segundo argumento para leitura
	
	if(argc < 2){
		printf("Uso: %s [domínio] [arquivo]\n", argv[0]);
		printf("Exp: %s businesscorp.com rato.txt\n", argv[0]);	// rato.txt tem que estar no formato "test."
		return 0;
	}
	
	while(fscanf(rato, "%s", &txt) != EOF){	// EOF = End Of File
		result = (char *) strcat(txt,alvo);	// concatena a linha do txt com o alvo
		host = gethostbyname(result);
		
		if(host==NULL){
			continue;
		}
		
		printf("%s %s\n", result, inet_ntoa(*((struct in_addr *)host->h_addr)));
	}
	
	return 0;
}
