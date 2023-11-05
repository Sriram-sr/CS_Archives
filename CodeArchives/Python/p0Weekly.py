import os

def merge_files_in_subfolders(main_folder, target_file):
    try:
        with open(target_file, 'w') as target:
            for root, dirs, files in os.walk(main_folder):
                for file_name in files:
                    if file_name.endswith('.py'):
                        with open(os.path.join(root, file_name), 'r') as source_file:
                            target.write(source_file.read() + '\n')
        print('Merging successful!')
    except IOError as e:
        print('An error occurred while merging files:', str(e))


if __name__ == '__main__':
    # Get the folder of the script being executed
    script_folder = os.path.dirname(os.path.abspath(__file__))
    main_folder = script_folder  # Use the script folder as the main folder
    target_file = 'p0Weekly.py'  # Replace with the desired merged file name

    merge_files_in_subfolders(main_folder, target_file)


S=input()
s=0
k=0
for i in range(len(S)):
    if S[i]=='A' or S[i]=='E' or S[i]=='I' or S[i]=='O' or S[i]=='U':
        k+=len(S)-i
    else:                                                            #Minion game
        s+=len(S)-i
if s==k:
    print("Draw")
elif k>s:
    print("Kevin "+ str(k))
else:
    print("Stuart "+ str(s))


##################################################################################
myDictionary={"two":"2", "one":"1", "five":"5", "1four":"4"}

newDictionary={}

sortedList=sorted(myDictionary.values())
print(sortedList)
for i in sortedList:
    for key, value in myDictionary.items():
        if value==i:
            newDictionary[key]=value
print(newDictionary)      

A=[2,5,6,7,8,0]
for i,j in enumerate(A):
    print(i,j)






















giv_str='aabbbccde'
new_list=[]
for i in range(len(giv_str)):
    if giv_str[i] in giv_str[i+1:]:
         if giv_str[i] not in new_list:
             new_list.append(giv_str[i])
count_list=[]             
for char in new_list:
    count_list.append(giv_str.count(char))
new_dict={}
'''for i in new_list:
    for j in count_list:
        new_dict[i]=j
        count_list.remove(j)
        break
    print(new_dict)'''
for i in range(len(new_list)):
    new_dict[new_list[i]]=count_list[i]
count_list.sort(reverse=True)

sorted_x = sorted(new_dict,key=new_dict.get,reverse=True)
for i in sorted_x:
    print(i,new_dict[i])


S=input()
s=0
k=0
for i in range(len(S)):
    if S[i]=='A' or S[i]=='E' or S[i]=='I' or S[i]=='O' or S[i]=='U':
        k+=len(S)-i
    else:                                                            #Minion game
        s+=len(S)-i
if s==k:
    print("Draw")
elif k>s:
    print("Kevin "+ str(k))
else:
    print("Stuart "+ str(s))



new_list=[1,2,3,4,5,6,7,8,9]
while len(new_list)>1:                        #TO right rotate and left rotate with jump2
    new_list=new_list[1:len(new_list):2]
    new_list=new_list[len(new_list)-2:0:-2]
print(new_list) 

#########################################################################

my_list=[1,4,6,8,4,5,3,0,1]
sub_list=[4,5]
for i in range(len(my_list)):
    for j in range(len(sub_list)):
        if sub_list[j]==my_list[i]:
            if j+1<len(sub_list) and i+1<len(my_list):
                if sub_list[j+1]==my_list[i+1]:
                    print(my_list[i:i+2])

list1=[2,3,7,5,4,9,2]
print(list1)
for i in range(0,len(list1),2):
    if i<len(list1)-1:
        list1[i],list1[i+1]=list1[i+1],list1[i]
print(list1)    

#To print B
for row in range(7):
    for col in range(5):
        if (col==0) or (col==4 and (row!=0 and row!=3 and row!=6)) or ((row==0 or row==3 or row==6) and (col>0 and col<4)):
            print("*",end="")
        else:
            print(" ",end="")
    print()        
print()
#To print K
i=0
j=4
for row in range(7):
    for col in range(5):
        if col==0 or (row==col+2 and col>1):
            print("*",end="")
        elif (row==i and col==j) and col>0:
            print("*",end="")
            i+=1
            j-=1
        else:
            print(end=" ")
    print()        
            

