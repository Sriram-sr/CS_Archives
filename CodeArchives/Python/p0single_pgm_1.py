class Library:
     def __init__(self,books):
        self.books=books

     def list_books(self):
        for book in self.books:
            print(books)
     
     def Borrow_book(self,borrow_book):
        if  borrow_book in self.books:
            print("Get your book")
            self.books.remove(borrow_book)
        else:
            print("book not available")
     
     def receive_book(self,receive_book):
        print("You have received the book")
        self.books.append(receive_book)
         
books=["c","java","python"]
Obj=Library(books)
  
msg="""
    1.Display book
    2.Borrow book
    3.Return book
"""

while True:
    print(msg)
    ch=int(input("Enter your choice: "))
    if ch == 1:
       Obj.list_books()
    elif ch == 2:
       book=input("Enter the name of the book: ")
       Obj.Borrow_book(book)
    elif ch == 3:
       book =input("Enter book to return")
       Obj.receive_book(book)
    else:
       print("Thank you come again")

def group_data(grpval,n):
     for value in grpval:
         if n == value:
             print(value)

# print(group_data([1,8,91,-5,6],9))
# print(group_data([12,71,-40,6,3],6))

# ---- # Game.py

guessing_number=18
countoften=1

while countoften <= 10:
   print("Guess the number")
   userinput=int(input())
   if userinput > 18:
      print("You are going too high")
   elif userinput < 18:
      print("You are going too low")
   elif userinput == 18:
      print("You have won")
      print("you have won with",10-countoften,"lifes left") 
      break
   print(10-countoften,"lifes left")
   countoften=countoften+1
if countoften > 10:
  print("Game over!")


# -------- # hack.py

n=int(input("Enter a number: "))
if n %2 != 0:
   print("wierd")
elif n%2 == 0 and (n > 2 and n< 5):
   print("Not wierd")
elif n%2 == 0 and (n > 6 and n < 20):
   print("wierd")
elif n%2 == 0 and n > 20:
    print("Not wierd") 
else:
    print("wierd")    

# ------- # inherit.py

class A:
   def fun(self):
      self.var=12
      self.varsh=19
class B(A):
   def __init__(self):
       self.var=54
       self.varsh=63

o=A()
o1=B()
print(o1.var)


# ------ # istype.py

def istype(lis):
     if isinstance(x,list) == True:
          print("This is a list")
     if isinstance(x,tuple) == True:
          print("This is a tuple")
     if isinstance(x,set) == True:
          print("This is a set")
            

x=("sai","sri","sarath")


# ------- # Johnis.py

'''row=3
col=7
list1=[[" " for x in range(col)] for y in range(row)]
string="JOHNISRUNNING"
index=0
col1=0
col2=row-1
column=0
for i in range(col):
    if i%(row-1)==0:
          for j in range(row):
              if index<len(string):
                  list1[j][column]=string[index]
                  index+=1
          column+=1
    else:
       if i==column:
           k=row-1
           for j in range(col1,col2):
              if index<len(string) and (k>0 and k<(row-1)):
                list1[k][column]=string[index]
                index+=1
                column+=1
              k-=1
           col1+=row-1
           col2+=row-1
for z in list1:
   print(z)'''

###################################################################################
       

# -------- #

list_a=[12,45,90,78,30,89,75,60,55,98]

'''value=list(filter(lambda x:  (x%15 == 0),list_a))
print(value)

list_var=[21,7,6,4,0,3,-7,-95,-5]
M=list(filter(lambda x: x > 0,list_var))
print(M)

print("____________________--")

check_lis=[12,-3,6,-67,45,-2]
for x in check_lis:
   if x > 0:
     print(x," ")'''

check_var=[12,-3,-6,9,5,-40,-1,-3]
valve=(n for n in check_var if n >0)
print("\n",*valve)

'''new_list=[]
for i in list_a:
    if i%15==0:
       new_list.append(i)
print(new_list)'''

# ------- #

for row  in range(7):
    for col in  range(5):
       if ((col==0 or col==4) and row!=0) or ((row==0 or row==3) and (col>0 and col<4)):
           print("*",end="")
       else:
          print(end=" ")
    print()

print()

for row in range(7):
   for col in range(5):
      if ((row==0 or row==3 or row==6) and (col>0 and  col<4)) or (col==0 and row>0 and row<4) or (col==4 and row>3 and row<6):
           print("*",end="")
      else:
          print(end=" ")
   print() 
 
print()
  
for row in range(7):
    for col in range(5):
       if (row==0 or row==6 and col!=2) or (col==2):
          print("*",end="")
       else:
          print(end=" ")
    print()

print()

for row in range(7):
    for col in range(5):
       if col==0 or (row==0  or row==3 and (col>0 and col<4)) or  (col==4 and (row!=0 and row!=3)):
           print("*",end="")
       else:
           print(end=" ")
    print()

print()

for row in range(7):
   for col in range(7):
      if (col==0 or col==6) or ((row==col) and (col>0 and col<4)) or (row==1 and col==5) or (row==2 and col==4):
          print("*",end="")
      else:
         print(end=" ")
   print()
print()
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
         
print()
for row in range(6):
    for col in range(7):
       if (row ==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8):
           print("*",end="")
       else:
          print(end=" ")
    print()     

# ----- #

string="Mybarbadoscric"
print("%s"%string)
print("%.2s"%string)
print("%.5s"%string)
print(string[:6])


# ----- # 

A=[]
n=int(input("Enter the number of values:"))

for i in range(0,n):
    A.append(input("Enter the item:  "))

print("The values are")

for i in A:
   print(i,end=" ")


list1=[1,2,66,34,2,35,99,34,54,6,21,99,33]
list2=[]

for i in list1:
   if i not in list2:
      list2.append(i)

print("\n",list2)

AK=["des","chas","THer"]
a="-".join(AK)
print(a)

print("____________________________________________")
A=[7,5,4,1,9]
print(all(i<2 for i in A))
print(all(i > 5 for i in A))

# ---- #

para=["25","35","45"]
print(".".join(para))

print("__________________")

a=["sri","Hi","boy"]
print(len(a))
print(max(a))
print(min(a))
print(list(range(5)))
print(list("sriram"))
kishan=["vijay","surya","Raina"]
print("hi:%s,hello:%s,bro:%s"%(kishan[0],kishan[1],kishan[2]))


# ----- #

I=[]  
n = int(input("Enter the number of elements in the list:"))  
for i in range(0,n):     
    I.append(input("Enter the item:"))     
print("printing the list items..")   
for i in I:   
    print(i, end = "  ")     

# ----- #

def concatenate_list(list):
      result=""
      for value in list:
          result+=str(value)
      return result

print(concatenate_list([1,41,61,2,9]))  

# ---- #

import numpy 
'''X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]
res=[[0,0,0],
     [0,0,0],
     [0,0,0]]

res=numpy.dot(X,Y)
print(res)

test_list = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]
new_l=[j for i in test_list for j in i]
print(new_l)

A =[[1, 2], [3, 4]]
  

B = [[4, 5], [6, 7]]
resu=numpy.add(A,B)
print(resu)'''
 
m= [[1,2],[3,4],[5,6]] 
print(numpy.transpose(m))

txt="Geeksforgeeks"
t=""
for i in txt:
   if i in t:
      pass 
   else:
      t+=i
print(t) 

A=[6,5,3,2,1]

for i in range(len(A)-1):
    if A[i]>=A[i+1]:
       print("Monotonically decreasing")
    elif A[i]<=A[i+1]:
       print("Monotonically increasing")

