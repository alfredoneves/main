#include <stdio.h>
#include <stdlib.h>
#include "lib/petest.h"

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

	if (argc != 2){
		usage();
	}
	/*typedef struct {
        	char *filepath;
        	IMAGE_DOS_HEADER *hdr_dos;
	} PEFILE; */

	PEFILE pe;
	pe.filepath = argv[1];
	petest_init(&pe);
	
	if (petest_ispe(&pe))
		printf("PE identificado...\n");
	else
		fatal("O arquivo não é um PE\n");

	printf("File: %s\n", pe.filepath);
	printf("Magic bytes: %x\n", pe.hdr_dos->e_magic);
	printf("COFF header: %x\n", pe.hdr_dos->e_lfanew);

	petest_deinit(&pe);

	return 0;
}
