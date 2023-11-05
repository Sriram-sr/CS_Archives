#include <stdio.h>
#include <conio.h>

void main(){
    int i, numbers, flag, number;
    printf("Enter range of prime: ");
    scanf("%d", &numbers);
    for(number=0;number<numbers;number++){
        flag = 0;
	for(i=2;i<number;i++){
        if (number%i==0){
            flag = 1;
            break;
        }
    }
    if (flag==0){
        printf("%d\n", number);
    }
}
}
    
