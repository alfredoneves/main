#include <stdio.h>
#include <stdlib.h>
#include "lib/petest.h"

// esse arquivo apenas verifica se outro arquivo é um PE, deixei salvo como backup

void usage(){
	printf("Uso: readpe <arquivo.exe>\n");
	fatal(NULL);
}

void fatal(char *msg){
	if (msg != NULL){
		fprintf(stderr, "Erro: %s\n", msg);
	}

	exit(1);
}

int main(int argc, char *argv[]){
	FILE *fh;
	unsigned char buffer[32];	// prepara um buffer de 32 bytes para ler o arquivo

	if (argc != 2){
		usage();
	}
	
	fh = fopen(argv[1], "rb");
	
	if (fh == NULL){
		fatal("Arquivo não encontrado ou sem permissão de leitura\n");
	}	

	if(fread(buffer, 32, 1, fh) != 1){	// fread retorna o número de blocos lidos
		fatal("Não foi possível ler os 32 bytes do arquivo\n");
	}	

	fclose(fh);

	if (!petest_ispe(buffer))
		fatal("O arquivo informado não parece ser um executável\n");
	
	return 0;
}
