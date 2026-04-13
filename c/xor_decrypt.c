#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void xor_decrypt(char *cypher_text, int text_len, char *key, char *output){
    int key_len = strlen(key);

    for(int i = 0; i < text_len; i++){
        output[i] = cypher_text[i] ^ key[i % key_len];
    }

    output[text_len] = '\0';
}

int main(){
    char cypher_hex[200];   // bigger to support spaces
    char cypher_text[100];
    char key[20];
    char output[100];

    printf("Enter cypher text (hex): \n");
    fgets(cypher_hex, sizeof(cypher_hex), stdin);
    cypher_hex[strcspn(cypher_hex, "\n")] = '\0';

    printf("Enter the key: \n");
    fgets(key, sizeof(key), stdin);

    if(key[0] == '\n'){
        printf("You must enter the key!\n");
        return 1;
    }

    key[strcspn(key, "\n")] = '\0';

    //  Convert HEX (with spaces) → raw bytes
    int j = 0;

    for (int i = 0; cypher_hex[i] != '\0'; ) {
        // skip spaces
        if (cypher_hex[i] == ' ') {
            i++;
            continue;
        }

        // ensure we have two hex chars
        if (cypher_hex[i + 1] == '\0') {
            printf("Invalid hex input!\n");
            return 1;
        }

        char byte_str[3];
        byte_str[0] = cypher_hex[i];
        byte_str[1] = cypher_hex[i + 1];
        byte_str[2] = '\0';

        cypher_text[j++] = (char) strtol(byte_str, NULL, 16);

        i += 2;
    }

    int byte_len = j;

    xor_decrypt(cypher_text, byte_len, key, output);

    printf("Clear text:\n");
    printf("%s\n", output);

    return 0;
}
