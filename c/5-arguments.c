#include <stdio.h>

int main(int argc, char *argv[]){       // used instead of void to work with arguments

        if(argc != 3){

                printf("Usage: ./arguments IP port\n");

        } else {

                printf("Scanning host %s in port %s\n", argv[1], argv[2]);
                return 0;

        }
}