num=123
count=0
while num>0:
   if num%2==0:
       num=num//2
       count+=1
   elif num%2!=0:
         num-=1
         count+=1
print(count)    

giv_dict={}
j=int(input("How many names do you want to enter?: "))
k=int(input("How many marks do you want to enter?: "))
for i in range(j):
    name=input("Enter name: ")
    marks=[]
    for h in range(k):
        mark=input("Enter the marks")
        marks.append(mark)
    giv_dict[name]=marks
print(giv_dict)    
'''for i in range(j):
    giv_dict[input()]=[input(f) for f in range(k)]
print(giv_dict)'''    
names=str(input("Enter the name you want to know the average: "))
n=giv_dict[str(names)]
sum=0
for i in n:
    sum+=int(i)
avg=sum/len(n)
print(f"Average is {avg}")

'''a = "this is a string"
a = a.split(" ") # a is converted to a list of strings. 
print(a)'''

'''dic={}
n=int(input("enter something : "))
n2=[input(n) for n in range(3)]
dic[n]=n2
print(dic)'''


person1=10
box1=10
box_list=[0 for x in range(person1)]
print(box_list)

for person in range(1,11):
    for box in range(person,11,person):
          if box<box1:
             if box_list[box]==0:
                 box_list[box]=1
             else:
                 box_list[box]=0
    print(box_list)
           

giv_list=[1,3,5,6,8]
target=7
max_val=max(giv_list)
if target>max_val:
    giv_list.append(target)
for i in giv_list:
     if target==i:
        print(giv_list.index(target))
else:
     giv_list.append(target)
     giv_list.sort()
     print(giv_list.index(target))  
             

list=["Karthick","dinesh","ajay","madhan"]
i=0
while i<len(list):
   print(list[i])
   i+=1
A=(2,3,4,5,5,9)
generator=(x**2 for x in A)
print(next(A))

q=int(input("number of queries: "))
empty_list=[]
type_list=[]
res_list=[]
for num in range(q):
    n=int(input("Enter the number of times: "))
    empty_list.append(n)
    type=input("Enter the type: ")
    type_list.append(type)
for i in range(len(type_list)):
        n=empty_list[i] 
        if type_list[i]=="odd":
           for j in range(n*2):
               if j%2!=0:
                  res_list.append(j)
        elif type_list[i]=="even":
             for k in range(n*2):
                  if k%2==0:
                     res_list.append(k) 
for res in res_list:
   print(res)

giv_list=["flower","flow","flight","float"]
res_str=""
min=giv_list[0]
for small in  giv_list:
    if len(small)< len(min):
         min=small
giv_list.remove(min)
for i in range(len(min)):
      count=0
      for word in range(len(giv_list)):
                if min[i]==giv_list[word][i]:
                    count+=1
      if count==len(giv_list):
           res_str+=min[i]
print(res_str)


giv_str="ABCDCDCDCMKGHCDCIOK"
sub_str="CDC"
count=0
for i in range(len(giv_str)):
    if giv_str[i]==sub_str[0]:
        if giv_str[i:i+3]==sub_str :
                count+=1

print(count)


arr = [12, 11, 13, 5, 6]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
       if arr[i]>arr[j]:
          arr[i],arr[j]=arr[j],arr[i]
print(arr)


python_students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
new_list=[]
for i in range(len(python_students)):
    for j in range(len(python_students[0])):
         new_list.append(python_students[i][j])
num_list=[]
for num in new_list:
     if num is type(float):                                     #To find the 2nd lowest num in nested list
          num_list.append(num)
#num_list=[x for x in new_list if isinstance(x,float)]
for i in new_list:
     if isinstance(i,float):
        num_list.append(i)
     elif isinstance(i,int): 
        num_list.append(i)
min_val=min(num_list)
num_list.remove(min_val)
sec_low=min(num_list)
res_list=[]
for i in python_students:
    if sec_low in i:
        res_list.append(i)
print(res_list)

'''n=int(input("Enter the number: "))
sum=0'''
'''for char in str(n):
    sum+=int(char)**3
if sum==n:
    print("amstrong number")
else:
    print("Not amstrong number")'''
