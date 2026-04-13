#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void xor_encrypt(char *text, char *key, char *output) {
    int text_len = strlen(text);
    int key_len = strlen(key);

    for (int i = 0; i < text_len; i++) {
        output[i] = text[i] ^ key[i % key_len]; // this part repeats the key untill all the text is encrypted
    }
}

int main(void){
    char text[100];
    char key[20];
    char cipher_text[100];

    printf("Enter text: ");
    fgets(text, sizeof(text), stdin);

    printf("Enter key: ");
    fgets(key, sizeof(key), stdin);

    if(key[0] == '\n'){
        printf("A key must be provided!\n");
        return 1;
    }

    // Remove newline characters
    text[strcspn(text, "\n")] = '\0';
    key[strcspn(key, "\n")] = '\0';

    xor_encrypt(text, key, cipher_text); // now the var cipher_text has raw bytes
    
    for(int i = 0; i < strlen(text); i++){ // I used strlen(text) because cipher_text has raw bytes and can break the strlen, but they are the same size
        printf("%02X ", (unsigned char)cipher_text[i]);
    }

    printf("\n"); // just adding a new line to the output

    return 0;
}
