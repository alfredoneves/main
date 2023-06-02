#include<stdio.h>

int main() {
    	float salarioBase, gratificacao, imposto, salarioFinal;
    	printf("salario base:");
    	scanf("%f", &salarioBase);
	gratificacao = 0.05;
	imposto = 0.07;
    	//TODO: Calcule a gratificação, o imposto e o salário final. Em seguida print no console o salário final.
        salarioFinal = salarioBase * (1 - (imposto - gratificacao));
        printf("Salario final: %.2f", salarioFinal);
    	getchar();
    	return 0;
}
