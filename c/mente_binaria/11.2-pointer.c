#include <stdio.h>

int main(int argc, char *argv[]) {
    // Calculate the number of elements in the array
    int arraySize = 0;
    while (argv[arraySize] != NULL) {
        arraySize++;
    }

    // Print the number of elements
    printf("Number of elements in the array: %d\n", arraySize);

    // You can also access the elements of the array using argv[i]
    for (int i = 0; i < arraySize; i++) {
        printf("Element %d: %s\n", i, argv[i]);
    }

    return 0;
}
