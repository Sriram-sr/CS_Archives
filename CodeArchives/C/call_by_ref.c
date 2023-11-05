#include <stdio.h>
#include <conio.h>

void main(){
    void changeIt(int *);
    int num = 23;
    printf("Number before function %d", num);
    changeIt(&num);
    printf("\nNumber after function is %d", num);
}

void changeIt(int *num){
    *num = *num + 1;
    printf("\nNumber in function is %d", *num);
}
