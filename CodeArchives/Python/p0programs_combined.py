class BasicCalculator:
      def __init__(self):
          self.curr_ans = 0

      def add(self,opt1,opt2):
          self.curr_ans=opt1+opt2
          return self.curr_ans

      def mul(self,opt1,opt2):
          self.curr_ans=opt1*opt2
          return self.curr_ans

      def sub(self,opt1,opt2):
          self.curr_ans=opt1-opt2
          return self.curr_ans

      def div(self,opt1,opt2):
          self.curr_ans=int(opt1/opt2)

opt1=int(input("Enter the 1st value: "))
opt2=int(input("Enter the 2nd value: "))
calc=BasicCalculator()
print("Multiplication:{}".format(calc.mul(opt1,opt2)))
print("division:{}".format(calc.div(opt1,opt2)))

# Calculator 

calc.add(2,3)
print(calc.curr_ans)

class flashcard:
  def __init__(self, word, meaning):
    self.word = word
    self.meaning = meaning
  def __str__(self):
    
    return self.word+' ( '+self.meaning+' )'
    
flash = []
print("welcome to flashcard application")

while(True):
  word = input("enter the name you want to add to flashcard : ")
  meaning = input("enter the meaning of the word : ")
  
  flash.append(flashcard(word, meaning))
  option = int(input("enter 0 , if you want to add another flashcard : "))
  
  if(option):
    break
    
print("\nYour flashcards")
for i in flash:
  print(">", i)

# Game

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

# Library

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

# Matrix 

m1=[[0 for i in range(4)]for j in range(4)]
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
            m4[j][i]=a
    a+=1
for i in m4:
    print(i)
print()
###################################################################              #To print 1234 in row col order
row=4
col=4
temp=1
new_list=[[0 for i in range(col)]for j in range(row)]

for i in range(row):
    for j in range(col):
       new_list[i][j]=temp
       temp+=1
for m in new_list:
    print(m)
print()

###########################################################################
mid=1
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
    print(i)
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

# Passbook

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

# Perimeter

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


# Rockpaper

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
 

# Task

row1="QqWwEeRrTtYyUuIiOoPp"
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
temp=[]
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
        keyboard(word,row3)

#!/usr/bin/python3
s = input() 
for i in ["isalnum()","isalpha()","isdigit()","islower()","isupper()"]:
   for j in s:
      if eval("j.{}".format(i)):
          print(True)
          break
      else:
          print(False)

# Class concept

#basic class program , here student() is the class name , name age are the class attributes 
class student:
    name="sriram"
    age = 21
    gender="male"
    print("My age is",age)   #To print inside the  function 
atmos=student()
#get attribute method

print(getattr(student, 'name'))
print(getattr(student,'age','gender'))

#dot notation method


print(student.name)
print(student.age)

#set attribute

setattr(student,'name','miyaan')
print(getattr(student,'name'))
print(isinstance(atmos,student))
print(type(atmos))
 #setting attributes by  dot notation 

student.city="Chennai"
print(student.city)


# Johnisrunning

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


# Dictionary 

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


# Logic

val=[]
for i in range(100,401):
     s=str(i)
     if (int(s[0])%2==0) and (int(s[1]%2)==0) and (int(s[2]%2)==0):
         val.append(s)
try:
     print(val)
except:
     print(val)

# Logic

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
  
# Recursion

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

# Tables

n=int(input("Enter the number you want to get the tables: "))
for i in range(1,11):
    print(n,'x',i,'=',n*i)

# Task

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

# Area 

#Area of the square
 
class square:
    def __init(self):
       self.side=10
    def square(self):
       return f"The area of square is {self.side * self.side}"
  
s1=square()
print(s1.square())


# Calculator

class BasicCalculator:
      def __init__(self):
          self.curr_ans = 0

      def add(self,opt1,opt2):
          self.curr_ans=opt1+opt2
          return self.curr_ans

      def mul(self,opt1,opt2):
          self.curr_ans=opt1*opt2
          return self.curr_ans

      def sub(self,opt1,opt2):
          self.curr_ans=opt1-opt2
          return self.curr_ans

      def div(self,opt1,opt2):
          self.curr_ans=int(opt1/opt2)

opt1=int(input("Enter the 1st value: "))
opt2=int(input("Enter the 2nd value: "))
calc=BasicCalculator()
print("Multiplication:{}".format(calc.mul(opt1,opt2)))
print("division:{}".format(calc.div(opt1,opt2)))

calc.add(2,3)
print(calc.curr_ans)


# Check

def checkfun(*var):
     for i in var:
         if i!=var[3]:
            return f"All values are not equal"
     return f"All values are equal"

print(checkfun(1,2,3,4))
print(checkfun(2,2,2,2,2))


# Div

def div(n1,n2):
    return True if n1%n2 == 0 else False
    
n1=int(input("Enter 1st value: "))
n2=int(input("Enter 2nd value: "))
 
print(div(n1,n2))


# Dummy

import random
print(random.randrange(0,50))

a,b=5,7
b,a=5,7
print(a)
print(b)

a=["m","k"]
b=["v","j"]
a.extend(b)
print(a)


print("_______________________________________________________")


class Employee:  
     def __init__(self, name, id):  
            self.id = id  
            self.name = name  
      
     def display(self):  
            print(("ID:{}\nName: {}".format(self.id, self.name))  
      
      
emp1 = Employee("John", 101)  
emp2 = Employee("David", 102)  
      
      
emp1.display()  
      
emp2.display()  

# Flash

class flashcard:
  def __init__(self, word, meaning):
    self.word = word
    self.meaning = meaning
  def __str__(self):
    
    return self.word+' ( '+self.meaning+' )'
    
flash = []
print("welcome to flashcard application")

while(True):
  word = input("enter the name you want to add to flashcard : ")
  meaning = input("enter the meaning of the word : ")
  
  flash.append(flashcard(word, meaning))
  option = int(input("enter 0 , if you want to add another flashcard : "))
  
  if(option):
    break
    
print("\nYour flashcards")
for i in flash:
  print(">", i)


































     











            
      

      
           
      
          
           
          
         





