'''temp=n
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if sum==n:                          #alternate method
    print("Amstrong number")
else:
    print("Not a amstrong number")'''

for i in range(1,1000):
     temp=i
     sum=0
     while temp>0:
         digit=temp%10
         sum+=digit**3
         temp//=10
         if sum==i:
             print(i)


new_list=[10,20,30,40,50]
cum_list=[]
j=0
for i in range(len(new_list)):
    j+=new_list[i]
    cum_list.append(j)
print(cum_list)

sec_list=[12,67,98,34]
sum_list=[]
for num in sec_list:
    sum=0                                 #find sum of char in list`:
    for char in str(num):                     
        sum+=int(char)
    sum_list.append(sum)
print(sum_list)      

split_list=[1,2,3,4,5,6,7,8,9,10,11,12,13]           #To split list into intervals
length=len(split_list)
n=5
broken_list=[split_list[i:i+n] for i in range(0,length,5)]
print(broken_list)


for i in range(0,length,n):
    print(split_list[i:i+n])        #alternate for above


l1=[[4,3,5],[1,2,3],[3,7,4]]
l2=[[1,3],[9,3,5,7],[8]]

for i in range(len(l1)):
       l1[i].extend(l2[i])
print(l1)       

result=[[0 for x in range(3)]for y in range(3)]
for i in range(len(result)):
    for j in range(len(result[0])):
        print(result[i][j],end=" ")
    print()    

















n=int(input("Enter the number: "))
def factorial(n):
    k=1
    while n>0:
        k*=n
        n-=1
    print(k)
factorial(n)


   

num=int(input("Enter the number of terms you want: "))
count=0
n1=0
n2=1
while count<num:
    print(n1)
    nth=n1+n2
    n1,n2=n2,nth
    count+=1

num=int(input("Enter the number: "))
for i in range(2,num):
    if num%i==0:
        print("Not a prime number")
        break
else:
    print("prime number")

for i in range(1,20):
    for j in range(2,i):
         if i%j==0:
             break
    else:
        print(i)

        

n=10
for i in range(n+1):
    x=2**i
    print("Two raised to the power of ",i,"is",x)

num=9343836
rev_number=0
while num>0:
    digit=num%10
    rev_number=rev_number*10+digit
    num//=10
print(rev_number)

A_list=[2,5,6,7,9]
'''for i in range(len(A_list)):
    print(all(A_list[i] <=A_list[i+1]) or (A_list[i] >= A_list[i+1]))'''
'''counter=0    
for i in A_list:
    counter+=1
print(counter)    
A_list *=0                    #to clear the list
print(A_list)                   

B=list(range(1,9))
sum=0
inc=0
while inc<len(B):
    sum+=B[inc]                 #Finding sum of the list using while
    inc+=1
print(sum)    

def len_of_list(my_list,size):
    if size<0:
        return 0
    else:                                                      # using recursion to find the length of the string
        return my_list[size-1]+len_of_list(my_list,size-1)
my_list=[3,45,6,4,2,5]
print(len_of_list(my_list,len(my_list)))

new_list=[45,36,887,2,8,1]
def rev_list(new_list):
    return [value for value in reversed(new_list)]
print(rev_list(new_list))

col_list=list(range(0,-9,-1))
col_list.reverse()
print(col_list)

mul_list=[2,6,8]
value=1
k=0
while k<len(mul_list):               #To multiply using while
    value*=mul_list[k]
    k+=1
print(value)

import math
print(math.prod(mul_list))'''

new1_list=[1,2,-4,5,-7,9,-4,6,-20]
'''num=0
while num<len(new1_list):
    if num%2==0:
        print(new1_list[num])
    num+=1'''

pos_list=filter((lambda x: (x>=0)),new1_list)




















new1_list=[2,4,5,-4,-8,9,12]
pos_list=list(filter((lambda x: (x>=0)),new1_list))
print(pos_list)

new_list=[5,6,9,7,2,[],66,37,8,[],8,[],15]
res_list=[ele for ele in new_list if ele!=[]]   #removing empty lists
new_res=list(filter(None,new_list))
print(res_list,new_res)

