#include <stdio.h>

int main(void){
	float speed;
	float distance;
	float hours;
	float remaining_minutes;

	printf("Enter the distance between the points (Km): ");
	scanf("%10f", &distance);

	printf("Enter the speed (Km/h): ");
	scanf("%10f", &speed);

	hours = distance / speed;
	remaining_minutes = (hours - (int)hours) * 60;
	
	printf("You will get there in %.0f hour(s) and %.0f minutes\n", hours, remaining_minutes);

	return 0;
}
