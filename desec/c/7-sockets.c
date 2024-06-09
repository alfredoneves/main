#include <stdio.h>
#include <sys/socket.h>
#include <netdb.h>

int main(int argc, char *argv[]){
	int meusocket;
	int conecta;
	struct sockaddr_in alvo;
	char *ip;
	int porta;
	
	if(argc < 3){
		printf("Uso: %s [IP] [PORTA]\n", argv[0]);
		printf("Exemplo: %s 192.168.0.1 80\n", argv[0]);
		return 0;
	}
	
	ip = argv[1];
	porta = atoi(argv[2]);
	
	meusocket = socket(AF_INET, SOCK_STREAM,0);
	alvo.sin_family = AF_INET;
	alvo.sin_port = htons(porta);
	alvo.sin_addr.s_addr = inet_addr(ip);
	
	conecta = connect(meusocket, (struct sockaddr *)&alvo, sizeof alvo);
	
	if(conecta == 0){
		printf("Porta %i aberta\n", porta);
	}
	
	return 0;
}
