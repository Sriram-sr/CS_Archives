#include <stdio.h>
#include <conio.h>

struct Student {
	int roll_no;
	char name[20];
	float mark;
};

void main(){
	struct Student s1 = {2, "Macha", 34.78};
	printf("%d", s1.roll_no);	
}
