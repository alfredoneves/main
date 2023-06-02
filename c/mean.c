#include<stdio.h>

int main() {
    float a, b, c, media;

    scanf("%f", &a);
    scanf("%f", &b);
    scanf("%f", &c);

    media = (a + b + c) / 3;
    printf("%f", media);
    getchar();
    return 0;
}