dup_list=[2,7,4,2,6,9,4,20,20,4,1,6]
temp_list=[]
repeated=[]
for i in range(len(dup_list)):               
    if dup_list[i] not in dup_list[i+1:]:           #removing duplicates in list     
        temp_list.append(dup_list[i])
    elif dup_list[-1] not in dup_list[:-2]:
        temp_list.append(dup_list[-1])
print(temp_list) 

for i in range(len(dup_list)):
    for j in range(i+1,len(dup_list)):                                    #alternate method
        if dup_list[i]==dup_list[j] and dup_list[i] not in repeated:
            repeated.append(dup_list[i])
print(repeated)        

a=list(map(int,input().split()))
print(a)


new_list=list(range(1,11))
d=3 #rotation number
i=0
temp_list=[]
while i<d:
    temp_list.append(new_list[i])
    i+=1
i=0
while d<len(new_list):
    new_list[i]=new_list[d]
    d+=1
    i+=1
new_list[:]=new_list[:i]+temp_list
print("The list after rotation is ",new_list)


samp_str="ABCDEFGHIJKLIMNOQRSTUVWXYZ"
length=len(samp_str)
t=4
for i in range(0,length,t):
    print(samp_str[i:i+t])

giv_str="alyssa healy"
print(giv_str.capitalize())

A="MananVohra"
B="".join(A)
print(B)
W=""
for i in A:
    W=i+W
print(W)

giv_str=input("Enter the string: ")
l=int(len(giv_str))
if giv_str[:int(l/2)]==giv_str[int(l/2):]:
    print("The string is symmetrical")
else:
    print("Not symmetrical")

sub_str="ohra"
print(A.find(sub_str))          #will return -1 if not found
print(A.count(sub_str))
import re
if re.search(A,sub_str):
    print("yes")

my_str="Hello geek how is doing geek ,hello"
from collections import Counter
res=Counter(my_str.split())
print(dict(res))

def strcount(my_str):
    counter=0
    while my_str[counter:]:
        counter+=1
    return counter
my_str="Hihellowelcome"
print(strcount(my_str))
new_str="This is the pytho language"
temp_list=new_str.split()                   #To print even length words
for word in temp_list:
    if len(word)%2==0:
        print(word)

def checkstring(string):
    string=string.lower()
    vow_set={'a','e','i','o','u'}
    s=set({})
    for char in string:
        if char in vow_set:
            s.add(char)     #To check all vowels are in the string
    if len(s)==len(vow_set):
        print("Accepted")
    else:
        print("Not accepted")
string="ABeeIghiObhKUul"
checkstring(string)

vowel = [string.count('a'), string.count('e'), string.count('i'), string.count('o'), string.count('u')] 
                                                                                                           #Alternate method
if len(set(string.lower()).intersection("aeiou")) >=5:
    print("Accepted")


















given_list=[1,3,5,6,3,4,9]
happy_list={3,7,8,9}
sad_list={1,5,4,2,6}
happiness=0
for num in given_list:
    if num in happy_list:
        happiness+=1
    elif num in sad_list:
        happiness-=1
print(happiness)

str1="aAfhjdgsu2@kshi"
str2="khiwyuklm0"
com_str=""
for char in str1:       #To find common in string
    if char in str2:
        com_str+=char
print(len(com_str))

s="GeeksforGeeks"
t=""
s=set(s)
s="".join(s)
print("without order {}".format(s))
for i in s:
    if i in t:
        pass
    else:
        t+=i
print("with order {}".format(t))        

giv_str="Geeks for Geeks"
count=0
for i in range(len(giv_str)):                                                #to find the 1st nonRepeating char
    if giv_str[i] not in giv_str[:i] and giv_str[i]  not in giv_str[i+1:]:
        count+=1
        if count>1:
            break
        print(giv_str[i])

from collections import Counter
new_str="My favorite game"
res=Counter(new_str)                #Alternate method
res=min(res,key=res.get)
print(res)


























from collections import Counter
new_str="Geeks for Geeks"
res=Counter(new_str)
res=max(res,key=res.get)
print(res)

giv_str="Hello geeks for geeks hi"
k=(giv_str.split(" "))
temp_list=[]                         # To find largest length word
for word in k:
    if len(word)>=4:
        temp_list.append(word)
print(temp_list)        
 