orig_arr=[1, 2, 3, 4, 5, 6, 7]
rotat_arr=[]
temp=[]
for i in range(2):
    temp.append(orig_arr[i])
for k in range(len(orig_arr)):
    rotat_arr.append(orig_arr[k])
result=rotat_arr[2:]+temp
print(orig_arr)
print(result)

#alternate way of rotration

arr = [12, 10, 5, 6, 52, 36]
pos=2
n=len(arr)

for i in range(0,2):
    x=arr[0]
    for j in range(0,n-1):
       arr[j]=arr[j+1]
    arr[n-1]=x
print(arr)
   

# --- #

'''m1=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for i in range(4):
   for j in range(4):
       if i+j==3:
          m1[i][j]=i+1
for i in m1:
   print(i)
m3=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for i in range(4):
    for j in range(4):
       if i+j==3:
          m3[i][j]=j+1
print()
for i in m3:
   print(i)
m2=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for i in range(4):
    for j in range(4):
        if i==j:
           m2[i][j]=j+1
print()
for i in m2:
   print(i)
print()

m4=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] 
a=1
for i in range(3,-1,-1):
    for j in range(3,-1,-1):
       if i==j:
         m4[i][j]=a
    a+=1  
print()
for k in m4:
    print(k)
print()'''       
###################################################################              #To print 1234 in row col order
'''row=4
col=4
temp=1
new_list=[[0 for i in range(col)]for j in range(row)]
print(new_list)

for i in range(row):
    for j in range(col):
       new_list[i][j]=temp
       temp+=1
for m in new_list:
    print(m)'''
###########################################################################
'''mid=1
row=4
col=4
new_list1=[[0 for i in range(col)] for j in range(row)]
for i in range(col):
   if i%2==0:
       for j in range(row):
           new_list1[j][i]=mid
           mid+=1
   else:
       for j in range(row-1,-1,-1):
            new_list1[j][i]=mid
            mid+=1
for i in new_list1:
    print(i)'''
###########################################################################
'''row=4
col=4
temp=1
new_list=[[0 for i in range(col)]for j in range(row)]
print(new_list)

for i in range(col):
    for j in range(row):
       new_list[j][i]=temp
       temp+=1
for m in new_list:
    print(m)'''
#############################################################################
'''val=1
row=4
col=4    	
snake_list=[[0 for i in range(col)] for j in range(row)]

for i in range(row):
     if i%2==0:
         for j in range(col):
             snake_list[i][j]=val
             val+=1
     else:
         for j in range(col-1,-1,-1):
             snake_list[i][j]=val
             val+=1
for h in snake_list:
     print(h)'''
####################################################################
row=4
col=4
val=1
spiral_list=[[0 for i in range(col)] for j in range(row)]

for i in range(row):
        if i==0:
           for j in range(col):
              spiral_list[i][j]=val
              val+=1
for i in range(col):
    if i==3:
         for j in range(1,4):
             spiral_list[j][i]=val
             val+=1

for i in range(row):
     if i==3:
         for j in range(col-2,-1,-1):
             spiral_list[i][j]=val
             val+=1
for i in range(row):
         if i==2:
             for j in range(0,col-3):
                 spiral_list[i][j]=val
                 val+=1  
for i in range(row):
      if i==2: 
         for j in range(1,3):
            spiral_list[i][j]=val
            val+=1
for i in range(row):
      if i==1:
         for j in range(2,-1,-1):
            spiral_list[i][j]=val
            val+=1
for i in spiral_list:
     print(i)         

# ---- # 

def swapfun(list):
    size=len(list)
    list[0],list[size-1]=list[size-1],list[0]
    print(list)
swapfun([2,4,5,6,9])

my_list=[2,5,6,8,3]
a,b,*c=my_list
print(a)
print(b)
print(c)

A=[4,5,8,2,1,9,6,5]
print(sorted(A))

# Python program to print Positive Numbers in a List

# list of numbers
list1 = [-10, -21, -4, 45, -66, 93]

# using list comprehension
pos_nos = [num for num in list1 if num >= 0]

print("Positive numbers in the list: ", pos_nos)

L1=[2,4,7,5,3,3]
L2=L1[:]
print(L2)
	
list1 = [10, 20, 30, 20, 20, 30, 40,
         50, -20, 60, 60, -20, -20]
nl=[]
for i in range(len(list1)):
   for j in range(len(list1)):
       if list1[i]==list1[j] and list1[i] not in nl:
          nl.append(list1[i])
print(nl)

#cumulative addition
list=[10,19,60,35,33,2,7]
cum_list=[sum(list[:x:1]) for x in range(1,len(list))]
print(cum_list)

#cum method 2

ls=[18,33,78,45,3,99]
cum_sum=0
nl=[]
for i in range(0,len(ls)):
     cum_sum+=ls[i]
     nl.append(cum_sum)
print(nl)

sml=[]
for ele in ls:
   sum=0
   for k in str(ele):
       sum+=int(k)
   sml.append(sum)
print(sml)

A="Geeks for geeks code practice"
print(A.split())
B="".join(A)
print(B)
Rev_str=""
for i in range(len(A)):
     if i!=2:
        Rev_str+=A[i]
print(Rev_str)
        
print(A.replace("e","",3))   #3 is the occurances

nl_lis=["Geeks","for","Geeks"]
print(" ".join(nl_lis))
print("Geeks for Geeks".count("for"))

# ---- #

                                       #factorial
'''def fact(n):
    if n==1 or n==0:
        return 1
    else:
       return n*fact(n-1)
print("The facotial  is :", fact(8))'''

'''                            #find largest number of list
A=[2,4,8,95,3]
print(sum(A))

lis_1=[12,56,46,90,-3,6]
n=len(lis_1)
max=lis_1[0]
for i in range(1,n):
    if lis_1[i] > max:
        max=lis_1[i]
print(max)'''

                        #Rotation of array
arr=[1,2,3,4,5,6,7,8]
n=len(arr)
d=3
temp=[]
i=0
while i < d:
    temp.append(arr[i])
    i+=1
i=0
while d < n:
    arr[i]=arr[d]
    i+=1
    d+=1

arr[:]=arr[:i]+temp
print(arr)

#alternte method
arr[:]=arr[d:n]+arr[:d]
print(arr)
                                 #swapping 1st and last element    

newlist=[1,2,3,4,5,56,8]
n=len(newlist)
newlist[0],newlist[n-1]=newlist[n-1],newlist[0]
print(newlist)
   
# ----- #

import random
tar_num,user_num=random.randint(1,10),0
while tar_num != user_num:
      user_num=int(input("Enter a number until you get it right: "))
print("Well guessed")

# ----- #

'''list_1=[1,8,67,55,8,34]
total=0
for i in range(0,len(list_1)):
    total+=list_1[i]
print(total)

list_1.reverse()
print(list_1)'''

'''import random
char_list = ['a','e','i','o','u']
random.shuffle(char_list)
print(' '.join(char_list))

                          #missing phone number
def missing(n):
   compare_set=set([1,2,3,4,5,6,7,8,9,0])
   n=set([i for i in n])
   ans=n.symmetric_difference(compare_set)
   print(ans)

missing([8,4,2,8,2,5,9,3,9,4])

name="COMPUTER"
index=0
for i in name:
    print(name[:(index+1)])
    index+=1'''
                          #  * pattern
'''n=5
for i in range(n):
    for j in range(i):
        print('*',end="")
print('')


for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')
	
                        #removing vowels in string
giv_str="Hello to this wondrfulplace thanks for joining"
new_str=""
for i in giv_str:
     if i in "AaEeIiOoUu":
          pass
     else:
        new_str+=i
print(new_str)'''

