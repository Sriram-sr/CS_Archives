#include<stdio.h>
#include<string.h>
int check_anagram(char a[], char b[]);
int main()
{
char a[1000], b[1000];
printf("Enter string");
gets(a);
gets(b);
if(check_anagram(a,b))
printf("String anagram");
else
printf("String not anagram");
}
int check_anagram(char a[], char b[])
{
int first[26], second[26], c=0;

while (a[c]!='\0')
{
printf("%d", first[a[c]]);
break;
// first[a[c]]-'a'++;
// c++;
// }
// c=0;
// while (b[c]!='\0')
// {
// second[b[c]-'a']++;
// c++;
// }
// for(c=0;c<26;c++)
// if(first[c] !=second[c])
// return 0;
// return 1;
}
}