F=new_str.split(" ")
print(("-".join(F)))
A="Geeks for Geeks"
B="Learning from Geeks for Geeks"       #uncommon word in two strings
A=A.split()
B=B.split()
values=[]
for i in B:
    if i not in A:
        values.append(i)
print(values)

G=set(A).symmetric_difference(set(B))          #Alternate method
print(G)








my_str="GeeksforGeeks"
d=2
temp_str=""
for i in range(d):
    temp_str+=my_str[i]                   #string rotation
cut_str=my_str.replace(my_str[:d],"",1)
res_str=cut_str+temp_str
print(res_str)

right_rot=my_str[len(my_str)-d:]+my_str[:len(my_str)-d]
left_rot=my_str[d:]+my_str[:d]                              #Alternate method
print(right_rot)
print(left_rot)

    
input="GEEGEEKSKS"
pattern="GEEKS"
index=input.find(pattern)                         #To check after removing substring gives the substring
k=input[:index]+input[len(input)-index+1:]
if k==pattern:
    print("True")

giv_str="Helloworrld"
dup_list=[]
for i in range(len(giv_str)):                                        #To print repeated char
    if giv_str[i]  in giv_str[:i] or giv_str[i] in giv_str[i+1:]:
        if giv_str[i] not in dup_list:
            dup_list.append(giv_str[i])
print(dup_list)            

inp_str="GeeksforGeeks"
rep_str="abcd"
rep=""
if rep_str in inp_str:
    rep+=rep_str
print(rep)    











nums = [3,2,4,7,8,3,5,6,1]
target = 8 
for i in range(len(nums)):               #To find indexes to be added to get target
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            print(i,j)



new_list=[12,45,87,33,32,90]
sum_list=[]
for i in new_list:
    sum=0
    for j in str(i):              #To get the sum of elements
        sum+=int(j)
    sum_list.append(sum)
print(sum_list)        


new_dict={"ok": [5, 6, 7, 8], "best": [6, 12, 10, 8], "s": [10, 11, 7, 5], "r": [1, 2, 5]}
emp_list=[]
cr_list=[]
res_list=[]
for i in new_dict.values():
    emp_list.append(i)
for value in emp_list:                          #To find the unique values
    for k in value:
        cr_list.append(k)
for i in range(len(cr_list)):
    if cr_list[i] not in cr_list[:i] and cr_list[i] not in cr_list[i+1:]:
        res_list.append(cr_list[i])
print("Only unrepeated values : ", res_list)
print("Only unique values : ",set(cr_list))

l1=list(sorted({ele for value in new_dict.values() for ele in value}))     #Alternate method using set comprehension
print(l1)


new_dic={'a': 100, 'b':200, 'c':300}
nl=[]
for i in new_dic.values():
    nl.append(i)
sum=0                                  #To find sum of keys
for i in nl:
    sum+=i
print(sum)    

test_dict = {"Arushi" : 22, "Anuradha" : 21, "Mani" : 21, "Haritha" : 21}
del test_dict["Mani"]
test_dict.pop("Haritha")
print(test_dict.pop("Mani","No"))
test_dict2 = {"Arushi" : 22, "Anuradha" : 21, "Mani" : 21, "Haritha" : 21}
res={key:val for key,val in test_dict2.items() if key!="Mani"}
print(res)


test_dict = {'month' : [1, 2, 3],
             'name' : ['Jan', 'Feb', 'March']}
print(dict(zip(test_dict["month"],test_dict["name"])))  

















samp_list=["aba","aba","xyz","123"]
count=0
for i in samp_list:                 #To get the count of words with same prefix and suffix
    if i[0]==i[-1]:
        count+=1
print(count)        

A=set()
sam_list=[20,40,30,20,80,10,60,40]
for i in sam_list:
    if i not in A:
        A.add(i)
print(A)

l=[]
if l:
    print("S")
else:
    print("K")


data = [("Apples", 5, "20"), ("Pears", 1, "5"), ("Oranges", 6, "10")]
data.sort(key=lambda x: x[0])
print(data)
                                                        #To sort using lambda function
sort_list_last=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sort_list_last.sort(key=lambda x:x[1])
print(sort_list_last)


for i in range(1,31):
    if i<6 or i>25:
        print(i**2)


