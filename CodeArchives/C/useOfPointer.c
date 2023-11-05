#include <stdio.h>

void sum(int*, int*, int*);

void main(){
    int num1 = 3, num2 = 8, total;
    sum(&num1, &num2, &total);
    printf("Total is %d", total);
}

void sum(int *n1,int *n2,int *t){
    *t = *n1 + *n2;
}