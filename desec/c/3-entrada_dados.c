#include <stdio.h>
#include <string.h>

int main(void){
	char alvo[20];
	char porta[10];
	
	printf("Digite o alvo:\n");
	fgets(alvo,20,stdin);
	alvo[strcspn(alvo, "\n")] = '\0';
	
	printf("Digite a porta:\n");
	fgets(porta,10,stdin);
	
	printf("Scaneando %s na porta %s\n", alvo,porta);

	return 0;
}