nums = [5, 15, 35, 8, 98]
for index,value in enumerate(nums):
    print(index,value)
print(list(enumerate(nums,2)))

v1=input()
v1.split(",")
print(v1)









num_list=[20,7,8,2,5]
min=num_list[0]-num_list[1]
new={}
for i in range(len(num_list)):
    for j in range(i+1,len(num_list)):                                      #min difference 
        if ((num_list[i]-num_list[j])<min and (num_list[i]>num_list[j])):
              min=abs(num_list[i]-num_list[j])
              new[min]=i,j
print(new[min])
print(min)


AK=[2,4,3]
BK=[5,6,4]
AK.reverse()
BK.reverse()
str1=""
str2=""
for i in AK:
    str1+=str(i)
for j in BK:
    str2+=str(j)
res=int(str1)+int(str2)
res_list=[]
for i in str(res):
    res_list.append(i)
print(res_list)    

num=17
giv=int(input())
temp=giv-num
if giv>num:
    print(abs(temp))
else:
    print(abs(temp))

histogram=[2, 3, 6, 5]
for n in histogram:
    res=""
    times=n
    while times>0:
       res+="*"
       times-=1
    print(res)   
    
numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]
for num in numbers:
    if num==237:
        print(num)
        break
    elif num%2==0:
        print(num)

giv_str="3322251"
count=1
for i in range(1,len(giv_str)):
    if giv_str[i-1]==giv_str[i]:
        count+=1
        if i+1==len(giv_str):
            print(giv_str[i],count)
    else:
        print(giv_str[i-1],count)
        count=1


roman=str(input("Enter the roman number: "))
roman=roman.upper()
total=0
pre=0
rom_dict={
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000 
       }

for i in range(len(roman)-1,-1,-1):
    if rom_dict[roman[i]]>=pre:
        total+=rom_dict[roman[i]]
    else:
       total-=rom_dict[roman[i]]
    pre=pre+rom_dict[roman[i]]
print(total)    

giv_list=[1,5,4]
giv_list.sort()
count=0
for i in range(len(giv_list)):           #To find the sum of abs difference
    for j in range(i+1,len(giv_list)):
        if j < len(giv_list):
            count+=abs(giv_list[i]-giv_list[j])
print(count)            

lis_1=[2,1,5,1]
for i in range(len(lis_1)):
    if lis_1[i] in lis_1[:i] or lis_1[i] in lis_1[i+1:]:
        sum=0                                             #To return 0 if list contain dup value else return sum
        print(sum)
        break
else:
    print(sum(lis_1))


A=[2,4,5,67,8]
print(all(x>1 for x in A))

str = 'a123'
try:
    i = float(str)
except (ValueError, TypeError):
    print('\nNot numeric')
print()

num_list = [45, 55, 60, 37, 100, 105, 220]
x=list(filter((lambda k:k%15==0),num_list))            
print(x)

try:
    k= int(input("Enter the number: "))
    
except ValueError:
    print("\n This is not a valid number")
finally:
    print("OK")
    

nums = [34, 1, 0, -23, 12, -88]
v=list(filter((lambda x: x>0),nums))
print(v)

try:
  x = 1
except NameError:
  print("Variable is not defined....!")
else:
  print("Variable is defined.")
try:
  y
except NameError:
  print("Variable is not defined....!")
else:
  print("Variable is defined.")
  
str1 = 'A8238i823acdeOUEI'
count=0
for i in str1:
    if i.islower():
        count+=1
print(count)

sum=0
n=8
while n>1:
    n-=1
    sum+=n**3
print(sum)    

lis1=[1,3,5,7,9]
k=0
for i in range(len(lis1)-1):
        if (lis1[i]*lis1[i+1])%2!=0:
            k+=1
print(k)

















n1=int(input("Enter the first number : "))
n2=int(input("Enter the second number : "))
if n1%n2==0:
    print("GCD="+str(n2))                 #To find the GCD
else:
    for i in range(int(n2/2),0,-1):
        if n2%i==0 and n1%i==0:
            print("GCD="+str(i))
            break

if n1>n2:
    k=n1
elif n2>n1:
    k=n2
                                         #To find the LCM
while True:
    if k%n1==0 and k%n2==0:
        LCM=k
        break
    k+=1