sub=["tamil","english","maths","science","social"]
marks=[]
for i in range(6):
    m=int(input("Enter marks: "))
    marks.append(m)
for j in range(len(marks)):
    print("{}.{} mark={}".format(j+1,sub[j],marks[j]))


# ------ #

                       #leap year
'''def leapyear(year):
     if ((year%400==0) or (year%100!=0) and (year%4==0)):
         print("leap")
     else:
         print("Not leap")
leapyear(1998)'''

                     #prime numbers
'''lower = int(input("Enter lower range: "))  
upper = int(input("Enter upper range: "))  
  
for num in range(lower,upper + 1):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           print(num)  '''


                   #Fibonacci
  
'''n1=0
n2=1
count=0
num=int(input("Enter the number of times: "))
 
if num == 1:
    print(n1)
else:
   while count<num:
         print(n1)
         nth=n1+n2
         n1,n2=n2,nth
         count+=1
print(n1)
         
n=5
for i in range(n,0,-1):
    for j in range(i):
        print("*",end="")
i=1
str='*'
while i<=5:
   print(str*i)
   i+=1'''

# --------- #

'''def len_string(str):
    count=0
    for char in str:
        count+=1
    return count
print(len_string("Hi hello and welcome"))'''
    
                #prime number
'''start=1
end=20
for i in range(start,end):
     if i > 1: 
        for j in range(2,i):
            if (i%j==0):
                break
        else:
           print(i)''' 

'''import re
txt="Hi hello welcome to the world of engineers"
print(re.search("^Hi.* engineers$",txt))
print(re.findall("^Hi",txt))


L1=[5,7,3,2,5,3,7,6,4,8]
print(list(dict.fromkeys(L1)))

txt="Helloworld!"
print(txt[::-1])'''

new=[]
for i in range(1500,2700):
   if (i%7==0) and (i%5==0):
        new.append(i)
print(new)
 
a=input("ENTER:")
print(a[-1])


kilometer=float(input("Enter the kilometer:"))
conv_fact=0.621371
miles=kilometer*conv_fact
print("the conversion of %.2f kilometerets is %.2f"%(kilometer,miles))


# ---------- #

for i in range(6):
    for j in range(i+1):
         print("*",end="")
    print()  

for i in range(6,0,-1):
    for j in range(i):
       print("*",end="")
    print()

'''for i in range(6):
    for j in range(i):
        print(i,end="")
    print()
for i in range(6,0,-1):
    for j in range(i):
        print(i,end="")
    print()

for i in range(1,6):
     for j in range(1,i+1):
         print(j,end="")
     print() 
for i in range(6,1,-1):
     for j in range(1,i+1):
        print(j,end="")
     print()'''


'''for i in range(1,6):
    for j in range(i):
        print('*',end="")
    print()'''
for i in range(5):
    for j in range(i,5):
        print(" ",end="")
    for k in range(i+1):
        print("*",end="")
    print()


# ---- #

'''ln=input("Enter a letter: ")
if  ln in ('a','e','i','o','u'):
     print("%s is a vowel" %ln)
elif ln == 'y':
     print("y is a niether a vowel nor consonant")
else:
     print("%s is a consonant" %ln)'''

'''ls_of_months={'january','february','march','april','may','june','july','august','september','october','november','december'}
print("select from the below: \n",ls_of_months)
month=input("Enter the month: ")

if month == 'february':
     print("There are 28/29 days in ",month)
if month in ('january','march','may','july','august','october','december'):
     print("There are 31 days in ",month)
if month in ('april','june','september','november'):
     print("There are 30 days in ",month)'''

'''num1=int(input("Enter 1st number"))
num2=int(input("Enter 2nd number"))
def addnum(num1,num2):
     plus=num1+num2
     if plus in range(15,20):
         
         return 20
     else:
         return plus
print(addnum(num1,num2))'''

print("Input some integers to calculate their sum and average. Input 0 to exit.")

count = 0
sum = 0.0
number = 1

while number != 0:
	number = int(input())
	sum = sum + number
	count += 1

if count == 0:
	print("Input some numbers")
else:
	print("Average and Sum of the above numbers are: ", sum / (count-1), sum)
	
# ----- #
      #Dictionary comprehension
'''my_str="Good morning to the good persons out there and the good"
mydict={key : my_str.count(key) for key in my_str.split()}
print(mydict)

A="My new string is this"
vowel="Aeiou"
S=set({})
for i in A:
   if i not in vowel:
        S.add(i)
print(S)'''

import numpy as np
X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
 
Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]
res=[[0,0,0],
     [0,0,0],
     [0,0,0]]
'''for i in range(len(X)):
    for j in range(len(X[0])):
         res[i][j]=X[i][j]+Y[i][j]
print(res)'''

res=np.dot(X,Y)
print(res)

# ------- #

'''#from array import *
new_arr=[1,2,3,4,5]
new_arr.reverse()
print(new_arr)
print(new_arr.count(3))

a=2
b=4
print(a if a>b else b)

def facto(n):
    fact=1
    if n<1:
      return 1
    else:
       while n > 1:
          fact*=n
          n-=1
       return fact
print(facto(5))
sum=0
n=int(input(""))
check=str(n)
for i in check:
    sum+=int(i)**3
print(sum)
if sum==n:
   print("Yes amstrong number")
else:
   print("No")'''

'''for i in range(1,10):           #prime number
    for j in range(2,i):
         if i%j==0:
            break
    else:
        print(i)
                            #To check prime number
n=int(input(""))
for i in range(2,int(n/2)+1):
     if n%i==0:
       print("Not a prime number")
       break
     else:
       print("prime number")'''

'''val="a"            #To find the ascii value of a number
print(ord(val))'''

giv_array=[25,7,3,5,99,3,56,44,2]
'''temp_arr=[]
res_arr=[]
i=0
r=3
while i < 3:
      temp_arr.append(giv_array[i])   
      i+=1
while r< len(giv_array):
     giv_array[i]=giv_array[r]
     i+=1
     r+=1
res_arr[:]=giv_array[3:]+temp_arr[:]
print(res_arr)'''

################MAx of given array
max=giv_array[0]
for i in range(1,len(giv_array)):
    if giv_array[i]>max:
        max=giv_array[i]
print(max)

#############

class passbook:
     def __init__(self,username,initial_bal,acc_type):
           self.Username=username
           self.Accounttype=acc_type
           self.curr_balance=0
     def user_display(self):
          print("Username : ",self.username)
          print("Account type : ",self.Accounttype)
          print("current balance : ",self.curr_balance)
     def deposit(self):
          dep_amount=int(input("Enter the amount you want to deposit: "))
          self.curr_balance+=dep_amount
          print("Successfully credited \nRemaining  balance : ",self.curr_balance) 

     def withdraw(self):
          withdraw=int(input("Enter the amount you want to withdraw: "))
          self.curr_balance-=withdraw
          print("You have withdrawn ",withdraw," Remaining balance is ",self.curr_balance)
     def transfer(self,other,amount):
          self.curr_balance-=amount
          other.current_balance+=amount
