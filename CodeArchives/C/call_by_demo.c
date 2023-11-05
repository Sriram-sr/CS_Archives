#include <stdio.h>
#include <conio.h>

int value_method(int param1, int param2){
	param1 = 100;
	param2 = 200;
	printf("Value method changed are %d %d\n", param1, param2);
}

void reference_method(int *param1, int *param2){
	*param1 = 888;
	*param2 = 777;
	printf("Value method changed are %d %d\n", *param1, *param2);
}

void main(){
	int arg1 = 10;
	int arg2 = 20;
	
	value_method(arg1, arg2);
    printf("After calling value method %d %d\n", arg1, arg2);
	
	reference_method(&arg1, &arg2);
	printf("After calling reference method %d %d\n", arg1, arg2);
}

	
