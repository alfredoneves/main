#include <stdio.h>
#include <stdlib.h>

enum Day { SUN, MON, TUE, WED, THU, FRI, SAT };

int main(){
        enum Day today = THU;

        printf("Today code = %d\n", today);

        switch(today){
                case 0:
                        printf("Today = Sunday\n");
                        break;
                case 1:
                        printf("Today = Monday\n");
                        break;
                case 2:
                        printf("Today = Tuesday\n");
                        break;
                case 3:
                        printf("Today = Wednesday\n");
                        break;
                case 4:
                        printf("Today = Thursday\n");
                        break;
                case 5:
                        printf("Today = Friday\n");
                        break;
                case 6:
                        printf("Today = Saturday\n");
                        break;
        }

        return 0;
}
