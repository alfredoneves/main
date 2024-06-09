#include <stdio.h>
#include <sys/socket.h>
#include <netdb.h>
#include <errno.h>
#include <arpa/inet.h>
#include <fcntl.h>
#include <unistd.h> // For `close()`
#include <sys/select.h> // For `select()`
#include <string.h> // For `memset()`

int main(int argc, char *argv[]){
	int meusocket;
    struct sockaddr_in alvo;
    struct timeval timeout; // timeout 
    char *ip;
    int portas[] = {21, 22, 25, 80, 139, 443, 445, 2222, 3306, 3389, 4444, 8080};
	int conecta;
	
    if (argc < 2) {
        printf("Usage: %s [IP]\n", argv[0]);
        printf("Example: %s 192.168.0.1\n", argv[0]);
        return 0;
    }

    ip = argv[1];

    for (int i = 0; i < sizeof(portas) / sizeof(portas[0]); i++) {
    	
        meusocket = socket(AF_INET, SOCK_STREAM, 0);
        if (meusocket < 0) {
            perror("Error creating socket");
            continue;
        }

        // Set non-blocking mode
        int flags = fcntl(meusocket, F_GETFL, 0);
        if (flags < 0 || fcntl(meusocket, F_SETFL, flags | O_NONBLOCK) < 0) {
            perror("Error setting non-blocking mode");
            close(meusocket);
            continue;
        }

        // Configure the target address
        memset(&alvo, 0, sizeof(alvo)); // Initialize the structure
        alvo.sin_family = AF_INET;
        alvo.sin_port = htons(portas[i]);
        alvo.sin_addr.s_addr = inet_addr(ip);

        conecta = connect(meusocket, (struct sockaddr *)&alvo, sizeof(alvo));
		
        // If connect is not yet completed and errno is EINPROGRESS, use `select()`
        if (conecta < 0 && errno == EINPROGRESS) {
			fd_set write_fds;
            FD_ZERO(&write_fds);
            FD_SET(meusocket, &write_fds);

            timeout.tv_sec = 2; // 2 seconds timeout
            timeout.tv_usec = 0;

            int ready = select(meusocket + 1, NULL, &write_fds, NULL, &timeout);

            if (ready > 0 && FD_ISSET(meusocket, &write_fds)) {
                // Check if the connection was successful
                int error = 0;
                socklen_t len = sizeof(error);
                getsockopt(meusocket, SOL_SOCKET, SO_ERROR, &error, &len);

                if (error == 0) {
                    printf("Port %d is open\n", portas[i]);
                }
			} else if (conecta == 0) { // Direct successful connection
				printf("Port %d is open\n", portas[i]);
			}

        close(meusocket);	// Close the socket after each attempt
		}
	}
	return 0;
}