print("LCM="+str(LCM))    

giv_str="MYstring123"
x=sorted(giv_str)
print(x)
n1,n2,n3=[],[],[]
for i in x:
    if i.islower():          #To sort in given order
        n1.append(i)
    elif i.isupper():
        n2.append(i)
    else:
        n3.append(i)
print(n1+n2+n3)        

giv_str="AAABCADDE"
k=3
new_list=[]
for i in range(0,len(giv_str),k):
   new_list.append((giv_str[i:i+k]))
print(new_list)   
res_str=""                            #To split into intervals and return single char
for word in new_list:
    new_str=""
    for let in word:
        if let not in new_str:
            new_str+=let
    res_str+=new_str
print(res_str)    

x = [1, -6, 4, 2, -1, 2, 0, -2, 0 ]
for i in range(len(x)):
    if i<len(x)-1:
        if sum(x[i:i+3])==0:
            print(x[i:i+3])


giv_str=248163264128
n=2
l=2
i=1
ans=True
while ans:
    if str(l) in str(giv_str):
        i+=1
        l=pow(n,i)
    else:
        ans=False
res=i-1
print(res)
     

pattern="abba"
pat="abcd"
s="dog cat cat dog"
new_s=s.split()
new_dic={}
for i in range(len(new_s)):
    for j in pattern:
        if new_s[i]
        new_dic[new_s[i]]=pat[j]


new_dict={"Name":"sriram",
        "Age":21,
        "blood":"B"}
print(new_dict) 
print(new_dict["Age"])
new_dict["colege"]="MIT"
print(new_dict)
print(dict.fromkeys(new_dict,"Bye"))
print(new_dict.get("Name"))

print(new_dict)
print(new_dict.setdefault("name2","loki"))
new_dict["Myhome"]={1:{"sri","ram"},"vi":{4,7,9}}
print(new_dict)
print(new_dict["Myhome"][1])
new_arr=[1,23,5,5,3,7]
from collections import OrderedDict
A=OrderedDict.fromkeys(new_arr)
for key in A.keys():
    print(key,end=" ")

s = "luffy is still joyboy"
b=s.split(" ")
max=len(b[0])
for i in b:                   #To find the largest word's length
    if len(i)>max:
        max=i
print(len(max))   

digits = [4,3,2,1,9]
last=digits[len(digits)-1]
last=last+1                   #To increment the last value by 1
for i in str(last):
    digits.append(int(i))
print(digits)    

a=12
print(bin(a).replace("0b",""))       #To find binary from decimal

a="11"
b="1"
sum=bin(int(a,2)+int(b,2))
print(sum[2:])

import math
print(math.sqrt(4))

giv_list=[1,2,3,4,5,6,8,9]
target =6
for i in range(len(giv_list)):
    if giv_list[i]==target:
        print(i)                   #To find the target number's index or to find where it is inserted

else:
    for i in range(len(giv_list)):
        if (giv_list[i] < target) and  (giv_list[i+1] > target):
            print(i+1)



test_tuple = ((4, 'Gfg', 10), (3, 'is', 8), (6, 'Best', 10))
res=[{'key':val[0] ,'value':val[1],'id':val[2]} for val in test_tuple]
print(res)
              ###################################################
new_list=[]
test_dict = {'gfg' : [5, 6, 7, 8],
             'is' : [10, 11, 7, 5],
             'best' : [6, 12, 10, 8],
             'for' : [1, 2, 5]}
for i in test_dict.values():
    new_list.append(i)
print(new_list)
temp_list=[]
for i in new_list:
    for j in i:
        temp_list.append(j)      #To get unique values from dictionary
print(temp_list) 
res_list=[]
for i in temp_list:
    if i not in res_list:
        res_list.append(i)
print(sorted(res_list)) 

##########################################################################
lis = [{ "name" : "Nandini", "age" : 20},
{ "name" : "Manjeet", "age" : 20 },
{ "name" : "Nikhil" , "age" : 19 }]
print(sorted(lis,key=lambda x:x["age"]))
print(sorted(lis,key=lambda x:(x["name"],x["age"])))
print(sorted(lis,key=lambda x: x["name"],reverse=True))

