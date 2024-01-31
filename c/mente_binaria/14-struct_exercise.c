#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct st {
	float height;
	float weight;
	char *name;	// you need to use pointer because you can't make an assignment to an array
};

int main(void) {
	struct st imc;
	char name[16];
	char weight[6];
	char height[5];
	
	printf("Name:");
	fgets(name, 16, stdin);
	printf("Weight:");
	fgets(weight, 6, stdin);
	printf("Height:");
	fgets(height, 5, stdin);
	
	imc.name = name;
	imc.weight = atof(weight);
	imc.height = atof(height);

	printf("Name = %s", name);
	printf("Height = %f\n", imc.height);
	printf("Weight = %f\n", imc.weight);
	printf("IMC = %f\n", (imc.weight / pow(imc.height,2)));

	return 0;
}