class bank(passbook):
      def __init__(self,username,initial_bal,acc_type):
          super().__init__(username,initial_bal,acc_type)
          self.history=[]
      def deposit(self,deposit):
          super().deposit(deposit)
          self.history.append("\n" +deposit + " has been credited")
      def withdraw(self,withdraw):
          super().withdraw(withdraw)
          self.history.append("\n" + withdraw + " has been debited")
      def transfer(self,other,amount):
          super().transfer(other,amount)
          self.history.append("\n,you deposited {} to {}".format(amount,other.username)
      def transfer_history(self):
          print("\n", "Transaction History")
          for i in range(len(self.history)):
  username1 = input("Enter the username of 1st account holder: ")
acc_type1 = input("Please specify your account type: ")

username2 = input("Enter the username of 2nd account holder: ")
acc_type2 = input("Please specify your account type: ")

user1 = Passbook(username1,acc_type1)
user2 = Passbook(username2,acc_type2)

user1
msg="""
    1. Display user information
    2. Deposit money
    3. Withdraw money
    4. Money Transfer
    5. Transaction History
"""
which=int(input("Which user's info you want to print, 1.{} or 2.{}:\n".format(username1, username2)))

while True:
    print(msg)
    if (which == 1):
        ch= int(input("\nEnter your choice: "))
        if ch == 1:
            user1.disp_user()
        elif ch == 2:
            money = int(input("Enter the amount to be credited to your account: "))
            user1.deposit(money)
        elif ch == 3:
            money = int(input("Enter the amount to be debited from your account:"))
            user1.withdraw(money)
        elif ch == 4:
            money= int(input("Enter the amount to be transfeered to another account:"))
            user1.moneytransfer(user2, money)
        elif ch == 5:
            user1.hist_of_trans()
        else:
            print("\nThank you, You have been logged out successfully")
            quit()

    if (which == 2):
        ch= int(input("\nEnter your choice: "))
        if ch == 1:
            user2.disp_user()
        elif ch == 2:
            money = int(input("Enter the amount to be credited to your account: "))
            user2.deposit(money)
        elif ch == 3:
            money = int(input("Enter the amount to be debited from your account:"))
            user2.withdraw(money)
        elif ch == 4:
            money= int(input("Enter the amount to be transferred to another account:"))
            user2.moneytransfer(user1, money)
        elif ch == 5:
            user2.hist_of_trans()
        else:
            print("\nThank you, You have been logged out successfully")
            quit()    

######

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

##########

class rectangle:
     def __init__(self,length,width):
         self.length=length
         self.width=width
     def area(self):
         return self.length*self.width
     def perimeter(self):
         return 2*(self.length+self.width)
     def display(self):
         print("length of the rectangle is : ",self.length)
         print("width of the rectangle is: ",self.width)
         print("The area of the triangle is : ",self.area())
         print("The perimeter of the rectangle is : ",self.perimeter())
    
class parellelopiped(rectangle):
     def __init__(self,length,width,height):
          rectangle.__init__(self,length,width)
          self.height=height

     def volume(self):
          volume=self.length*self.width*self.height
          print(volume)
rect=rectangle(7,6)
print(rect.display())

print("_____________________________________________")
 
parallel=parallelopiped(7,9,8)
print("The volume is ", parallel.volume())


#########

#Recursion function


'''def addlist(data_list):
     total=0
     for x in data_list:
        if type(x) == type([]):
             total += addlist(x)
        else:
            total+=x
     return total
print(addlist([1,2,[3,4],[5,6]]))'''

#factorial using iterative

'''def fact(n):
    f=1
    while (n>0 ):
       f*=n
       n-=1
    return f
print(fact(5))'''


#factorial using recursuion

def factto(n):
    if n<=1:
       return 1
    else:
       if n>1:
           return n*factto(n-1)
print(factto(5))

############

def cube(n):
    n-=1
    total=0
    while (n>0):
       total+=n*n*n
       n-=1
    return total
print("The addition of cubes of all smallest integers " +"is",cube(5))

############

pack=[1,2,3,4,5,6,7,8,89]
odd_num=0
even_num=0
 
for x in  pack:
    if x%2 == 0:
       even_num+=1
    else:
       odd_num+=1
print(odd_num)
print(even_num)  

print("_____________________")

for x in range(6):
    if x==3 or x==4:
         continue  
    print(x,end = "")
print("\n")

###########

x,y=0,1
while y  <50:
   print(y)
   x,y=y,x+y 

##########

 '''for i in range(0,51):
    if i % 3 == True:
        print("FIZZ")
    elif i % 5 == True:
       print("BUZZ")
    elif i % 3 and i % 5:
       print("Fizzbuzz")''' 

for fizzbuzz in range(51):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)
	
##########

abc="Mechanic234"
l=0
d=0
for i  in abc:
   if i.isalpha():
       l+=1
   elif i.isdigit():
       d+=1
print(l)
print(d)
    

#########

A=['a','b','c']
B=['d','c']
C=[]
for i in A:
   if i not in B:
      C.append(i)
for k in B:
   if k not in A:
      C.append(k)

    
  
print(C)


print("________________________________")

for i in range(len(A)):
    for j in range(len(B)):
         if A[i]==B[j]:
            A.remove(A[i])
            B.remove(B[j])
           
print(A+B)

print("__________________________")

for i in A:
   for j in B:
       if i==j:
          A.pop(i)
          B.pop(j)
print(A+B)
            
################

#Dictionary

'''dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dict4={}
new_dict={}
new_dict.update(dic3)
print(new_dict)
for d in (dic1,dic2,dic3):
     dict4.update(d)
print(dict4)'''

'''D=dict()
for x in range(1,16):
    D[x]=x**2
print(D)'''

def mergedict(*dicts):
    result=dict()
    for d in dicts:
       result.update(d)
    return result
students1 = {
  'Theodore': 10,
  'Mathew': 11,
}
students2 = {
  'Roxanne': 9
}
print(mergedict(students1,students2))



A="Welcome"
print(A[::-1])


B=[1,8,6]
print(max(B))
C=tuple(B)
print(C)
print(min(C))

num1 = 15
num2 = 12
sum = num1 + num2

print("Sum of {} and {} is {}" .format(num1, num2, sum))


#########

val=[]
for i in range(100,401):
     s=str(i)
     if (int(s[0])%2==0) and (int(s[1]%2)==0) and (int(s[2]%2)==0):
         val.append(s)
try:
     print(val)
except:
     print(val)

#########

class parent:
     def __init__(self):
         self.__private_var=5
      
     def show(self):
         print(self.__private_var)
         print("Inside parent")

     def elig(self):
         abc="var"

obj=parent()
obj.show()

print(parent.abc)

###########

import math
nums=[1,15,15,1]
pnums=math.prod(nums)
print(pnums)


##########

import random

class flashcard:
	def __init__(self):
		
		self.fruits={'apple':'red',
					'orange':'orange',
					'watermelon':'green',
					'banana':'yellow'}
		
	def quiz(self):
		while (True):
			
			fruit, color = random.choice(list(self.fruits.items()))
			
			print("What is the color of {}".format(fruit))
			user_answer = input()
			
			if(user_answer.lower() == color):
				print("Correct answer")
			else:
				print("Wrong answer")
				
			option = int(input("enter 0 , if you want to play again : "))
			if (option):
				break

print("welcome to fruit quiz ")
fc=flashcard()
fc.quiz()

##########

import re
str="You are very beautiful"
x=re.findall("o",str)
y=re.findall("[o]",str)
print(y)
print(x)
k=re.search("very",str)
print(k)
l=re.split("are",str)
print(l)
j=re.sub("are","and",str)
print(j)

o=re.findall("very$",str)
print(o)
p=re.findall("a+",str)
print(p)
var="Get the stuff done for now"
g=re.findall("ff{1}",var)


##########

import random
lst=['s','w','g']

