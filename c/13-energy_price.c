#include <stdio.h>
#include <stdlib.h>

float* calcula_energia(float sal_min, float kw){
        float* arr = malloc(3 * sizeof(float));

        if(arr == NULL){
                return NULL;
        }

        float kwh = sal_min / 1000.0; // KW/h
                                      
        arr[0] = kwh; // price per kilowhat per hour
        arr[1] = kwh * kw; // consumption * price kwh
        arr[2] = kwh * kw * 0.85; // price with discount of 15%

        return arr;
}

int main(void){
        float* prices;
        float sal_min;
        float kw;
        char buffer[10];

        printf("Type the minimum salary:\n");
        fgets(buffer, sizeof(buffer), stdin);
        sal_min = atof(buffer);

        printf("Type the KW consumed:\n");
        fgets(buffer, sizeof(buffer), stdin);
        kw = atof(buffer);

        prices = calcula_energia(sal_min, kw);

        printf("Price per KW: $ %.2f\n", prices[0]);
        printf("Price to pay: $ %.2f\n", prices[1]);
        printf("Price with discount: $ %.2f\n", prices[2]);

        free(prices);
        return 0;
}
