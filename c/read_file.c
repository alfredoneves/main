#include <stdio.h>

int main(int argc, char *argv[]){
	char line[100];
	FILE *file;	// creates the 
	file = fopen(argv[1], "r");	// opens the file for reading
	
	// validate the input
	if(argc!=2){
		printf("Usage: ./read_file [file_name]\n");
		return 0;
	}else if(file==NULL){
			printf("File not found!\n");
			return 1;
	}
	
	// read the file
	while(fgets(line, sizeof(line), file)){
		printf(line);
	}
	
	return 0;
}
