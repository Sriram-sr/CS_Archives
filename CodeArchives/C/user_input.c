#include <stdio.h>

int main(){
	char userString[30];
	
	printf("Enter your string: \n");
	scanf("%s", userString);
	
	printf("The address in num %d\n", &userString);
	
	printf("original address is %p", &userString);
	
	
}