chance=10
no_of_chance=0
human_point=0
computer_point=0

print("\n\n\t\t\t\t Snake Water Gun Game\n\n")
print("\'s\' for snake \'w\' for Water \'g\' for Gun")

while no_of_chance < chance :
    userinput=input('snake water or gun : ')
    compinput=random.choice(lst)
    
    if userinput == compinput:
        print("Tie both 0 points each\n")
    elif userinput=="s" and compinput=="g":
        print("computer won")
        computer_point+=1
        print(f"you guess {userinput} and computer  guess is {compinput}\n")
        print("computer wins 1 point")
        print(f" computer point: {computer_point} and user point : {human_point} \n")
    elif userinput=="s" and compinput=="w":
        print("You won!")
        human_point+=1
        print(f"you guess {userinput} and computer guess is {compinput}\n")
        print("You win 1 point")
        print(f" computer point: {computer_point} Your point : {human_point} \n\n")

    elif userinput=="w" and compinput=="s":
        print("computer won!")
        computer_point+=1
        print(f"you guess {userinput} and computer guess is {compinput}\n")
        print("computer win 1 point")
        print(f" computer point: {computer_point} Your point : {human_point} \n\n")
    
    else:
        print("You have entered wrong input\n")
    
    no_of_chance+=1
    print(f"{chance - no_of_chance} left out of {chance}\n")
print("Game over")

if computer_point == human_point:
    print("\nGame is tied")
elif computer_point > human_point:
    print("Computer is won")
elif human_point > computer_point:
    print("You have won")

print(f"computer point is {computer_point} and you point is {human_point}")
 

#######

a=set([13,73,3,8,98,60])
b=set([67,8,3,66,55,44])
print(a.difference(b))

#####

import os 
print(os.path.getsize("calci.py"))


print("_______________")
 
x=5
y=6
z=x+y
print("\n%d+%d=%d"%(x,y,z))


#########

def sum(x,y):
     sum= x+y
     if sum >=15 and sum <=20:
        return 0
     else:
        print(sum)

sum(9,2)

print("____________________________________________")
 
def test_number5(x, y):
   if x == y or (x-y) == 5 or (x+y) == 5:
       return True
   else:
       return False
print(test_number5(7, 2))
print(test_number5(3, 2))
print(test_number5(2, 2))
print(test_number5(7, 3))
print(test_number5(27, 53))

##############

n=int(input("Enter the number you want to get the tables: "))
for i in range(1,11):
    print(n,'x',i,'=',n*i)


##########

'''given="Johnisrunning"
result=[]
for i in range(0,len(given),4):
    result.append(given[i])

for j in range(1,len(given),2):
    result.append(given[j])
for k in range(2,len(given),4):
    result.append(given[k])

print(result)'''


given_list=[[1,4,5],[1,3,4],[2,6]]
new_list=[]
for i in given_list:
     for j in i:
         new_list.append(j)
for i in range(0,len(new_list)):
     for j in range(i+1,len(new_list)):
          if new_list[i] > new_list[j]:
               new_list[i],new_list[j]=new_list[j],new_list[i]
print()
print(new_list)                 

#######


w1="QqWwEeRrTtYyUuIiOoPp"
row2="AaSsDdFfGgHhJjKkLl"
row3="ZzXxCcVvBbNnMm"
key1=""
key2=""
key3=""
new_list=[]
lis1=["hello","Alaska","dad","peace","omk","iew","jfs"]
for i in lis1:
   for j in i:
       if (j in row2) and (j not in row1) and (j not in row3):
           key1+=j
       elif (j in row3) and (j not in row1) and (j not in row2):
           key2+=j
       elif (j in row1) and (j not in row2) and (j not in row3):
           key3+=j
for i in lis1:
   if i in key1:
      new_list.append(i)
   if i in key2:
      new_list.append(i)
   if i in key3:
      new_list.append(i)
print(new_list)
###################################   alternate method
'''temp=[]
new_li=[]       
def keyboard(giv_str,list):
     for char in giv_str:
        if char in list:
             temp.append(char)
        if len(temp)==len(giv_str):
           new_li.append(giv_str)
print(new_li)  

for word in lis1:
     if word[0] in row1:
        keyboard(word,row1)
     elif word[0] in row2:
        keyboard(word,row2)
     elif word[0] in row3:
        keyboard(word,row3)'''

#!/usr/bin/python3
s = input() 
for i in ["isalnum()","isalpha()","isdigit()","islower()","isupper()"]:
   for j in s:
      if eval("j.{}".format(i)):
          print(True)
          break
      else:
          print(False)

########

class Employee:  
    __count = 0;  
    def __init__(self):  
        Employee.__count = Employee.__count+1  
    def display(self):  
        print("The number of employees",Employee.__count)  
emp = Employee()  
emp1=Employee()

try:
  print(emp.__count) 

except:
  print(emp.display())

A="myself"
B="Myself"

print(hex(id(A)))
print(hex(id(B)))
A="Myself"
print(hex(id(A)))


#Area of the square
 
class square:
    def __init(self):
       self.side=10
    def square(self):
       return f"The area of square is {self.side * self.side}"
  
s1=square()
print(s1.square())

class Bank:  
     def getroi(self):  
        return 10;  
class SBI(Bank):  
     def getroi(self):  
        return 7;  
      
class ICICI(Bank):  
     def getroi(self):  
        return 8;  
b1 = Bank()  
b2 = SBI()  
b3 = ICICI()  
print("Bank Rate of interest:",b1.getroi());  
print("SBI Rate of interest:",b2.getroi());  
print("ICICI Rate of interest:",b3.getroi());  

i=1
while i<=20:
  if i == 8:
    break
  print(i) 
  i+=1

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

print("a.add")
print("b.sub")
print("c.mul")
print("d.div")

choice=input("Enter your choice: ")
num1=int(input("Enter the 1st number: "))
num2=int(input("Enter the 2nd number: "))

if choice == 'a':
     print("The answer is ",add(num1,num2))
elif choice == 'b':
     print("The answer is ",sub(num1,num2))
elif choice == 'c':
     print("The answer is ",mul(num1,num2))
elif choice == 'd':
     print("The answer is ",div(num1,num2))
else:
     print("Invalid input")


def checkfun(*var):
     for i in var:
         if i!=var[3]:
            return f"All values are not equal"
     return f"All values are equal"

print(checkfun(1,2,3,4))
print(checkfun(2,2,2,2,2))

class GrandParent:
  def __init__(self, txt):
    print('got')
    print(self)
    self.txt = txt
  
  def grand_method(self):
    print('in meth ', self)
    print(self.txt)

class Parent:
  def __init__(self, txt):
    self.message = txt

  def printmessage(self):
    print(self.message)

class Child(Parent, GrandParent):
  def __init__(self, txt):
    gp = GrandParent(txt)
    super().__init__(txt)

x = Child("Hello, and welcome!")

x.printmessage()
x.grand_method()

class Student:  
        def __init__(self, name, id, age):  
            self.name = name  
            self.id = id  
            self.age = age  
      
s = Student("John", 101, 22)  
      
print(getattr(s, 'name'))  
      
setattr(s, "age", 23)  
      
print(getattr(s, 'age'))  
    
      
print(hasattr(s, 'id'))  
delattr(s, 'age')  
      
print(s.age)  

class sriram:
    hen="hello"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def Chick():
        hen="Bhai"
obj=sriram("MK",12)

        

print(obj.name)
print(obj.hen)

i=1
while i<=20:
  if i%2 == 0:
     i+=1
     continue
  print(i)
  i+=1

