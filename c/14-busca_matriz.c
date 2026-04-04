#include <stdio.h>
#include <stdlib.h>

int main(){
        int matriz[3][3];
        int chave;
        char buffer[5];

        for(int i = 0; i < 3; i++){
                for(int j = 0; j < 3; j++){
                        printf("Forneça o número para a matriz na posição [%i][%i]\n", i, j);
                        fgets(buffer, sizeof(int), stdin);
                        matriz[i][j] = atoi(buffer);
                }
        }

        printf("Forneça a chave de busca:\n");
        fgets(buffer, sizeof(int), stdin);
        chave = atoi(buffer);

        for(int i = 0; i < 3; i++){
                for(int j = 0; j < 3; j++){
                        if(matriz[i][j] == chave){
                                printf("matriz[%i][%i] = %i\n", i, j, chave);
                                return 0;
                        }
                }
        }

        printf("Chave não encontrada!\n");


        return 0;
}
