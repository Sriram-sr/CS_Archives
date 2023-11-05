#include <stdio.h>


void main(){
    int *ptrVar;
    int var = 11;
    ptrVar = &var;

    printf("The address read from and the value is %d", *ptrVar);
}