for od in range(1,20,2):
    print(od)
    
def div(n1,n2):
    return True if n1%n2 == 0 else False
    
n1=int(input("Enter 1st value: "))
n2=int(input("Enter 2nd value: "))
 
print(div(n1,n2))

filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[1]))

color_list = ["Red","Green","White" ,"Black"]
print( "%s %s"%(color_list[0],color_list[-1]))

exam_st_date = (11,12,2014)
print( "The examination will start from : %s / %s / %s"%exam_st_date)

for i in range(1,6):
    for j in range(5,0,-1):
        print(j,end="")
    print()    

lst=[4,"str",{'i':5},(6,5),[7,8,9]]
def empty(lst):
        return [type(i)() for i in lst]
print(empty(lst))

haystack = "leetcode"
needle = "leeto"

print(haystack.find(needle))

days = int(input("enter the number of days :"))
if(days == 0):
  print("No fine for you")
elif(days >=1 and days <=5):
  print("Fine amount: ", days * 0.5)
elif(days > 5 and days <= 10):
  print("Fine amount: ", days * 1)
elif(days > 10 and days <=30):
  print("fine amount: ", days *5)
elif(days > 30):
  print("your membership is cancelled")

def group_data(grpval,n):
     for value in grpval:
         if n == value:
             print(value)

print(group_data([1,8,91,-5,6],9))
print(group_data([12,71,-40,6,3],6))

def some_thing():
	return 0

if some_thing():
    print('Function is true')	
else:
    print('Function is false')    

n=int(input("Enter a number: "))
if n %2 != 0:
   print("wierd")
elif n%2 == 0 and (n > 2 and n< 5):
   print("Not wierd")
elif n%2 == 0 and (n > 6 and n < 20):
   print("wierd")
elif n%2 == 0 and n > 20:
    print("Not wierd") 
else:
    print("wierd")              

class A:
   def fun(self):
      self.var=12
      self.varsh=19
class B(A):
   def __init__(self):
       self.var=54
       self.varsh=63

o=A()
o1=B()
print(o1.var)

class person(object):
	def __init__(self,name,idnumber):
		self.name = name
		self.idnumber = idnumber

def display(self):
	print(self.name)
	print(self.idnumber)
	
def details(self):
	print("My name is {}".format(self.name))
	print("IdNumber: {}".format(self.idnumber))
	
class Employee(Person):
	def __init__(self, name, idnumber, salary, post):
		self.salary = salary
		self.post = post

		Person.__init__(self, name, idnumber)
		
	def details(self):
		print("My name is {}".format(self.name))
		print("IdNumber: {}".format(self.idnumber))
		print("Post: {}".format(self.post))


a = Employee('Rahul', 886012, 200000, "Intern")
a.display()
a.details

class user:
    def __init__(self,*aname):
       self.name=aname


O1=user(["sri","sarath",123])

print(O1.name)
O1.name="sai"
print(O1.name)

class New:
   x="java"
   y="python"
   v1="HTML"
   def old(self,C):
      print("i know ",New.x)
      print("i know ",New.y)
      print("I also know",C)

var=New()
var.old("C++")
var.v1="dj"
var.v2="feet"
print("hello",New.v1)
print(var.v1)

def istype(lis):
     if isinstance(x,list) == True:
          print("This is a list")
     if isinstance(x,tuple) == True:
          print("This is a tuple")
     if isinstance(x,set) == True:
          print("This is a set")
            

x=("sai","sri","sarath")

list_a=[12,45,90,78,30,89,75,60,55,98]

'''value=list(filter(lambda x:  (x%15 == 0),list_a))
print(value)

list_var=[21,7,6,4,0,3,-7,-95,-5]
M=list(filter(lambda x: x > 0,list_var))
print(M)

print("____________________--")

check_lis=[12,-3,6,-67,45,-2]
for x in check_lis:
   if x > 0:
     print(x," ")'''

check_var=[12,-3,-6,9,5,-40,-1,-3]
valve=(n for n in check_var if n >0)
print("\n",*valve)

'''new_list=[]
for i in list_a:
    if i%15==0:
       new_list.append(i)
print(new_list)'''

for row  in range(7):
    for col in  range(5):
       if ((col==0 or col==4) and row!=0) or ((row==0 or row==3) and (col>0 and col<4)):
           print("*",end="")
       else:
          print(end=" ")
    print()

print()

for row in range(7):
   for col in range(5):
      if ((row==0 or row==3 or row==6) and (col>0 and  col<4)) or (col==0 and row>0 and row<4) or (col==4 and row>3 and row<6):
           print("*",end="")
      else:
          print(end=" ")
   print() 
 
print()
  
for row in range(7):
    for col in range(5):
       if (row==0 or row==6 and col!=2) or (col==2):
          print("*",end="")
       else:
          print(end=" ")
    print()

print()

for row in range(7):
    for col in range(5):
       if col==0 or (row==0  or row==3 and (col>0 and col<4)) or  (col==4 and (row!=0 and row!=3)):
           print("*",end="")
       else:
           print(end=" ")
    print()

print()

for row in range(7):
   for col in range(7):
      if (col==0 or col==6) or ((row==col) and (col>0 and col<4)) or (row==1 and col==5) or (row==2 and col==4):
          print("*",end="")
      else:
         print(end=" ")
   print()
print()
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
         
print()
for row in range(6):
    for col in range(7):
       if (row ==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8):
           print("*",end="")
       else:
          print(end=" ")
    print()     


string="Mybarbadoscric"
print("%s"%string)
print("%.2s"%string)
print("%.5s"%string)
print(string[:6])

A=[]
n=int(input("Enter the number of values:"))

for i in range(0,n):
    A.append(input("Enter the item:  "))

print("The values are")

for i in A:
   print(i,end=" ")


list1=[1,2,66,34,2,35,99,34,54,6,21,99,33]
list2=[]

for i in list1:
   if i not in list2:
      list2.append(i)

print("\n",list2)

AK=["des","chas","THer"]
a="-".join(AK)
print(a)

print("____________________________________________")
A=[7,5,4,1,9]
print(all(i<2 for i in A))
print(all(i > 5 for i in A))

para=["25","35","45"]
print(".".join(para))

print("__________________")

a=["sri","Hi","boy"]
print(len(a))
print(max(a))
print(min(a))
print(list(range(5)))
print(list("sriram"))
kishan=["vijay","surya","Raina"]
print("hi:%s,hello:%s,bro:%s"%(kishan[0],kishan[1],kishan[2]))


I=[]  
n = int(input("Enter the number of elements in the list:"))  
for i in range(0,n):     
    I.append(input("Enter the item:"))     
print("printing the list items..")   
for i in I:   
    print(i, end = "  ")     

def concatenate_list(list):
      result=""
      for value in list:
          result+=str(value)
      return result

print(concatenate_list([1,41,61,2,9]))  
           

import numpy 
'''X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]
res=[[0,0,0],
     [0,0,0],
     [0,0,0]]

res=numpy.dot(X,Y)
print(res)

test_list = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]
new_l=[j for i in test_list for j in i]
print(new_l)

A =[[1, 2], [3, 4]]
  

B = [[4, 5], [6, 7]]
resu=numpy.add(A,B)
print(resu)'''
 
m= [[1,2],[3,4],[5,6]] 
print(numpy.transpose(m))

txt="Geeksforgeeks"
t=""
for i in txt:
   if i in t:
      pass 
   else:
      t+=i
print(t) 

A=[6,5,3,2,1]

