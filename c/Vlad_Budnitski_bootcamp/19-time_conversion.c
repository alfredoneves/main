#include <stdio.h>

int main(void){
	int time;
	int hours;
	int minutes;
	int seconds;

	printf("Enter the total of seconds: ");
	scanf("%10i", &time);

	hours = time / 3600;
	minutes = (time - hours * 3600) / 60;
	seconds = (time - hours * 3600) % 60;
	
	printf("hours: %i\n", hours);
	printf("minutes: %i\n", minutes);
	printf("seconds: %i\n", seconds);

	return 0;
}
