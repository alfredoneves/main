#include <stdio.h>
#include <stdlib.h>

#define K 4
enum pieces { TOWER, HORSE, BISHOP };	// creates an enumeratin

int main(int argc, char *argv[]) {
	int table[K][K] = { 0 };	// creates an empty matrix
	int i, j;
	
	table[0][0] = TOWER;
	table[1][0] = BISHOP;
	
	for (i=0; i<K; i++){
		for (j=0; j<K; j++) {
			printf("[%d][%d]=%d ", i, j, table[i][j]);
			if (j == K-1) {
				printf("\n");
			}
		}
	}

	return 0;
}
