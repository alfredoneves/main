#include<stdio.h>

int main() {
	float precoFabrica, lucro, impostos, precoFinal;
    	float percentualLucro, percentualImpostos;

    	scanf("%f", &precoFabrica);
    	scanf("%f", &percentualLucro);
    	scanf("%f", &percentualImpostos);
	
	lucro = precoFabrica * percentualLucro / 100;
	printf("Lucro: R$ %.2f\n", lucro);
    
    	impostos = precoFabrica * percentualImpostos / 100;
	printf("Impostos: R$ %.2f\n", impostos);
	
	precoFinal = precoFabrica + lucro + impostos;
	printf("Preco final: R$ %.2f\n", precoFinal);
	
    	getchar();
    	return 0;
}