b="The wait is over"
print(b.split())
A=["the", "wait","is","over"]
print(" ".join(A))




























candy_list=[1,1,2,5,2,5]
length=len(candy_list)//2
types=len(set(candy_list))
if types<=length:
    print(f" She can eat {types} candies")
    
a = {2, 4, 5, 9}
b = {2, 4, 11, 12} 
print(a.union(b))

for i in range(1,6):
   for j in range(i):
       print("$",end="")
   print()
print()
for i in range(5,0,-1):
    for j in range(i):
       print("$",end="")
    print()
print()
for i in range(1,6):
     for j in range(i):
         print(i,end="")
     print()
print()
for i in range(5,0,-1):
     for j in range(i):
        print(i,end="")
     print()

print()

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()
print()
for i in range(5,0,-1):
    for j in range(1,i+1):
       print(j,end="")
    print()
print()
for i in range(1,6):
     for j in range(i,0,-1):
         print(j,end="")
     print()
print()
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end="")
    print()
print()
n=1
col=1
for i in range(4):
    for j in range(1,col+1):
        print(n,end="")
        n+=1
    col+=2
    print()
print()

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    for k in range(i-1,0,-1):
        print(k,end="")
    print()

print()
 
for i in range(1,6):
    for j in range(5,i,-1):
       print(" ",end="")
    for k in range(i):
       print("*",end="")
    print()
print()
for i in range(5,0,-1):
   for j in range(5,i,-1):
      print(" ",end="")
   for k in range(i):
      print("*",end="")
   print()

print()

for i in range(1,6):
    for j in range(5,i,-1):
        print(" ",end="")
    for k in range(1,i+1):
        print(k,end="")
    print()
print()

for i in range(5,0,-1):
    for j in range(5,i,-1):
       print(" ",end="")
    for k in range(1,i+1):
       print(k,end="")
    print()
print()
 
for i in range(1,6):
    for j in range(5,i,-1):
       print(" ",end="")
    for k in range(1,i+1):
       print(i,end="")
    print()
print()

for i in range(5,0,-1):
    for j in range(5,i,-1):
       print(" ",end="")
    for k in range(i):
       print(i,end="")
    print()

print()
 
string="PYTHON"
for i in range(6):
    for j in range(i+1):
        print(string[j],end="")
    print()
     
var="12345"
for i in range(len(var)):
    for j in range(len(var)):
       if i==j or (i+j==4):
          print(var[j],end=" ")
       else:
          print(" ",end="")
    print()
    
for row in range(7):
    for col in range(5):
        if (col==0 and row!=0 and row!=6) or (col==4 and row!=0 and row!=6) or (row==0 and col!=0 and col!=4) or (row==6 and col!=0 and col!=4):
            print("*",end="")
        else:
            print(" ",end="")
    print()

for i in range(1,10):
    for j in range(1,i+1):
       print(i,end="")
    print()







           



test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]
new_list=[]
for i in range(len(test_list)):
    if i<len(test_list)-1:
        if test_list[i][0]==test_list[i+1][0] or test_list[i][0]==test_list[i-1][0]:
            new_list.append(test_list[i])
print(new_list)
res_list=[]                                 #join tuple with similar initial element
res_list.append(new_list[0][0])
for i in range(len(new_list)):
    res_list.append(new_list[i][1])
print(res_list)
final_list=[]
res_list=tuple(res_list)
print(res_list)
final_list.append(res_list)
for i in test_list:
    if i not in new_list:
        final_list.append(i)
print(final_list)


test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
k=2
result=[ i for i in test_list if len(i)!=2]
print(result)
altr=list(filter((lambda x:len(x)!=k),test_list))   
print(altr)





















test_tup=[('452', 10), ('256', 5), ('100', 20), ('135', 15)]
new_list=[]
for i in test_tup:
    new_list.append(list(i))
for i in range(len(new_list)):       #To sort using 2nd value of a tuple
    if i<len(new_list)-1:
        if new_list[i][1]>new_list[i+1][1]:
            new_list[i],new_list[i+1]=new_list[i+1],new_list[i]
print(new_list)          

test_tup.sort(key=lambda x:x[1])  #Alternate
print(test_tup)
print(sorted(test_tup,key=lambda x: x[1]))

