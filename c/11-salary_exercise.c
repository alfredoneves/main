#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void){
        float salario;
        float aumento;
        char nome[30];
        char buffer[15];
        printf("Qual o nome do funcionário?\n");
        fgets(nome, sizeof(nome), stdin);
        nome[strcspn(nome, "\n")] = '\0';

        printf("Qual o salário do funcionário em reais (exp: 3400.50)?\n");
        fgets(buffer, sizeof(buffer), stdin);
        salario = atof(buffer);

        printf("Qual o aumento de salário em percentual (10, 50, 70)?\n");
        fgets(buffer, sizeof(buffer), stdin);
        buffer[strcspn(buffer, "%")] = '\0';
        aumento = atof(buffer);


        printf("Funcionário: %s\n", nome);
        printf("Salário: %.2f reais\n", salario);
        printf("Aumento: %.2f %\n", aumento);
        printf("Novo salário: %.2f\n", salario * (aumento + 100) / 100);

        return 0;
}
