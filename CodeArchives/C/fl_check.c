#include <stdio.h>
#include <conio.h>

int main(){
	int number[] = {4,2,1,8,5};
	int i, j, temp, length = 5;
	int 

	for(i=0;i<length-1;i++){
		for(j=0;j<length-1-i;j++){
			printf("Innner loop");
			if (number[j]>number[j+1]){
				temp = number[j];
				number[j] = number[j+1];
				number[j+1] = temp;
			}
		}
	}

	for(i=0;i<length;i++){
		printf("%d", number[i]);
	}
}