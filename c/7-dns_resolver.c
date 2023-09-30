#include <stdio.h>
#include <netdb.h>	// consults dns
#include <arpa/inet.h>	// translates the results of gethostbyname to human readable

int main(int argc, char *argv[]){
	// get the hostname
	if(argc!=2){
		printf("Use mode: ./dns_resolver [address]\n");
		return 0;
	}
	
	struct hostent *alvo = gethostbyname(argv[1]);	// dns query
	
	if(alvo == NULL){	// in case of error in the target specification a null result is returned to alvo
		printf("address error\n");
	}else{
		printf("IP: %s\n", inet_ntoa(*((struct in_addr *)alvo->h_addr)));	// dns translation
	}
	
	return 0;
}
