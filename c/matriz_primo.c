#include <stdio.h>
#include <stdlib.h>

int verifica_primo(int j){
        if(j == 0 || j == 1){
                return 0;
        }

        for(int k = 2; k < j; k++){
                if(j % k == 0){
                        return 0;
                }
        }

        return 1;
}

int main(){
        int vetor[9];
        char buffer[10];

        for(int i = 0; i < 9; i++){
                printf("Insira o dado da posição %i:\n", i);
                fgets(buffer, sizeof(int), stdin);
                vetor[i] = atoi(buffer);
        }

        for(int i = 0; i < 9; i++){
                if(verifica_primo(vetor[i])){
                        printf("%i é primo, pos: %i\n", vetor[i], i);
                }
        }


        return 0;
}
