#include<stdio.h>

int main(){
	int *address;
	int int_value = 9;
	address = &int_value;
	// printf("Address at P is %d", address);
	// printf("\nValue at address is %d", *address);
	int array[] = {2,3,4};
	printf("Address is %d", array);
	printf("Address if one is %d", array+1); // four bytes gets added from previous value
}