for i in range(len(A)-1):
    if A[i]>=A[i+1]:
       print("Monotonically decreasing")
    elif A[i]<=A[i+1]:
       print("Monotonically increasing")

orig_arr=[1, 2, 3, 4, 5, 6, 7]
rotat_arr=[]
temp=[]
for i in range(2):
    temp.append(orig_arr[i])
for k in range(len(orig_arr)):
    rotat_arr.append(orig_arr[k])
result=rotat_arr[2:]+temp
print(orig_arr)
print(result)

#alternate way of rotration

arr = [12, 10, 5, 6, 52, 36]
pos=2
n=len(arr)

for i in range(0,2):
    x=arr[0]
    for j in range(0,n-1):
       arr[j]=arr[j+1]
    arr[n-1]=x
print(arr)
   
mark1 = int(input("Enter your mark1: "))
mark2 = int(input("Enter your mark2: "))
mark3 = int(input("enter your mark3: "))
Total=mark1+mark2+mark3
Average=Total/3
print("Total= " ,Total)
print("Average= ",Average)

if(mark1 >=35 and mark2 >=35 and mark3 >= 35):
  print("Result is pass")
  if(Average >= 90 and Average <= 100):
    print("Grade : A ")
  elif(Average >= 80  and Average <= 89):
    print("Grade : B ")
  elif(Average >= 70 and Average <= 79):
    print("Grade : C")
  else:
    print("Grade : 0")
else:
  print("Result is fail")
  print("Grade:No grade")


'''def print_value(str):
     if len(str) < 2:
         return ''
     return str[0:2]+str[-2:]
print(print_value("sriramsr"))
print(print_value("Mywekon"))
print(print_value("W"))
print(print_value("aj"))'''


'''def change_val(str):   #pgm to return the 1st value changed to $ in any of the characters
    char=str[0]
    str=str.replace(char,"$")
    str=char+str[1:]
    return str
print(change_val("return"))
print(change_val("sriramsr"))'''
 
'''def swapfun(a,b):
    new_a=b[0:2]+a[2:]
    new_b=a[0:2]+b[2:]
    print(new_a + ""+ new_b)
print(swapfun("sriram","vijay"))'''

'''def adding(a):
    b=len(a)
    if b > 2:
        if a[-3:] == 'ing':
            a+='ly'
        else:
            a+='ing'
    return a
print(adding("slicing"))
print(adding("watch"))'''


'''def removefun(str,n):
     first_part=str[:n]
     last_part=str[n+1:]
     print(first_part+last_part)
removefun("sriram",3)
removefun("welcomeboy",5)'''

def interchange(str):
     return str[-1:] + str[1:-1] + str[:1]
print(interchange("vijaybro"))


'''A=[1,3,4,56,7,3,-2]
min=A[0]
for i in A:
    if i > min:
       min= i


print(min)'''
 
'''def compare(str):
    count=0
    for word in str:
        if len(word) > 1 and word[0] == word[-1]:
            count+=1
    return count
print(compare(["abc","aukdc","alpha","ajay","Akka"]))'''

'''A=[21,-20,-34,76,47,88,76,21,3,2,8,55,-10]
B=[]
for x in A:
   if x not in A:
      B.append(x)
print(B)'''
'''a = [10,20,30,20,10,50,60,40,80,50,40]
B=set(a)
print(B)'''

'''def lenstring(n,str):
    lis=[]
    var=str.split(" ")
    for x in var:
       if len(x) > n:
           lis.append(x)
    return lis
print(lenstring(3,"Hi ji  brown fox returns to manchester and leeds"))'''

'''num = [7,8, 120, 25, 44, 20, 27]
vnum=[]
for x in num:
  if x %2 != 0:
     vnum.append(x)
print(vnum)'''

tuplex=("HELLOBITZKILLA")
print(tuplex[2:9:-2])

'''
A=[1,2,5,7,8,9]
lx=tuple(A)

tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
print(''.join(tup))'''

'''tuplex = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
print(tuplex[4])'''

'''tuplex = 2, 4, 5, 6, 2, 3, 4, 4, 7 
print(tuplex.count(4))
ls=list(tuplex)
print(ls)
print(ls.count(4))
print(2 in tuplex)
print(7 in ls)
'''
'''L=["a","f","h","l","k"]
L.remove("h")
print(L)

print(L.pop(2))'''

'''p=(2,3,5,6,7,7,3,2,1,0)
K=p[-8:-4]
print(K)'''


A=((2,"w"),(3,"p"),("l",6))
C=dict(A)
print(C)

x = ("w3resource")
y = reversed(x)
print(tuple(y))
x = (5, 10, 15, 20)
y = reversed(x)
print(tuple(y))

l = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
k=dict(l)
print(k)


'''def len_string(str):
    count=0
    for char in str:
        count+=1
    return count
print(len_string("Hi hello and welcome"))'''
    
                #prime number
'''start=1
end=20
for i in range(start,end):
     if i > 1: 
        for j in range(2,i):
            if (i%j==0):
                break
        else:
           print(i)''' 

'''import re
txt="Hi hello welcome to the world of engineers"
print(re.search("^Hi.* engineers$",txt))
print(re.findall("^Hi",txt))


L1=[5,7,3,2,5,3,7,6,4,8]
print(list(dict.fromkeys(L1)))

txt="Helloworld!"
print(txt[::-1])'''

new=[]
for i in range(1500,2700):
   if (i%7==0) and (i%5==0):
        new.append(i)
print(new)
 
a=input("ENTER:")
print(a[-1])


kilometer=float(input("Enter the kilometer:"))
conv_fact=0.621371
miles=kilometer*conv_fact
print("the conversion of %.2f kilometerets is %.2f"%(kilometer,miles))

for i in range(6):
    for j in range(i+1):
         print("*",end="")
    print()  

for i in range(6,0,-1):
    for j in range(i):
       print("*",end="")
    print()

'''for i in range(6):
    for j in range(i):
        print(i,end="")
    print()
for i in range(6,0,-1):
    for j in range(i):
        print(i,end="")
    print()

for i in range(1,6):
     for j in range(1,i+1):
         print(j,end="")
     print() 
for i in range(6,1,-1):
     for j in range(1,i+1):
        print(j,end="")
     print()'''


'''for i in range(1,6):
    for j in range(i):
        print('*',end="")
    print()'''
for i in range(5):
    for j in range(i,5):
        print(" ",end="")
    for k in range(i+1):
        print("*",end="")
    print()


def swapfun(list):
    size=len(list)
    list[0],list[size-1]=list[size-1],list[0]
    print(list)
swapfun([2,4,5,6,9])

my_list=[2,5,6,8,3]
a,b,*c=my_list
print(a)
print(b)
print(c)

A=[4,5,8,2,1,9,6,5]
print(sorted(A))

# Python program to print Positive Numbers in a List

# list of numbers
list1 = [-10, -21, -4, 45, -66, 93]

# using list comprehension
pos_nos = [num for num in list1 if num >= 0]

print("Positive numbers in the list: ", pos_nos)

L1=[2,4,7,5,3,3]
L2=L1[:]
print(L2)
	
list1 = [10, 20, 30, 20, 20, 30, 40,
         50, -20, 60, 60, -20, -20]
nl=[]
for i in range(len(list1)):
   for j in range(len(list1)):
       if list1[i]==list1[j] and list1[i] not in nl:
          nl.append(list1[i])
print(nl)

#cumulative addition
list=[10,19,60,35,33,2,7]
cum_list=[sum(list[:x:1]) for x in range(1,len(list))]
print(cum_list)

#cum method 2

