#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Pessoa{
        char nome[20];
        int idade;
        float peso;
        float altura;
};

int main(){
        struct Pessoa pessoas[3];
        char buffer[20];

        for(int i = 0; i < 3; i++){
                printf("Digite o nome da pessoa %i:\n", i);
                fgets(buffer, sizeof(buffer), stdin);
                strcpy(pessoas[i].nome, buffer);

                printf("Digite a idade da pessoa %i:\n", i);
                fgets(buffer, sizeof(buffer), stdin);
                pessoas[i].idade = atoi(buffer);

                printf("Digite o peso (Kg) da pessoa %i:\n", i);
                fgets(buffer, sizeof(buffer), stdin);
                pessoas[i].peso = atof(buffer);

                printf("Digite a altura (m) da pessoa %i:\n", i);
                fgets(buffer, sizeof(buffer), stdin);
                pessoas[i].altura = atof(buffer);
        }

        printf("O nome da primeira pessoa é %s", pessoas[0].nome);
        printf("A idade da segunda pessoa é %i\n", pessoas[1].idade);
        printf("O peso da terceira pessoa é %.2f Kg\n", pessoas[2].peso);

        return 0;
}
