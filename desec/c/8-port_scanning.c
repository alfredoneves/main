#include <stdio.h>
#include <sys/socket.h>
#include <netdb.h>
#include <errno.h>
#include <time.h>	// timeout
#include <fcntl.h>	// evitar ficar preso na porta aberta

int main(int argc, char *argv[]){
	int meusocket;
	int conecta;
	struct sockaddr_in alvo;
	struct timeval timeout;	// timeout 
	char *ip;
	int portas[] = {21,22,25,80,139,443,445,2222,3306,3389,4444,8080};
	
	if(argc < 2){
		printf("Uso: %s [IP]\n", argv[0]);
		printf("Exemplo: %s 192.168.0.1\n", argv[0]);
		return 0;
	}
	
	ip = argv[1];
	
	for(int i=0;i<sizeof(portas);i++){
		printf("ok\n");
		meusocket = socket(AF_INET, SOCK_STREAM,0);
		alvo.sin_family = AF_INET;
		alvo.sin_port = htons(portas[i]);
		alvo.sin_addr.s_addr = inet_addr(ip);
		
		// timeout
		timeout.tv_sec = 2;
		if(setsockopt(meusocket, SOL_SOCKET, SO_RCVTIMEO, &timeout, sizeof(timeout)) < 0) {
            perror("Error setting receive timeout");
            close(meusocket);
            continue;
        }
        
		conecta = connect(meusocket, (struct sockaddr *)&alvo, sizeof alvo);
            
		if(conecta == 0){
			printf("Porta %i aberta\n", portas[i]);
			close(meusocket);
			close(conecta);
		} else {
			close(meusocket);
			close(conecta);
		}
	}
	
	return 0;
}
