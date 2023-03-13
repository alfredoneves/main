#include <stdio.h>
#include <sys/socket.h>
#include <netdb.h>

// man 7 ip
// man socket
// cat /etc/protocols

int main(void){
	int socket0;
	int connect0;
	
	struct sockaddr_in target;	// creates the target to connect
	socket0 = socket(AF_INET, SOCK_STREAM,0);	// defines IPV4, TCP and IP (check manual)
	
	target.sin_family = AF_INET;
	target.sin_port = htons(80);
	target.sin_addr.s_addr = inet_addr("192.168.0.1");
	
	connect0 = connect(socket0, (struct sockaddr *)&target, sizeof target);	// starts connection
	
	if(connect0 == 0){	// connect0 receives 0 if the connection is ok
		printf("Port open\n");
		close(socket0);
		close(connect0);
	}else {
		printf("Port closed\n");
	}
	
	return 0;
}
