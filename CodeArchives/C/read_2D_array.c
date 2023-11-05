#include <stdio.h>
#include <conio.h>

void main(){
	int count, idx;
	printf("Enter the number of values: ");
	scanf("%d", &count);
	int numbers[count];
	for(idx=0;idx<count;idx++){
		printf("Enter: ");
		scanf("%d", &numbers[idx]);
	}
	
	for(idx=0;idx<count;idx++){
		printf("%d\n", numbers[idx]);
	}
}
	