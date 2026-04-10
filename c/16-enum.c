#include <stdio.h>
#include <stdlib.h>

int main(){
        // enum is used to create an array of constants
        // it's useful to give values to days, months, colors etc
        enum Level{
                LOW = 10,
                MEDIUM = 50,
                HIGH = 100
        };

        // we must create a variable and assign a value from the enum to it
        enum Level ricky_lv = HIGH;

        printf("Ricky level = %d\n", ricky_lv);

        switch(ricky_lv){
                case 10:
                        printf("Low level\n");
                        break;
                case 50:
                        printf("Medium level\n");
                        break;
                case 100:
                        printf("High level\n");
                        break;
        }

        return 0;
}
