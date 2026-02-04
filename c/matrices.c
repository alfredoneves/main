#include <stdio.h>

int main(void){
        int mat[3][3];

        for(int l=0; l<3; l++){
                for(int c=0; c<3; c++){
                        mat[l][c] = c + (l * 3);
                }
        }

        for(int l=0; l<3; l++){
                for(int c=0; c<3; c++){
                        printf("%i ", mat[l][c]);
                }

                printf("\n");
        }


        return 0;
}
