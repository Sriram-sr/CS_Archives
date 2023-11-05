#include <stdio.h>
#include <conio.h>

void main(){
	int a = 2;
	int *p = &a;
	printf("Straight: %x", &a);
	printf("rev : %x",*p);
}