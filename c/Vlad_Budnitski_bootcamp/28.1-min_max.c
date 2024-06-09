#include <stdio.h>

int main(void){
	int numbers[3];

	// filling the array
	for (int i = 0; i < 3; i++){
		printf("Enter the value %i: ", i+1);
		scanf("%10i", &numbers[i]);	
	}

	// getting the size of the array and preparing max and min
	int arr_size = sizeof(numbers) / sizeof(numbers[0]);
	int max = 0;
	int min = 0;

	for (int i = 0; i < arr_size; i++){
		if (numbers[i] > max || i == 0){
			max = numbers[i];
		}

		if (numbers[i] < min || i == 0){
			min = numbers[i];
		}
	}

	printf("Max: %i\n", max);
	printf("Min: %i\n", min);

	return 0;
}
