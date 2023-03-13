#include <stdio.h>
#include <sys/socket.h>
#include <netdb.h>

// man 7 ip
// man socket
// cat /etc/protocols

int main(int argc, char *argv[]){
	int socket0;
	int connect0;
	int port;
	int end=65535;
	char *host;
	host=argv[1];
	
	struct sockaddr_in target;	// creates the target to connect
	
	for(port=0;port<=end;port++){
		socket0 = socket(AF_INET, SOCK_STREAM,0);	// defines IPV4, TCP and IP (check manual)
		target.sin_family = AF_INET;
		target.sin_port = htons(port);
		target.sin_addr.s_addr = inet_addr(host);
		
		connect0 = connect(socket0, (struct sockaddr *)&target, sizeof target);	// starts connection
		
		if(connect0 == 0){	// connect0 receives 0 if the connection is ok
			printf("Port %d open\n",port);
			close(socket0);
			close(connect0);
		}else {
			close(socket0);
			close(connect0);
		}
	}
	
	
	return 0;
}
