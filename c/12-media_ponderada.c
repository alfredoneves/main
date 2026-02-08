#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void){
        float nota_lab, av_semestral, ex_final, nota_final;
        char buffer[10];

        while(1){
                printf("Informe sua nota de laboratório: ");
                fgets(buffer, sizeof(buffer), stdin);
                nota_lab = atof(buffer);

                printf("Informe sua nota da avaliação semestral: ");
                fgets(buffer, sizeof(buffer), stdin);
                av_semestral = atof(buffer);

                printf("Informe sua nota de exame final: ");
                fgets(buffer, sizeof(buffer), stdin);
                ex_final = atof(buffer);

                if(nota_lab >= 0 && av_semestral >= 0 && ex_final >= 0 && nota_lab <= 10 && av_semestral <= 10 && ex_final <= 10){
                        break;
                } else {
                        printf("As notas precisam estar entre 0 e 10!\n");
                }
        }

        nota_final = (nota_lab * 2 + av_semestral * 3 + ex_final * 5) / 10;

        printf("Nota final = %f\n", nota_final);

        if(nota_final >= 8){
                printf("Conceito = A\n");
        } else if(nota_final >= 7){
                printf("Conceito = B\n");
        } else if(nota_final >= 6){
                printf("Conceito = C\n");
        } else if(nota_final >= 5){
                printf("Conceito = D\n");
        } else {
                printf("Conceito = E\n");
        }

        return 0;
}
