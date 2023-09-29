#include <stdio.h>
#include <stdlib.h>     // lib that has the "system" command

int main(void){
        char command[20];

        printf("Type a system command to be executed:\n");
        fgets(command, 20, stdin);
        system(command);        // executes the command

        return 0;
}