ls=[18,33,78,45,3,99]
cum_sum=0
nl=[]
for i in range(0,len(ls)):
     cum_sum+=ls[i]
     nl.append(cum_sum)
print(nl)

sml=[]
for ele in ls:
   sum=0
   for k in str(ele):
       sum+=int(k)
   sml.append(sum)
print(sml)

A="Geeks for geeks code practice"
print(A.split())
B="".join(A)
print(B)
Rev_str=""
for i in range(len(A)):
     if i!=2:
        Rev_str+=A[i]
print(Rev_str)
        
print(A.replace("e","",3))   #3 is the occurances

nl_lis=["Geeks","for","Geeks"]
print(" ".join(nl_lis))
print("Geeks for Geeks".count("for"))


      #Dictionary comprehension
'''my_str="Good morning to the good persons out there and the good"
mydict={key : my_str.count(key) for key in my_str.split()}
print(mydict)

A="My new string is this"
vowel="Aeiou"
S=set({})
for i in A:
   if i not in vowel:
        S.add(i)
print(S)'''

import numpy as np
X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
 
Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]
res=[[0,0,0],
     [0,0,0],
     [0,0,0]]
'''for i in range(len(X)):
    for j in range(len(X[0])):
         res[i][j]=X[i][j]+Y[i][j]
print(res)'''

res=np.dot(X,Y)
print(res)

'''#from array import *
new_arr=[1,2,3,4,5]
new_arr.reverse()
print(new_arr)
print(new_arr.count(3))

a=2
b=4
print(a if a>b else b)

def facto(n):
    fact=1
    if n<1:
      return 1
    else:
       while n > 1:
          fact*=n
          n-=1
       return fact
print(facto(5))
sum=0
n=int(input(""))
check=str(n)
for i in check:
    sum+=int(i)**3
print(sum)
if sum==n:
   print("Yes amstrong number")
else:
   print("No")'''

'''for i in range(1,10):           #prime number
    for j in range(2,i):
         if i%j==0:
            break
    else:
        print(i)
                            #To check prime number
n=int(input(""))
for i in range(2,int(n/2)+1):
     if n%i==0:
       print("Not a prime number")
       break
     else:
       print("prime number")'''

'''val="a"            #To find the ascii value of a number
print(ord(val))'''

giv_array=[25,7,3,5,99,3,56,44,2]
'''temp_arr=[]
res_arr=[]
i=0
r=3
while i < 3:
      temp_arr.append(giv_array[i])   
      i+=1
while r< len(giv_array):
     giv_array[i]=giv_array[r]
     i+=1
     r+=1
res_arr[:]=giv_array[3:]+temp_arr[:]
print(res_arr)'''

################MAx of given array
max=giv_array[0]
for i in range(1,len(giv_array)):
    if giv_array[i]>max:
        max=giv_array[i]
print(max)

def cube(n):
    n-=1
    total=0
    while (n>0):
       total+=n*n*n
       n-=1
    return total
print("The addition of cubes of all smallest integers " +"is",cube(5))

pack=[1,2,3,4,5,6,7,8,89]
odd_num=0
even_num=0
 
for x in  pack:
    if x%2 == 0:
       even_num+=1
    else:
       odd_num+=1
print(odd_num)
print(even_num)  

print("_____________________")

for x in range(6):
    if x==3 or x==4:
         continue  
    print(x,end = "")
print("\n")

x,y=0,1
while y  <50:
   print(y)
   x,y=y,x+y 

 '''for i in range(0,51):
    if i % 3 == True:
        print("FIZZ")
    elif i % 5 == True:
       print("BUZZ")
    elif i % 3 and i % 5:
       print("Fizzbuzz")''' 

for fizzbuzz in range(51):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)
	
abc="Mechanic234"
l=0
d=0
for i  in abc:
   if i.isalpha():
       l+=1
   elif i.isdigit():
       d+=1
print(l)
print(d)
    

A=['a','b','c']
B=['d','c']
C=[]
for i in A:
   if i not in B:
      C.append(i)
for k in B:
   if k not in A:
      C.append(k)

    
  
print(C)


print("________________________________")

for i in range(len(A)):
    for j in range(len(B)):
         if A[i]==B[j]:
            A.remove(A[i])
            B.remove(B[j])
           
print(A+B)

print("__________________________")

for i in A:
   for j in B:
       if i==j:
          A.pop(i)
          B.pop(j)
print(A+B)
            
class parent:
     def __init__(self):
         self.__private_var=5
      
     def show(self):
         print(self.__private_var)
         print("Inside parent")

     def elig(self):
         abc="var"

obj=parent()
obj.show()

print(parent.abc)

import math
nums=[1,15,15,1]
pnums=math.prod(nums)
print(pnums)


import random
randlist=[]

for i in range(0,10):
     n=random.randint(1,50)
     randlist.append(n)
print(randlist)

import re
str="You are very beautiful"
x=re.findall("o",str)
y=re.findall("[o]",str)
print(y)
print(x)
k=re.search("very",str)
print(k)
l=re.split("are",str)
print(l)
j=re.sub("are","and",str)
print(j)

o=re.findall("very$",str)
print(o)
p=re.findall("a+",str)
print(p)
var="Get the stuff done for now"
g=re.findall("ff{1}",var)

def second_largest(array):
	array.sort()
	return array[-2]

array = [2,3,8,1,4]
print(second_largest(array))

a=set([13,73,3,8,98,60])
b=set([67,8,3,66,55,44])
print(a.difference(b))

class Nokia:
     company="Nokia India"
     website="Nokiaindia99@gmail.com"
   
     def contactdetails(self):
         print("Address:Cherry road , near poonamalle")

class Nokia1100(Nokia):
     def __init__(self):
        self.name = "Nokia 1100"
        self.year = 1999


     def product_details(self):
         print("Name is:",self.name)
         print("year is:",self.year)
         print("company:",self.company)
         print("website:",self.website)

product=Nokia1100()
product.product_details()
product.contactdetails()

import os 
print(os.path.getsize("calci.py"))


print("_______________")
 
x=5
y=6
z=x+y
print("\n%d+%d=%d"%(x,y,z))

# return sum of the series 0....n(number)

number = 5

def sum_of_series(number):
    sum_of_values = 0
    while number>0:
        sum_of_values+=number
        number-=1
    return sum_of_values

print(sum_of_series(number))

        
def sum(x,y):
     sum= x+y
     if sum >=15 and sum <=20:
        return 0
     else:
        print(sum)

sum(9,2)

print("____________________________________________")
 
def test_number5(x, y):
   if x == y or (x-y) == 5 or (x+y) == 5:
       return True
   else:
       return False
print(test_number5(7, 2))
print(test_number5(3, 2))
print(test_number5(2, 2))
print(test_number5(7, 3))
print(test_number5(27, 53))

def swap_letters(array):
    for idx in range(len(array)):
        if 'G' in array[idx]:
            temp_str = array[idx].replace('G','e')
            array[idx] = temp_str
    return array        

array = ['Gfg', 'is', 'best', 'for', 'Geeks']
print(swap_letters(array))

class Employee:  
    __count = 0;  
    def __init__(self):  
        Employee.__count = Employee.__count+1  
    def display(self):  
        print("The number of employees",Employee.__count)  
emp = Employee()  
emp1=Employee()

try:
  print(emp.__count) 

except:
  print(emp.display())

A="myself"
B="Myself"

print(hex(id(A)))
print(hex(id(B)))
A="Myself"
print(hex(id(A)))














































































































































































            
      

      
           
      
          
           
          
         






















           





























     



















































        































































