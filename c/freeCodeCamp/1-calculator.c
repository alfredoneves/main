#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
  char buffer[10];
  char operator[3];
  int num1, num2;

  printf("Calculator started!\n");

  printf("Type the operation (+, - , *, /): ");
  fgets(operator, sizeof(operator), stdin);
  operator[strcspn(operator, "\n")] = '\0';

  printf("Type the first number: ");
  fgets(buffer, sizeof(buffer), stdin);
  num1 = atoi(buffer);

  printf("Type the second number: ");
  fgets(buffer, sizeof(buffer), stdin);
  num2 = atoi(buffer);

  printf("%i %s %i = ", num1, operator, num2);

  if(strcmp(operator, "+") == 0){
        printf("%i\n", num1 + num2);
  } else if(strcmp(operator, "-") == 0){
        printf("%i\n", num1 - num2);
  } else if(strcmp(operator, "*") == 0){
        printf("%i\n", num1 * num2);
  } else {
        if(num2 == 0){
                printf("Division by 0 is not permitted!\n");
        } else {
                printf("%i\n", num1 / num2);
        }
  }

  printf("Calculator finished!\n");

  return 0;
}
