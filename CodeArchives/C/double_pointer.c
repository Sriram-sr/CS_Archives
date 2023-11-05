#include <stdio.h>
#include <conio.h>

void main(){
	int a, b, *p,*q, **i;
	a = 10;
	b = 20;
	p = &a;
	q = &b;
	i = &p;
	*q = 99;
	printf("Value of a: %d\n", a);
	printf("Value of a: %d\n", *p);
	printf("Address of a: %x\n", &a);
	printf("Address of a: %x\n", p);
	printf("Value of a: %d\n", **i);
	printf("Address of pointer: %x\n", &p);
	printf("Address of pointer: %x\n", i);
	printf("Value of b : %d", b);
}
	