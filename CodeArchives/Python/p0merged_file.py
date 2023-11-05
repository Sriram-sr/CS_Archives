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
    target_file = 'merged_file.py'  # Replace with the desired merged file name

    merge_files_in_subfolders(main_folder, target_file)


dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

dict1.update(dict2)
print(dict1)

original_dict = {'a':1, 'b':2}
item= ('c', 3)

new_dict={}

new_dict[item[0]]=item[1] 

new_dict.update(original_dict)

print(new_dict)


def rearrange_to_larger(array):
    temp_list=[val for char in array for val in str(char)]
    temp_list.sort(reverse=True)
    num="".join(temp_list)
    return int(num)

array=[23,9,674,2,10]
print(rearrange_to_larger(array))

    
    

def find_difference(str_1,str_2):
    uncommon_words=[word for word in str_2.split() if word not in str_1.split()]
    return uncommon_words

A = "Geeks for Geeks" 
B = "Learning from Geeks for Geeks"
print(find_difference(A,B))

res=set(A.split()).symmetric_difference(set(B.split()))    #Alternate 
print(res)


string = "14, 625, 498.002"

string=string.replace(',','*')
string=string.replace('.',',')
string=string.replace('*','.')

print(string)

country_code={'India':10044,
        'Australia':10004,
        'England':91004}
print(country_code['India'])
country_code.setdefault('England',1000006)
country_code.setdefault('south_africa',123456)
print(country_code['south_africa'])
print(country_code.get('England'))

from collections import defaultdict
country_code=defaultdict(lambda:'key not found')
print(country_code['sri_lanka'])   #It wont throw you error because defaultdict is set

new_dict={'name':'sriram',
        "age":21,
        'gender':"male"}
new_dict['address']='chennai'
new_dict.pop('address')
print(new_dict)
print(dict([(1,"age"),(2,"sex")]))

print(dict.fromkeys(new_dict,'oops'))

b=set([9,3,56,3,3432,235,2])
print(sorted(b))

test_dict = {'month' : [1, 2, 3],
             'name' : ['Jan', 'Feb', 'March']}
print(dict(zip(test_dict["month"],test_dict["name"])))

new_tuple=(1,2,)
print(new_tuple)

data = [("Apples", 5, "20"), ("Pears", 1, "5"), ("Oranges", 6, "10")]

print(sorted(data,key=lambda x:x[1]))


print(new_dict.get("address","chennai"))

key=new_dict.keys()

new_dict.update({"mob":1244})
print(key)
val=new_dict.items()
print(val)
print(new_dict)

key_value={2:64,1:69,4:23,5:65,6:34,3:76}
def sort_dict(n):
    for i in sorted(n):
        print((i,n[i]),end="")
    print()
sort_dict(key_value)
print(sorted(key_value,key=lambda x:key_value[x]))
print(sorted(key_value.values()))
print(sorted(key_value.items()))
print(sorted(key_value.items(),key=lambda x:(x[1])))  #To sort using value  

new_list=['a','e','i','o','u']
find_list=['g','e','e','k','s']
print(list(filter(lambda x:x in new_list,find_list)))

l1=[12,31,44,55,66,77]
print(list(filter(lambda x:x%2==0,l1)))



new_list=[2,3,4,5,6,7]
def square(n):
    return n**2
print(list(map(square,new_list))) #Using normal function

print(list(map(lambda x:x**2,new_list)))   #Using lambda fun

print(list(map(lambda x :x+x,new_list)))

list2=[1,2,3,4,5]                                  #To add two lists
print(list(map(lambda x,y:x+y,new_list,list2))) 

str_list=['Hello','World']
print(list(map(list,str_list)))

str_list=['2','3','9']
print(list(map(float,str_list)))

len_list=['Hello','world','python','py','realworldentity']
print(list(map(len,len_list)))                               #To find the length of each word

l1=[2,3,4,6,7]
l2=[2,5,3,6]
#print("\t\tH")
print(list(map(pow,l1,l2)))

print(list(map(lambda x,y:x**y,l1,l2)))   #Finding pow using lambda 

list1=["sri ram","hi","cricketer"]
print(list(map(str.capitalize,list1)))
print(list(map(str.upper,list1)))
print(list(map(str.lower,list1)))

dot_list=['...#..hello','world...']
print(list(map(lambda x:x.strip('.#'),dot_list)))


def various(x):
    return x**x,x+x,x**2
new_l=[2,5,9,8,7]
print(list(map(various,new_l)))

def check(x):
    return x.replace(',','.')
num=['12.3','15,6']
print(list(map(check,num)))

import math
def mixer(x):
    return x>=0
newli=[-81,25,9,-16]          #To find the square root of only positive values
def square_root(y):
    cleaned_square=map(math.sqrt,filter(mixer,newli))
    return list(cleaned_square)
print(square_root(newli))
result=[]


new_dict={'a':100,'b':200,'c':300}
def sumdic(n):
    sum=0
    for i in n:
        sum+=n[i]
    return sum
print("The sum of the values is {}".format(sumdic(new_dict)))


def unpack(a,b,c,d):
    print(a)
    print(b)
    print(c,d)

pack_list=[2,4,6,8]

unpack(*pack_list)

def get_sum(*args):
    return sum(args)

print(get_sum(5,6,8,3))

#dictionary can also be passed

def using_dict(x,y,z):
    return x,y,z

d = {'x':2, 'y':4, 'z':10}
print(using_dict(**d))

def use_kwarg(**kwarg):
    print(type(kwarg))
    
    for key in kwarg:
        print("%s=%s"%(key,kwarg[key]))

use_kwarg(Name=9,Age=21,Place=24)

#Assigning Subsequent Rows to Matrix first row elements

test_list = [[5, 8, 10], [2, 0, 9], [5, 4, 2], [2, 3, 9]]

res_dict={}
temp=test_list[0]
test_list.remove(temp)

for idx in range(len(temp)):
    res_dict[temp[idx]]=test_list[idx]

print(res_dict)    

test_list = [[5, 8, 10], [2, 0, 9], [5, 4, 2], [2, 3, 9]]

new_res=dict(zip(test_list[0],test_list[1:]))
print(new_res)

a="Geeks"
b=b"Geeks"

c=a.encode("ASCII")
d=b.decode("ASCII")

if b==c:
    print("Encode successful")
if a==d:
    print("Decode successful")

x="This is outside function"
def check_fun():
    global x
    x="This is inside a function"
 
def new_fun():
    x="This is newly created variable"
print(x)
check_fun()
new_fun()
print(x)
print(x)


#Once you have declared  a variable global the real global variable won't be considered

def unpack(a,b,c,d):
    print(a)
    print(b)
    print(c,d)

pack_list=[2,4,6,8]

unpack(*pack_list)

def get_sum(*args):
    return sum(args)

print(get_sum(5,6,8,3))

#dictionary can also be passed

def using_dict(x,y,z):
    return x,y,z

d = {'x':2, 'y':4, 'z':10}
print(using_dict(**d))


import re

ip=str(input("Enter the IP: "))

regex="^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

if re.search(regex,ip):
    print("Valid IP")
else:
    print("Invalid IP")

ip=input(str("Enter IP address: "))
def check_validity(ip):
    global ip_list
    ip_list=ip.split(".")
    flag=1
    if len(ip_list)==4:
        for each in ip_list:
            if int(each)>255 or int(each)<0:
                flag=0

    if len(ip_list)!=4 or flag==0:
        print("Invalid IP")
    else:
        class_check(ip)
    
def subnet_mask(classs):
    if classs=="A":
        print("Subnet mask is {}".format("255.0.0.0"))
    elif classs=="B":
        print("Subnet mask is {}".format("255.255.0.0"))
    elif classs=="C":
        print("Subnet mask is {}".format("255.255.255.0"))


def class_check(ip):
    classs=''
    sub=int(ip_list[0])
    if sub>=0 and sub<=127:
        classs="A"
    elif sub>=128 and sub<=191:
        classs="B"
    elif sub>=192 and sub<=223:
        classs="C"
    elif sub>=224 and sub<=239:
        classs="D"
    elif sub>240 and sub<=255:
        classs="E"
    print("Class is {}".format(classs))
    subnet_mask(classs)
  
check_validity(ip)



jack = { "name":"Jack Frost",
         "assignment" : [80, 50, 40, 20],
         "test" : [75, 75],
         "lab" : [78.20, 77.20]
       }
         
james = { "name":"James Potter",
          "assignment" : [82, 56, 44, 30],
          "test" : [80, 80],
          "lab" : [67.90, 78.72]
        }
  
dylan = { "name" : "Dylan Rhodes",
          "assignment" : [77, 82, 23, 39],
          "test" : [78, 77],
          "lab" : [80, 80]
        }
          
jess = { "name" : "Jessica Stone",
         "assignment" : [67, 55, 77, 21],
         "test" : [40, 50],
         "lab" : [69, 44.56]
       }

tom = { "name" : "Tom Hanks",
        "assignment" : [29, 89, 60, 56],
        "test" : [65, 56],
        "lab" : [50, 40.6]
      }
student_list=[jack,james,dylan,jess,tom]

def calculate_avg(name):
    assignment_sum=sum(name['assignment'])/len(name['assignment'])
    test_sum=sum(name['test'])/len(name['test'])
    lab_sum=sum(name['lab'])/len(name['lab'])
    student_avg=(0.1*assignment_sum)+(0.7*test_sum)+(0.2*lab_sum)
    return student_avg
def grade_calculator(name):
    if calculate_avg(name)>=90:
        return f"Grade:A"
    elif calculate_avg(name)>=80:
        return f"Grade:B"
    elif calculate_avg(name)>=70:
        return f"Grade:C"
    elif calculate_avg(name)>=60:
        return f"Grade:D"
    elif calculate_avg(name)>=50:
        return f"Grade:E"
    else:
        return f"Grade:E"

def student_display(name,funcname):
    print("The avgerage mark of {} is {}".format(name,calculate_avg(funcname)))
    print("The grade for {} is {}".format(name,grade_calculator(funcname)))

def class_avg(slist):
    avg_list=[]
    for i in student_list:
        avg_list.append(calculate_avg(i))
        average=sum(avg_list)/len(avg_list)
        return average
student_display("jack",jack)
student_display("james",james)
student_display("dylan",dylan)
student_display("jess",jess)
student_display("tom",tom)

print("\nThe class average is {}".format(class_avg(student_list)))




class student:
    mark1=78
    mark2=99
    def avg_mark(self):
        sum=student.mark1+student.mark2
        avg=sum/2
        return sum,avg
new_obj=student()
print(new_obj.mark2)
print(new_obj.avg_mark())
print(type(new_obj))

giv_list= [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,
                  4, 4, 4, 2, 2, 2, 2]
check_list=list(set(giv_list))
count_list=[]
for i in check_list:
    count_list.append(giv_list.count(i))
new_dict={}    
for i in range(len(check_list)):
    new_dict[check_list[i]]=count_list[i]
print(new_dict)  
                 #Alternate
from collections import Counter
ans=Counter(giv_list)
for k,v in ans.items():
    print("%d : %d"%(k,v))

res_dict={}
for i in giv_list:
    if i in res_dict:
        res_dict[i]+=1
    else:
        res_dict[i]=1
print(res_dict)        



res2_dict={}
for m in giv_list:
    res2_dict[m]=giv_list.count(m)
print(res2_dict)    


from collections import Counter
test_list = [4, 6, 6, 4, 2, 2, 4, 4, 8, 5, 8]
test_dict=Counter(test_list)
res_dict={}
for key in test_dict:
    res_dict[key]=[]                            #To find the frequency of repeated elements
for key,val in test_dict.items():
    for j in range(val):
        res_dict[key].append(val)
print(res_dict)        

res={key:[key]*val for key,val in Counter(test_list).items()} #Alternate
print(res)

dic1={'abc':'hello',
        'bcd':'world'}
dic2={'xyz':'hi',
        'gyh':'boys'}
result={**dic1,**dic2}
print(result)

class parent:
    def __init__(self,name1,name2):
        self.fname=name1
        self.lname=name2
    def display(self):
        print("last name is "+ self.lname)
class student(parent):
    pass
x=student("sri","ram")
x.display()


new_str = "geeksforgeeks"
k=2
temp_str=""
for i in range(len(new_str)):     #To find the kth non repeating value
    if i<len(new_str)-1:
        if new_str[i] not in new_str[i+1:] and new_str[i] not in new_str[:i]:
            temp_str+=new_str[i] 
answer=temp_str[k-1]
print(answer)

class basic():
    def check(self,num):
        if num%2==0:
            print("The number is Even")
        elif num%2!=0:
            print("The number is Odd")
n=basic()
x=int(input("Enter the number: "))
n.check(x)

from more_itertools import distinct_permutations

for p in distinct_permutations('1356'):
    print(''.join(p))

new_dict={"Java":[2,3,5,2,6],"Python":[1,8,12,6,4]}
list_1=[]
rep_list=[]
for val in new_dict.values():
    list_1+=val
for i in range(len(list_1)):
    if list_1[i] in list_1[i+1:] or list_1[i] in list_1[:i]:
        rep_list.append(list_1[i])                             #To remove repeated values
for i in rep_list:
    for j in new_dict.values():
        if i in j:
            j.remove(i)
print(new_dict)            
            

from collections import Counter
giv_str= "Python is great and Java is also great"
giv_str=giv_str.split()
new_dict=Counter(giv_str)
res_list=[]                     # To remove duplicate values using dictionary
for key,val in new_dict.items():
    if val==1:
        res_list.append(key)
print(res_list)        

s = "Python is great and Java is also great"
s=s.split()
r=[]                               #Alternate
for i in s:
    if s.count(i)<=1 and i not in r:
        r.append(i)
print(r)        



test_list = ["Gfg", "is", "Best"]
subs_dict = {
    "Gfg" : [5, 6, 7],
    "is" : [7, 4, 2],
}

k=2                                #Replace the key value with k'th index

for i in range(len(test_list)):
    for j in subs_dict.keys():
        if test_list[i]==j:
            test_list[i]=subs_dict[j][k]
print(test_list)         

test_str = 'geekforgeeks best for geeks'
repl_dict = {'geeks' : 'all CS aspirants'}
test_list=test_str.split()                   #To replace a word in a dictionary
res=[]
for wrd in test_list:
    res.append(repl_dict.get(wrd,wrd))
result=" ".join(res)
print(result)


test_str = 'gfg is best for geeks'
test_dict = {'geeks' : 1, 'best': 6}
for key in test_dict:
    if key in test_str.split():                 #To remove a word
        test_str=test_str.replace(key,"")
print(test_str)           

                                                            
test_str=test_str.split()                               #Alternate
res_list=[i for i in test_str if i not in test_dict]
ans=" ".join(res_list)
print(ans)


class selfcheck:
    def __init__(self,name,age):
        self.myname=name
        self.myage=age
    def checkit():
        print("My name is {} and my age is {}".format(self.myname,self.myage))
new_ob=selfcheck("Sriram",21)
new_ob.checkit()

class selfcheck:
    def __init__(self,name,age):
        self.myname=name
        self.myage=age
    def checkit(self):
        print("My name is {} and my age is {}".format(self.myname,self.myage))
new_ob=selfcheck("Sriram",21)
new_ob.checkit()
new_ob.myage=25     #Changing the variable in init using the object
new_ob.checkit()
    
    

new_str="Geeksforgeeks"
org_str=""
for i in range(len(new_str)):
    if new_str[i] not in new_str[i+1:] and new_str[i] not in new_str[:i]:
        org_str+=new_str[i]              #To return only the repeated values
res_list=[]
for i in new_str:
    if i not in org_str:
        res_list.append(i)
print(set(res_list))        

from collections import Counter
ar1 = [1, 5, 10, 20, 40,20, 80]
ar2 = [6, 7, 20, 80, 100,20]
ar3 = [3,20, 4, 15, 20, 30, 70, 80, 120]  #To find the common elements and their count
ar1=Counter(ar1)
ar2=Counter(ar2)
ar3=Counter(ar3)
result_dict=dict(ar1.items() & ar2.items() & ar3.items())
common=[]
for key,val in result_dict.items():
    for i in range(val):
        common.append(key)
print(common)        
print(result_dict)

def swapcase(str):
    output=''
    for char in str:
        if char.isupper()==True:
            output+=char.lower()
        elif char.islower()==True:
            output+=char.upper()
        else:
            output+=char
    return output
string=input("Enter the string: ")
result=swapcase(string)
print(result)



n1=int(input("Enter the start value: "))
n2=int(input("Enter the end value: "))
time=int(input("Enter time: "))
new_list=[]
for i in range(n1,n2+1):
    new_list.append(i)
rev_list=new_list[::-1]    
ret_value=n2-n1
rem=int(time%ret_value)   #To print the position of time value in the given range
ans=0
q=time//ret_value
if q%2==0:
    for j in range(len(new_list)):
        ans+=new_list[rem]
        break
elif q%2!=0:
    for h in range(len(new_list),-1,-1):
        new_list
        ans+=rev_list[rem]
        break       
print(ans)      


test_dict = {"Gfg" : [5, 7, 5, 4, 5],
             "is" : [6, 7,7], 
             "Best" : [9, 9, 6, 5, 5]}
def find_unique(test_dict):
    max_val=0
    max_key=None
    for key in test_dict.keys():                   #To find the key with max unique values
        if len(set(test_dict[key]))>max_val:
            max_val=len(set(test_dict[key]))
            max_key=key
    print(max_key)        
find_unique(test_dict)

#Alternate
print(sorted(test_dict,key=lambda x:len(set(test_dict[x])),reverse=True)[0])


from collections import Counter
votes = ["john", "johnny", "jackie", 
                    "johnny", "john", "jackie", 
                    "jamie", "jamie", "john",
                    "johnny", "jamie", "johnny", 
                    "john"]
votes=Counter(votes)
max_vote=[]
for i in votes.values():
     max_vote.append(i)        #To print who has maximum number of votes
max_value=max(max_vote)

for key,val in votes.items():
    if val==max_value:
        print(key)

new_dict={}
for k,v in votes.items():
    new_dict[v]=k
maxVote = sorted(new_dict.keys(),reverse=True)[0]
print(maxVote)
   
if len(new_dict[maxVote])>1:
    print (sorted(new_dict[maxVote])[0])
else:
    print (new_dict[maxVote][0])

   


class perform:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def display(self):
        print("The addition of {} & {} is {}".format(self.n1,self.n2,self.add))
    def addition(self):
        self.add=self.n1+self.n2
add=perform(5,9)
add.addition()
add.display()        

class dog():
    def __init__(self,bread,color):
        self.color=color
        self.bread=bread
        print("Object created")
    def new_dog(self,name):
        self.name=name
        print("Name of the dog is "+self.name)
        print("Bread is "+self.bread)
        print("Color is "+self.color)
sweety=dog('lab','brown') 
sweety.new_dog("sweety")
choco=dog('choco','black')
choco.new_dog('choco')



class student:
    name="Sriram"
    age=21
    adress="kovai"
    def new_fun():
        print(student.name)

    def inst(self):
        print("age: "+str(student.age))

obj=student()
obj.address="chennai"
print(obj.age)
print(obj.address)
print(student.__dict__)
print(student.adress)
student.new_fun()          #Class method

obj.inst()                #Instance method

def display(func):
    def runningfun():
        print("Executing")
        func()
    return runningfun()

@display
def newfun():
    print("Go to display")
newfun()    

class temp:
    def __init__(self,user):
        self.use=user
        print("Constructor created")
    def __del__(self):
        print("Constructor deleted")
    
    def new_fun(self):
        print(self.use)
new_ob=temp('sriram')      
new_ob.new_fun()


class check:
    def __init__(self,giname):
        print("Called when obj created")
        self.name=giname
    def usefun(self):
        print("The name is : "+self.name)
obj1=check("sri") 
obj2=check("ram")
obj1.usefun()
obj2.usefun()


class parent:
    def __init__(self,name):
        self.name=name
    def display(self):
        return self.name
    def usename(self):
        return True
class chld(parent):
    def childfun(self):
        print("Using "+username())
obj=parent('sri')
print(obj.name,obj.username())

class new:
    def __init__(self,name,age

try:
    b=5
    print(b)
except Exception as error:
    print(error)
else:
    print("No errors")
finally:
    print("Over")

try:
    a=10
    print(b)
except NameError as error:
    print("10")

try:
    a="pk"
    print(int(a))
except ValueError as error:
    print("string")

try:
    list_1=[2,3,4]
    print(list_1[3])
except IndexError as error:
    print("correct Index")




class Grandfather:
    new_var='Hi'
    def display(self):
        print(new_var)
o=Grandfather()
o.display()




import socket

c=socket.socket()

c.connect(("192.168.0.110",9999))

while True:
    print(c.recv(1024).decode())
    msg=input("Enter message: ")
    c.send(bytes(msg,"utf-8"))

import socket
import threading

c=socket.socket()
c.connect(("192.168.0.110",7777))

def send():
    
    while True:
          v=str(input("Enter: "))
          c.sendall(bytes(v,"utf-8"))
          
          
def recv():

    while True:
          print(c.recv(1024).decode())
   
thread_1 = threading.Thread(target = send)
thread_2 = threading.Thread(target = recv)

thread_1.start()
thread_2.start()
    
    
    

prices=[7,1,5,3,6,4]
profit_list=[]

for day in range(len(prices)):
    for nxt in range(day+1,len(prices)):
        if prices[day]>prices[nxt]:
            pass
        else:
            profit=prices[nxt]-prices[day]
            profit_list.append(profit)

print("Maximum profit of the week is {}".format(max(profit_list)))


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1,n2=0,0
        for i in range(len(num1)):
            n1=(n1*10)+(ord(num1[i])-48)
        for j in range(len(num2)):
            n2=(n2*10)+(ord(num2[j])-48)
        return str(n1*n2)


import time
import threading

def calc_square(arr):
    for n in arr:
        print("Square: ",n**2)
        time.sleep(0.2)

def calc_cube(arr):
    for n in arr:
        print("Cube: ",n**3)
        time.sleep(0.2)
arr=[2,3,4,5]

t=time.time()

t1=threading.Thread(target=calc_square,args=[arr])
t2=threading.Thread(target=calc_cube,args=[arr])


t1.start()
t2.start()

t1.join()
t2.join()

#calc_square(arr)
#calc_cube(arr)

print("Done in :",time.time()-t)

import time
from threading import *
class process1(Thread):
    def run(self):
        for num in range(5):
            print("Hi")
            time.sleep(0.5)

class process2(Thread):
    def run(self):
        for num in range(5):
            print("Hello")
            time.sleep(0.5)
t1=process1()
t2=process2()

t1.start()
t2.start()

t1.join()   #To print "Bye" (main thread) after the child threads gets over join fn is used
t2.join()
print("Bye")

import threading
import time

def fun_1():
    for t in range(5):
        print("Waiting 1 second...")
        time.sleep(1)
        print("Waiting done....")

def fun_2():
    for t in range(5):
        print("Waiting 2 second...")
        time.sleep(1)
        print("Waiting done....")

t=time.time()

t1=threading.Thread(target=fun_1)
t2=threading.Thread(target=fun_2)

t1.start()
t2.start()

t1.join()
t2.join()

print("Done in :",round(time.time()-t),"seconds")


print('ll")l


def outer():
    x=10
    def inner():
        y=12
        result=x+y  #Calling a function with a variable
        return result
    return inner
a = outer()
print(a())


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
    # print(rev_number)
    num//=10
print(rev_number)

A_list=[2,5,6,7,9]
for i in range(len(A_list)):
    print(all(A_list[i] <=A_list[i+1]) or (A_list[i] >= A_list[i+1]))
counter=0    
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
print(math.prod(mul_list))

new1_list=[1,2,-4,5,-7,9,-4,6,-20]
num=0
while num<len(new1_list):
    if num%2==0:
        print(new1_list[num])
    num+=1

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


n=1234
txt=""
while n>0:
    rem=n%10
    n=n//10
    txt+=str(rem)
print(txt)    





# new_list=list(range(1,11))
# d=3 #rotation number
# i=0
# temp_list=[]
# while i<d:
#     temp_list.append(new_list[i])
#     i+=1
# i=0
# while d<len(new_list):
#     new_list[i]=new_list[d]
#     d+=1
#     i+=1
# new_list[:]=new_list[:i]+temp_list
# print("The list after rotation is ",new_list)

def rotate_list(lis,n):
    r=n
    temp_list=lis[:r]
    res=lis[r:]+temp_list
    return res

lis=[2,3,4,6,1,7,9,-2,3]
n=3
print(rotate_list(lis,n))    




samp_str="ABCDEFGHIJKLIMNOQRSTUVWXYZ"
length=len(samp_str)
t=4
for i in range(0,length,t):
    print(samp_str[i:i+t])
num=2653
res=''
for i in str(num):
    res=i+res
print(res)    
A="MananVohra is"
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
res=Counter(new_str)      
print(res)          #Alternate method
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













def fun(arg):
    print("Hello",arg)

import mymodule
mymodule.fun("sri")


Nums = [3,2,4,7,8,3,5,6,1]
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
        temp_list.append(j)      #To get sorted unique values from dictionary
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
print(lis)
print(sorted(lis,key=lambda x:x["age"]))
print(sorted(lis,key=lambda x:(x["name"],x["age"])))
print(sorted(lis,key=lambda x: x["name"],reverse=True))

b="The wait is over"
print(b.split())
A=["the", "wait","is","over"]
print(" ".join(A))


new_list1=[2,34,56,1,34,6,2]
new_list1.sort(reverse=True)
print(new_list1)






print(sorted(lis,key=lambda x:x['age'],reverse=True))

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


def usage_yield(val):
    while val>0:
        if val%2==0:
            yield val
        val-=1
 
val=10 
for even in usage_yield(val):
    print(even)

def check_subseq(txt,sub):
    for char in sub:
        if char not in txt:
            print(False)
            break
    else:
        print(True)

s = "axc"
t = "ahbgdc"
check_subseq(t,s)

def check_iter(list):
    iter_val=iter(list)
    
    while True:
        try:
            values=next(iter_val)
            print(values)

        except StopIteration: 
            break
    
nl=[1,2,3,4,6]
check_iter(nl)


def replace_by_X(txt,sub):
    res_str=""
    for char in range(len(txt)-2):
        if txt[char:char+2]==sub:
            idx=char+1

        elif char==idx and txt[idx+1:idx+3]!=sub:
            res_str+="X"
        else:
            res_str+=txt[char]

    temp_str=""
    for i in res_str:
        if i!='b':
             temp_str+=i
    return temp_str
                



txt="abababcdefababcdab"
sub="ab"

print(replace_by_X(txt,sub))



Input=[11, 5, 17, 18, 23, 50,60,70]

a=1
b=5

res=Input[:a]+Input[b+1:]

print(res)


def remove(Inp):
    res=filter(None,Inp)
    return res

Input= [(), ('ram','15','8'), (), ('laxman', 'sita'), 
                  ('krishna', 'akbar', '45'), ('',''),()]
print(remove(Input))

    

def remove_dup_differently(list):
    res_list=[]
    for char in list:
        count_val=list.count(char)
        if count_val>1:
            if res_list.count(char)==0:
                res_list.append(char)

    return res_list            


list = [1,2,1,2,3,4,5,1,1,2,5,6,7,8,9,9] 
print(remove_dup_differently(list))
from collections import Counter
def group_similar(list):
    new_dict=Counter(list)
    for key,val in new_dict.items():
        new_dict[key]=[key for time in range(val)]

    return new_dict

test_list = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8]
print(group_similar(test_list))        


def mirror_characters(alpha_listi,txt,n):
    half=len(alpha_list)//2
    generic=alpha_list[:half]
    reverse=list(reversed(alpha_list[half:]))
    match_dict={}
    add=txt[:n-1]
    txt=txt[n-1:]
    for idx in range(half):
        match_dict[generic[idx]]=reverse[idx]
    for char in range(len(txt)):
        for key,val in match_dict.items():
            if txt[char]==key:
                txt=txt.replace(txt[char],val)
            elif txt[char]==val:
                txt=txt.replace(txt[char],key)

    return add+txt    

alpha_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
N = 6
txt="pneumonia"
print(mirror_characters(alpha_list,txt,N))




def non_repeating(str,k):
    temp_list=[]
    for char in range(len(str)-1):
        if str[char] in str[char+1:]:
            pass
        else:
            temp_list.append(str[char])

    return temp_list[k-1]

str ='geeksforgeeks'
k = 2
print(non_repeating(str,k))


def remove_repeated(test_dict):
    comm_list=[val for val in test_dict.values()]
    temp_list=[inner for outer in comm_list for inner in outer]
    to_be_removed=[]

    for char in range(len(temp_list)-1):
        if temp_list[char] in temp_list[:char] or temp_list[char] in temp_list[char+1:]:
            to_be_removed.append(temp_list[char])

    for key in test_dict.keys():
        key_list=test_dict[key]
        emp_list=[]
        for val in key_list:
            if val not in to_be_removed:
                emp_list.append(val)
        test_dict[key]=emp_list

    return test_dict    
test_dict = {'Manjeet': [1], 'Akash': [1, 8, 9]}
print(remove_repeated(test_dict))

def remove_the_keyvalue(test_str,test_dict):
    temp_list=test_str.split()
    for word in range(len(temp_list)):
        if temp_list[word] in test_dict:
            temp_list[word]=""
    res_str=" ".join(temp_list)

    return res_str        

test_str = 'gfg is best for geeks'
test_dict = {'geeks' : 1, 'best': 6}
print(remove_the_keyvalue(test_str,test_dict))      

def replace_by_k(test_list,rep_dict,k):
    for val in range(len(test_list)):
        for key in rep_dict:
            if test_list[val]==key:
                rep_list=rep_dict[key]
                test_list[val]=rep_list[k]
    
    return test_list

test_list=["gfg","is","best"]
subs_dict={"gfg":[5,6,7],"best":[7,4,5]}
k=0

#print(replace_by_k(test_list,subs_dict,k))

#Alternate
result=[ele if ele not in subs_dict else subs_dict[ele][k] for ele in test_list]
print(result)


#ALternate2 

replace_list=[subs_dict.get(val,val) for val in test_list]

res=[key[k] if isinstance(key,list) else key for key in replace_list]

print(res)




def find_equilibrium(new_list):
    for char in range(len(new_list)):
        if sum(new_list[:char])==sum(new_list[char+1:]):
            print(new_list[char])

new_list=[1,3,5,2,2]
find_equilibrium(new_list)

def find_mean(test_dict):
    sum=0
    for value in test_dict.values():
        sum+=value
    length=len(test_dict)
    avg=sum//length
    return avg

test_dict = {'Gfg' : 4, 'is': 4, 'Best' : 4, 'for' : 4, 'Geeks' : 4}
print(find_mean(test_dict))

def check_if_same(str):
    from collections import Counter
    for char in range(len(str)):
        temp=str[:char]+str[char+1:]
        temp_dict=Counter(temp)
        temp_list=[val for val in temp_dict.values()]
        temp_list=set(temp_list)
        if len(temp_list)==1:
            print("yes")
            break
        else:
            pass
    else:
        print("No")


str = 'xyyzz'
check_if_same(str)

def get_ip():
    import subprocess as sp
    output=sp.getoutput("ifconfig")
    output=output.split("\n")
    idx=""
    for line in output:
        if "wlp2s0"in line:
            idx=output.index(line)
    output=output[17:]
    output="".join(output)
    output=output.split()
    res=[output[word+1] for word in range(len(output)) if output[word]=="inet"]
    print("IP_Address : ",res[0])
get_ip()


def check_intersection(strA,strB):
    from collections import Counter
    global counter_1
    global counter_2
    counter_1=Counter(strA)
    counter_2=Counter(strB)
    for kv in counter_1:
        if kv not in counter_2:
            print("Impossible")
            break
        else:
            pass
    else:
        print("Possible")
        

s1 = 'GeeksforGeeks'
s2 = 'rteksfoGrdsskGeggehes'
check_intersection(s1,s2)

#Alternate

result=counter_1 & counter_2
if counter_1==result:
    print("Possible")


import webbrowser

webbrowser.open("http://facebook.com")


def copy_from_file(filename,operation,new_file):
    try:
        with open(filename,operation) as file_1:
            file_data=file_1.read()

        with open(new_file,"w") as file_2:
            file_2.write(file_data)

    except:
        pass

copy_from_file("/home/sriram/run_code.py","r","copied_file.txt")    

from instabot import Bot

bot=Bot()

bot.login(username="miyaan__33",password="Sriram@8124")



with open("Hello.txt","a") as file:
    file.write("Hello world\n")


def reverse_number(given):
    rev=0
    while given>0:
        rem=given%10
        given=given//10
        rev=(rev*10)+rem
    return rev

given=29876
print(reverse_number(given))




def group_similar(arr):
    count_dict={}
    res_list=[]
    for val in arr:
        count_dict[val]=arr.count(val)

   # result=[[i]*j for i,j in count_dict.items()]
   # print(result)

    for key,val in count_dict.items():
        temp_list=[]
        for count in range(val):
            temp_list.append(key)
        res_list.append(temp_list)

    return res_list    

test_list = [1, 3, 4, 4, 2, 3]    
print(group_similar(test_list))



import multiprocessing
import time
import os

square_list=[0,2]

time_1=time.time()

def calc_squares(arr):
    global square_list
    for val in arr:
        print("square: ",val*val)
        time.sleep(0.3)
        square_list.append(val*val)
    print(square_list)

def calc_cubes(arr):
    for val in arr:
        print("cube: ",val**3)
        time.sleep(0.3)
    print(square_list[0])   #A process don't share its variable to other 

arr=[2,4,6,8,10]
prcs_1=multiprocessing.Process(target=calc_cubes,args=(arr,))
prcs_2=multiprocessing.Process(target=calc_squares,args=(arr,))

prcs_1.start()
prcs_2.start()

prcs_1.join()
prcs_2.join()

print("Process ID for process 1: ",prcs_1.pid)
print("process ID for the main thread : ",os.getpid())
print("Process ID for process 2: ",prcs_2.pid)

time_2=time.time()

print("Time_taken for completion of two processes is ",time_2-time_1)

print(square_list)



import threading
from time import sleep

class Execute_threads:
    def square(self,list):
        for val in list:
            print("square: ",val**2)
            print("I\'m Executing first")
            sleep(0.2)
            print(thread_1.is_alive())    #To know the thread is alive are over
    def cube(self,list):
        for val in list:
            print("cube: ",val**3)
            print("I\'m Executing second")
            sleep(0.2)

math=Execute_threads()
arr=[2,3,8,9]

thread_1=threading.Thread(target=math.square,args=(arr,))
thread_2=threading.Thread(target=math.cube,args=(arr,))

thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()
print(thread_1.is_alive())

#The join is used because if u use it only the threads will execute first other wise the main thread statements also executes in between like the print statement below
print("HI")

import multiprocessing

def function_1(arr):
    for idx,val in enumerate(arr):
        square_list[idx]=val**2
    variable_to_use.value=5.4    

arr=[1,2,3,4,5]

square_list=multiprocessing.Array('i',5)
variable_to_use=multiprocessing.Value('d',1.2)
#Creating two variables independent of the process created like shared memory

prcs_2=multiprocessing.Process(target=function_1,args=(arr,))

prcs_1.start()
prcs_1.join()

print(square_list[:])
print(variable_to_use.value)


def check_duplicate(lis):
    for i in range(len(lis)):
        if lis[i] in lis[:i] or lis[i] in lis[i+1:]:
            print("True")
            break
    else:
        print("False")

nums = [1,1,1,3,3,4,3,2,4,2]
check_duplicate(nums)



import re
s = "aa"
p = "a*"

s = "mississippi"
p = "mis*is*p*."
res=re.findall(p,s)
if res[0]==s:
    print("True")
else:
    print("False")

A=b'GFGD'     #Convert a byte string into corresponding ASCII value
print(list(A))


#Given a Matrix and a range of indices, the task is to write a python program that can sort  matrix on the basis of the sum of only given range

test_list = [[1, 4, 3, 1, 3], [3, 4, 5, 2, 4], [23, 5, 5, 3], [2, 3, 5, 1, 6]]
i, j = 1, 3 

def index_sumsort(lis,i,j):
    dict={}
    for k,l in enumerate(lis):
        s=0
        s=sum(l[i:j])
        dict[s]=k
    sort_ls=sorted(dict)
    sorted_indx=[]
    for index in sort_ls:
        sorted_indx.append(dict[index])
    res=[]
    for x in sorted_indx:
        res.append(lis[x])
    print(res)    

index_sumsort(test_list,i,j)    

#Alternate method 
def get_sum(row):
    return sum(row[1:3])
test_list.sort(key=get_sum)
print(test_list)

#Alternate2
ans=sorted(test_list,key=lambda row:sum(row[1:3]))
print(ans)

#To sort the list using digit in the str
test_list = ["gfg is 4", "all no 1", "geeks over 7 seas", "and 100 planets"] 

temp=[]
for i in test_list:
    temp.append(i.split())
num_list=[]

for word in temp:
    for num in word:
        if num.isdigit():
            num_list.append(int(num))

res=[]
num_list.sort()
for nm in num_list:
    for let in test_list:
        k=let.split()
        if str(nm) in k:
            res.append(let)


print(res)            


dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

dict1.update(dict2)
print(dict1)

original_dict = {'a':1, 'b':2}
item= ('c', 3)

new_dict={}

new_dict[item[0]]=item[1] 

new_dict.update(original_dict)

print(new_dict)


def rearrange_to_larger(array):
    temp_list=[val for char in array for val in str(char)]
    temp_list.sort(reverse=True)
    num="".join(temp_list)
    return int(num)

array=[23,9,674,2,10]
print(rearrange_to_larger(array))

    
    

def find_difference(str_1,str_2):
    uncommon_words=[word for word in str_2.split() if word not in str_1.split()]
    return uncommon_words

A = "Geeks for Geeks" 
B = "Learning from Geeks for Geeks"
print(find_difference(A,B))

res=set(A.split()).symmetric_difference(set(B.split()))    #Alternate 
print(res)


string = "14, 625, 498.002"

string=string.replace(',','*')
string=string.replace('.',',')
string=string.replace('*','.')

print(string)

country_code={'India':10044,
        'Australia':10004,
        'England':91004}
print(country_code['India'])
country_code.setdefault('England',1000006)
country_code.setdefault('south_africa',123456)
print(country_code['south_africa'])
print(country_code.get('England'))

from collections import defaultdict
country_code=defaultdict(lambda:'key not found')
print(country_code['sri_lanka'])   #It wont throw you error because defaultdict is set

new_dict={'name':'sriram',
        "age":21,
        'gender':"male"}
new_dict['address']='chennai'
new_dict.pop('address')
print(new_dict)
print(dict([(1,"age"),(2,"sex")]))

print(dict.fromkeys(new_dict,'oops'))

b=set([9,3,56,3,3432,235,2])
print(sorted(b))

test_dict = {'month' : [1, 2, 3],
             'name' : ['Jan', 'Feb', 'March']}
print(dict(zip(test_dict["month"],test_dict["name"])))

new_tuple=(1,2,)
print(new_tuple)

data = [("Apples", 5, "20"), ("Pears", 1, "5"), ("Oranges", 6, "10")]

print(sorted(data,key=lambda x:x[1]))


print(new_dict.get("address","chennai"))

key=new_dict.keys()

new_dict.update({"mob":1244})
print(key)
val=new_dict.items()
print(val)
print(new_dict)

key_value={2:64,1:69,4:23,5:65,6:34,3:76}
def sort_dict(n):
    for i in sorted(n):
        print((i,n[i]),end="")
    print()
sort_dict(key_value)
print(sorted(key_value,key=lambda x:key_value[x]))
print(sorted(key_value.values()))
print(sorted(key_value.items()))
print(sorted(key_value.items(),key=lambda x:(x[1])))  #To sort using value  

new_list=['a','e','i','o','u']
find_list=['g','e','e','k','s']
print(list(filter(lambda x:x in new_list,find_list)))

l1=[12,31,44,55,66,77]
print(list(filter(lambda x:x%2==0,l1)))



new_list=[2,3,4,5,6,7]
def square(n):
    return n**2
print(list(map(square,new_list))) #Using normal function

print(list(map(lambda x:x**2,new_list)))   #Using lambda fun

print(list(map(lambda x :x+x,new_list)))

list2=[1,2,3,4,5]                                  #To add two lists
print(list(map(lambda x,y:x+y,new_list,list2))) 

str_list=['Hello','World']
print(list(map(list,str_list)))

str_list=['2','3','9']
print(list(map(float,str_list)))

len_list=['Hello','world','python','py','realworldentity']
print(list(map(len,len_list)))                               #To find the length of each word

l1=[2,3,4,6,7]
l2=[2,5,3,6]
#print("\t\tH")
print(list(map(pow,l1,l2)))

print(list(map(lambda x,y:x**y,l1,l2)))   #Finding pow using lambda 

list1=["sri ram","hi","cricketer"]
print(list(map(str.capitalize,list1)))
print(list(map(str.upper,list1)))
print(list(map(str.lower,list1)))

dot_list=['...#..hello','world...']
print(list(map(lambda x:x.strip('.#'),dot_list)))


def various(x):
    return x**x,x+x,x**2
new_l=[2,5,9,8,7]
print(list(map(various,new_l)))

def check(x):
    return x.replace(',','.')
num=['12.3','15,6']
print(list(map(check,num)))

import math
def mixer(x):
    return x>=0
newli=[-81,25,9,-16]          #To find the square root of only positive values
def square_root(y):
    cleaned_square=map(math.sqrt,filter(mixer,newli))
    return list(cleaned_square)
print(square_root(newli))
result=[]


new_dict={'a':100,'b':200,'c':300}
def sumdic(n):
    sum=0
    for i in n:
        sum+=n[i]
    return sum
print("The sum of the values is {}".format(sumdic(new_dict)))


def unpack(a,b,c,d):
    print(a)
    print(b)
    print(c,d)

pack_list=[2,4,6,8]

unpack(*pack_list)

def get_sum(*args):
    return sum(args)

print(get_sum(5,6,8,3))

#dictionary can also be passed

def using_dict(x,y,z):
    return x,y,z

d = {'x':2, 'y':4, 'z':10}
print(using_dict(**d))

def use_kwarg(**kwarg):
    print(type(kwarg))
    
    for key in kwarg:
        print("%s=%s"%(key,kwarg[key]))

use_kwarg(Name=9,Age=21,Place=24)

#Assigning Subsequent Rows to Matrix first row elements

test_list = [[5, 8, 10], [2, 0, 9], [5, 4, 2], [2, 3, 9]]

res_dict={}
temp=test_list[0]
test_list.remove(temp)

for idx in range(len(temp)):
    res_dict[temp[idx]]=test_list[idx]

print(res_dict)    

test_list = [[5, 8, 10], [2, 0, 9], [5, 4, 2], [2, 3, 9]]

new_res=dict(zip(test_list[0],test_list[1:]))
print(new_res)

a="Geeks"
b=b"Geeks"

c=a.encode("ASCII")
d=b.decode("ASCII")

if b==c:
    print("Encode successful")
if a==d:
    print("Decode successful")

x="This is outside function"
def check_fun():
    global x
    x="This is inside a function"
 
def new_fun():
    x="This is newly created variable"
print(x)
check_fun()
new_fun()
print(x)
print(x)


#Once you have declared  a variable global the real global variable won't be considered

def unpack(a,b,c,d):
    print(a)
    print(b)
    print(c,d)

pack_list=[2,4,6,8]

unpack(*pack_list)

def get_sum(*args):
    return sum(args)

print(get_sum(5,6,8,3))

#dictionary can also be passed

def using_dict(x,y,z):
    return x,y,z

d = {'x':2, 'y':4, 'z':10}
print(using_dict(**d))


import re

ip=str(input("Enter the IP: "))

regex="^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

if re.search(regex,ip):
    print("Valid IP")
else:
    print("Invalid IP")

ip=input(str("Enter IP address: "))
def check_validity(ip):
    global ip_list
    ip_list=ip.split(".")
    flag=1
    if len(ip_list)==4:
        for each in ip_list:
            if int(each)>255 or int(each)<0:
                flag=0

    if len(ip_list)!=4 or flag==0:
        print("Invalid IP")
    else:
        class_check(ip)
    
def subnet_mask(classs):
    if classs=="A":
        print("Subnet mask is {}".format("255.0.0.0"))
    elif classs=="B":
        print("Subnet mask is {}".format("255.255.0.0"))
    elif classs=="C":
        print("Subnet mask is {}".format("255.255.255.0"))


def class_check(ip):
    classs=''
    sub=int(ip_list[0])
    if sub>=0 and sub<=127:
        classs="A"
    elif sub>=128 and sub<=191:
        classs="B"
    elif sub>=192 and sub<=223:
        classs="C"
    elif sub>=224 and sub<=239:
        classs="D"
    elif sub>240 and sub<=255:
        classs="E"
    print("Class is {}".format(classs))
    subnet_mask(classs)
  
check_validity(ip)



jack = { "name":"Jack Frost",
         "assignment" : [80, 50, 40, 20],
         "test" : [75, 75],
         "lab" : [78.20, 77.20]
       }
         
james = { "name":"James Potter",
          "assignment" : [82, 56, 44, 30],
          "test" : [80, 80],
          "lab" : [67.90, 78.72]
        }
  
dylan = { "name" : "Dylan Rhodes",
          "assignment" : [77, 82, 23, 39],
          "test" : [78, 77],
          "lab" : [80, 80]
        }
          
jess = { "name" : "Jessica Stone",
         "assignment" : [67, 55, 77, 21],
         "test" : [40, 50],
         "lab" : [69, 44.56]
       }

tom = { "name" : "Tom Hanks",
        "assignment" : [29, 89, 60, 56],
        "test" : [65, 56],
        "lab" : [50, 40.6]
      }
student_list=[jack,james,dylan,jess,tom]

def calculate_avg(name):
    assignment_sum=sum(name['assignment'])/len(name['assignment'])
    test_sum=sum(name['test'])/len(name['test'])
    lab_sum=sum(name['lab'])/len(name['lab'])
    student_avg=(0.1*assignment_sum)+(0.7*test_sum)+(0.2*lab_sum)
    return student_avg
def grade_calculator(name):
    if calculate_avg(name)>=90:
        return f"Grade:A"
    elif calculate_avg(name)>=80:
        return f"Grade:B"
    elif calculate_avg(name)>=70:
        return f"Grade:C"
    elif calculate_avg(name)>=60:
        return f"Grade:D"
    elif calculate_avg(name)>=50:
        return f"Grade:E"
    else:
        return f"Grade:E"

def student_display(name,funcname):
    print("The avgerage mark of {} is {}".format(name,calculate_avg(funcname)))
    print("The grade for {} is {}".format(name,grade_calculator(funcname)))

def class_avg(slist):
    avg_list=[]
    for i in student_list:
        avg_list.append(calculate_avg(i))
        average=sum(avg_list)/len(avg_list)
        return average
student_display("jack",jack)
student_display("james",james)
student_display("dylan",dylan)
student_display("jess",jess)
student_display("tom",tom)

print("\nThe class average is {}".format(class_avg(student_list)))




class student:
    mark1=78
    mark2=99
    def avg_mark(self):
        sum=student.mark1+student.mark2
        avg=sum/2
        return sum,avg
new_obj=student()
print(new_obj.mark2)
print(new_obj.avg_mark())
print(type(new_obj))

giv_list= [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,
                  4, 4, 4, 2, 2, 2, 2]
check_list=list(set(giv_list))
count_list=[]
for i in check_list:
    count_list.append(giv_list.count(i))
new_dict={}    
for i in range(len(check_list)):
    new_dict[check_list[i]]=count_list[i]
print(new_dict)  
                 #Alternate
from collections import Counter
ans=Counter(giv_list)
for k,v in ans.items():
    print("%d : %d"%(k,v))

res_dict={}
for i in giv_list:
    if i in res_dict:
        res_dict[i]+=1
    else:
        res_dict[i]=1
print(res_dict)        



res2_dict={}
for m in giv_list:
    res2_dict[m]=giv_list.count(m)
print(res2_dict)    


from collections import Counter
test_list = [4, 6, 6, 4, 2, 2, 4, 4, 8, 5, 8]
test_dict=Counter(test_list)
res_dict={}
for key in test_dict:
    res_dict[key]=[]                            #To find the frequency of repeated elements
for key,val in test_dict.items():
    for j in range(val):
        res_dict[key].append(val)
print(res_dict)        

res={key:[key]*val for key,val in Counter(test_list).items()} #Alternate
print(res)

dic1={'abc':'hello',
        'bcd':'world'}
dic2={'xyz':'hi',
        'gyh':'boys'}
result={**dic1,**dic2}
print(result)

class parent:
    def __init__(self,name1,name2):
        self.fname=name1
        self.lname=name2
    def display(self):
        print("last name is "+ self.lname)
class student(parent):
    pass
x=student("sri","ram")
x.display()


new_str = "geeksforgeeks"
k=2
temp_str=""
for i in range(len(new_str)):     #To find the kth non repeating value
    if i<len(new_str)-1:
        if new_str[i] not in new_str[i+1:] and new_str[i] not in new_str[:i]:
            temp_str+=new_str[i] 
answer=temp_str[k-1]
print(answer)

class basic():
    def check(self,num):
        if num%2==0:
            print("The number is Even")
        elif num%2!=0:
            print("The number is Odd")
n=basic()
x=int(input("Enter the number: "))
n.check(x)

from more_itertools import distinct_permutations

for p in distinct_permutations('1356'):
    print(''.join(p))

new_dict={"Java":[2,3,5,2,6],"Python":[1,8,12,6,4]}
list_1=[]
rep_list=[]
for val in new_dict.values():
    list_1+=val
for i in range(len(list_1)):
    if list_1[i] in list_1[i+1:] or list_1[i] in list_1[:i]:
        rep_list.append(list_1[i])                             #To remove repeated values
for i in rep_list:
    for j in new_dict.values():
        if i in j:
            j.remove(i)
print(new_dict)            
            

from collections import Counter
giv_str= "Python is great and Java is also great"
giv_str=giv_str.split()
new_dict=Counter(giv_str)
res_list=[]                     # To remove duplicate values using dictionary
for key,val in new_dict.items():
    if val==1:
        res_list.append(key)
print(res_list)        

s = "Python is great and Java is also great"
s=s.split()
r=[]                               #Alternate
for i in s:
    if s.count(i)<=1 and i not in r:
        r.append(i)
print(r)        



test_list = ["Gfg", "is", "Best"]
subs_dict = {
    "Gfg" : [5, 6, 7],
    "is" : [7, 4, 2],
}

k=2                                #Replace the key value with k'th index

for i in range(len(test_list)):
    for j in subs_dict.keys():
        if test_list[i]==j:
            test_list[i]=subs_dict[j][k]
print(test_list)         

test_str = 'geekforgeeks best for geeks'
repl_dict = {'geeks' : 'all CS aspirants'}
test_list=test_str.split()                   #To replace a word in a dictionary
res=[]
for wrd in test_list:
    res.append(repl_dict.get(wrd,wrd))
result=" ".join(res)
print(result)


test_str = 'gfg is best for geeks'
test_dict = {'geeks' : 1, 'best': 6}
for key in test_dict:
    if key in test_str.split():                 #To remove a word
        test_str=test_str.replace(key,"")
print(test_str)           

                                                            
test_str=test_str.split()                               #Alternate
res_list=[i for i in test_str if i not in test_dict]
ans=" ".join(res_list)
print(ans)


class selfcheck:
    def __init__(self,name,age):
        self.myname=name
        self.myage=age
    def checkit():
        print("My name is {} and my age is {}".format(self.myname,self.myage))
new_ob=selfcheck("Sriram",21)
new_ob.checkit()

class selfcheck:
    def __init__(self,name,age):
        self.myname=name
        self.myage=age
    def checkit(self):
        print("My name is {} and my age is {}".format(self.myname,self.myage))
new_ob=selfcheck("Sriram",21)
new_ob.checkit()
new_ob.myage=25     #Changing the variable in init using the object
new_ob.checkit()
    
    

new_str="Geeksforgeeks"
org_str=""
for i in range(len(new_str)):
    if new_str[i] not in new_str[i+1:] and new_str[i] not in new_str[:i]:
        org_str+=new_str[i]              #To return only the repeated values
res_list=[]
for i in new_str:
    if i not in org_str:
        res_list.append(i)
print(set(res_list))        

from collections import Counter
ar1 = [1, 5, 10, 20, 40,20, 80]
ar2 = [6, 7, 20, 80, 100,20]
ar3 = [3,20, 4, 15, 20, 30, 70, 80, 120]  #To find the common elements and their count
ar1=Counter(ar1)
ar2=Counter(ar2)
ar3=Counter(ar3)
result_dict=dict(ar1.items() & ar2.items() & ar3.items())
common=[]
for key,val in result_dict.items():
    for i in range(val):
        common.append(key)
print(common)        
print(result_dict)

def swapcase(str):
    output=''
    for char in str:
        if char.isupper()==True:
            output+=char.lower()
        elif char.islower()==True:
            output+=char.upper()
        else:
            output+=char
    return output
string=input("Enter the string: ")
result=swapcase(string)
print(result)



n1=int(input("Enter the start value: "))
n2=int(input("Enter the end value: "))
time=int(input("Enter time: "))
new_list=[]
for i in range(n1,n2+1):
    new_list.append(i)
rev_list=new_list[::-1]    
ret_value=n2-n1
rem=int(time%ret_value)   #To print the position of time value in the given range
ans=0
q=time//ret_value
if q%2==0:
    for j in range(len(new_list)):
        ans+=new_list[rem]
        break
elif q%2!=0:
    for h in range(len(new_list),-1,-1):
        new_list
        ans+=rev_list[rem]
        break       
print(ans)      


test_dict = {"Gfg" : [5, 7, 5, 4, 5],
             "is" : [6, 7,7], 
             "Best" : [9, 9, 6, 5, 5]}
def find_unique(test_dict):
    max_val=0
    max_key=None
    for key in test_dict.keys():                   #To find the key with max unique values
        if len(set(test_dict[key]))>max_val:
            max_val=len(set(test_dict[key]))
            max_key=key
    print(max_key)        
find_unique(test_dict)

#Alternate
print(sorted(test_dict,key=lambda x:len(set(test_dict[x])),reverse=True)[0])


from collections import Counter
votes = ["john", "johnny", "jackie", 
                    "johnny", "john", "jackie", 
                    "jamie", "jamie", "john",
                    "johnny", "jamie", "johnny", 
                    "john"]
votes=Counter(votes)
max_vote=[]
for i in votes.values():
     max_vote.append(i)        #To print who has maximum number of votes
max_value=max(max_vote)

for key,val in votes.items():
    if val==max_value:
        print(key)

new_dict={}
for k,v in votes.items():
    new_dict[v]=k
maxVote = sorted(new_dict.keys(),reverse=True)[0]
print(maxVote)
   
if len(new_dict[maxVote])>1:
    print (sorted(new_dict[maxVote])[0])
else:
    print (new_dict[maxVote][0])

   


class perform:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def display(self):
        print("The addition of {} & {} is {}".format(self.n1,self.n2,self.add))
    def addition(self):
        self.add=self.n1+self.n2
add=perform(5,9)
add.addition()
add.display()        

class dog():
    def __init__(self,bread,color):
        self.color=color
        self.bread=bread
        print("Object created")
    def new_dog(self,name):
        self.name=name
        print("Name of the dog is "+self.name)
        print("Bread is "+self.bread)
        print("Color is "+self.color)
sweety=dog('lab','brown') 
sweety.new_dog("sweety")
choco=dog('choco','black')
choco.new_dog('choco')



class student:
    name="Sriram"
    age=21
    adress="kovai"
    def new_fun():
        print(student.name)

    def inst(self):
        print("age: "+str(student.age))

obj=student()
obj.address="chennai"
print(obj.age)
print(obj.address)
print(student.__dict__)
print(student.adress)
student.new_fun()          #Class method

obj.inst()                #Instance method

def display(func):
    def runningfun():
        print("Executing")
        func()
    return runningfun()

@display
def newfun():
    print("Go to display")
newfun()    

class temp:
    def __init__(self,user):
        self.use=user
        print("Constructor created")
    def __del__(self):
        print("Constructor deleted")
    
    def new_fun(self):
        print(self.use)
new_ob=temp('sriram')      
new_ob.new_fun()


class check:
    def __init__(self,giname):
        print("Called when obj created")
        self.name=giname
    def usefun(self):
        print("The name is : "+self.name)
obj1=check("sri") 
obj2=check("ram")
obj1.usefun()
obj2.usefun()


class parent:
    def __init__(self,name):
        self.name=name
    def display(self):
        return self.name
    def usename(self):
        return True
class chld(parent):
    def childfun(self):
        print("Using "+username())
obj=parent('sri')
print(obj.name,obj.username())

class new:
    def __init__(self,name,age

try:
    b=5
    print(b)
except Exception as error:
    print(error)
else:
    print("No errors")
finally:
    print("Over")

try:
    a=10
    print(b)
except NameError as error:
    print("10")

try:
    a="pk"
    print(int(a))
except ValueError as error:
    print("string")

try:
    list_1=[2,3,4]
    print(list_1[3])
except IndexError as error:
    print("correct Index")




class Grandfather:
    new_var='Hi'
    def display(self):
        print(new_var)
o=Grandfather()
o.display()




import socket

c=socket.socket()

c.connect(("192.168.0.110",9999))

while True:
    print(c.recv(1024).decode())
    msg=input("Enter message: ")
    c.send(bytes(msg,"utf-8"))

import socket
import threading

c=socket.socket()
c.connect(("192.168.0.110",7777))

def send():
    
    while True:
          v=str(input("Enter: "))
          c.sendall(bytes(v,"utf-8"))
          
          
def recv():

    while True:
          print(c.recv(1024).decode())
   
thread_1 = threading.Thread(target = send)
thread_2 = threading.Thread(target = recv)

thread_1.start()
thread_2.start()
    
    
    

prices=[7,1,5,3,6,4]
profit_list=[]

for day in range(len(prices)):
    for nxt in range(day+1,len(prices)):
        if prices[day]>prices[nxt]:
            pass
        else:
            profit=prices[nxt]-prices[day]
            profit_list.append(profit)

print("Maximum profit of the week is {}".format(max(profit_list)))


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1,n2=0,0
        for i in range(len(num1)):
            n1=(n1*10)+(ord(num1[i])-48)
        for j in range(len(num2)):
            n2=(n2*10)+(ord(num2[j])-48)
        return str(n1*n2)


import time
import threading

def calc_square(arr):
    for n in arr:
        print("Square: ",n**2)
        time.sleep(0.2)

def calc_cube(arr):
    for n in arr:
        print("Cube: ",n**3)
        time.sleep(0.2)
arr=[2,3,4,5]

t=time.time()

t1=threading.Thread(target=calc_square,args=[arr])
t2=threading.Thread(target=calc_cube,args=[arr])


t1.start()
t2.start()

t1.join()
t2.join()

#calc_square(arr)
#calc_cube(arr)

print("Done in :",time.time()-t)

import time
from threading import *
class process1(Thread):
    def run(self):
        for num in range(5):
            print("Hi")
            time.sleep(0.5)

class process2(Thread):
    def run(self):
        for num in range(5):
            print("Hello")
            time.sleep(0.5)
t1=process1()
t2=process2()

t1.start()
t2.start()

t1.join()   #To print "Bye" (main thread) after the child threads gets over join fn is used
t2.join()
print("Bye")

import threading
import time

def fun_1():
    for t in range(5):
        print("Waiting 1 second...")
        time.sleep(1)
        print("Waiting done....")

def fun_2():
    for t in range(5):
        print("Waiting 2 second...")
        time.sleep(1)
        print("Waiting done....")

t=time.time()

t1=threading.Thread(target=fun_1)
t2=threading.Thread(target=fun_2)

t1.start()
t2.start()

t1.join()
t2.join()

print("Done in :",round(time.time()-t),"seconds")


print('ll")l


def outer():
    x=10
    def inner():
        y=12
        result=x+y  #Calling a function with a variable
        return result
    return inner
a = outer()
print(a())


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
    # print(rev_number)
    num//=10
print(rev_number)

A_list=[2,5,6,7,9]
for i in range(len(A_list)):
    print(all(A_list[i] <=A_list[i+1]) or (A_list[i] >= A_list[i+1]))
counter=0    
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
print(math.prod(mul_list))

new1_list=[1,2,-4,5,-7,9,-4,6,-20]
num=0
while num<len(new1_list):
    if num%2==0:
        print(new1_list[num])
    num+=1

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


n=1234
txt=""
while n>0:
    rem=n%10
    n=n//10
    txt+=str(rem)
print(txt)    





# new_list=list(range(1,11))
# d=3 #rotation number
# i=0
# temp_list=[]
# while i<d:
#     temp_list.append(new_list[i])
#     i+=1
# i=0
# while d<len(new_list):
#     new_list[i]=new_list[d]
#     d+=1
#     i+=1
# new_list[:]=new_list[:i]+temp_list
# print("The list after rotation is ",new_list)

def rotate_list(lis,n):
    r=n
    temp_list=lis[:r]
    res=lis[r:]+temp_list
    return res

lis=[2,3,4,6,1,7,9,-2,3]
n=3
print(rotate_list(lis,n))    




samp_str="ABCDEFGHIJKLIMNOQRSTUVWXYZ"
length=len(samp_str)
t=4
for i in range(0,length,t):
    print(samp_str[i:i+t])
num=2653
res=''
for i in str(num):
    res=i+res
print(res)    
A="MananVohra is"
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
res=Counter(new_str)      
print(res)          #Alternate method
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













def fun(arg):
    print("Hello",arg)

import mymodule
mymodule.fun("sri")


Nums = [3,2,4,7,8,3,5,6,1]
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
        temp_list.append(j)      #To get sorted unique values from dictionary
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
print(lis)
print(sorted(lis,key=lambda x:x["age"]))
print(sorted(lis,key=lambda x:(x["name"],x["age"])))
print(sorted(lis,key=lambda x: x["name"],reverse=True))

b="The wait is over"
print(b.split())
A=["the", "wait","is","over"]
print(" ".join(A))


new_list1=[2,34,56,1,34,6,2]
new_list1.sort(reverse=True)
print(new_list1)






print(sorted(lis,key=lambda x:x['age'],reverse=True))

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


def usage_yield(val):
    while val>0:
        if val%2==0:
            yield val
        val-=1
 
val=10 
for even in usage_yield(val):
    print(even)

def check_subseq(txt,sub):
    for char in sub:
        if char not in txt:
            print(False)
            break
    else:
        print(True)

s = "axc"
t = "ahbgdc"
check_subseq(t,s)

def check_iter(list):
    iter_val=iter(list)
    
    while True:
        try:
            values=next(iter_val)
            print(values)

        except StopIteration: 
            break
    
nl=[1,2,3,4,6]
check_iter(nl)


def replace_by_X(txt,sub):
    res_str=""
    for char in range(len(txt)-2):
        if txt[char:char+2]==sub:
            idx=char+1

        elif char==idx and txt[idx+1:idx+3]!=sub:
            res_str+="X"
        else:
            res_str+=txt[char]

    temp_str=""
    for i in res_str:
        if i!='b':
             temp_str+=i
    return temp_str
                



txt="abababcdefababcdab"
sub="ab"

print(replace_by_X(txt,sub))



Input=[11, 5, 17, 18, 23, 50,60,70]

a=1
b=5

res=Input[:a]+Input[b+1:]

print(res)


def remove(Inp):
    res=filter(None,Inp)
    return res

Input= [(), ('ram','15','8'), (), ('laxman', 'sita'), 
                  ('krishna', 'akbar', '45'), ('',''),()]
print(remove(Input))

    

def remove_dup_differently(list):
    res_list=[]
    for char in list:
        count_val=list.count(char)
        if count_val>1:
            if res_list.count(char)==0:
                res_list.append(char)

    return res_list            


list = [1,2,1,2,3,4,5,1,1,2,5,6,7,8,9,9] 
print(remove_dup_differently(list))
from collections import Counter
def group_similar(list):
    new_dict=Counter(list)
    for key,val in new_dict.items():
        new_dict[key]=[key for time in range(val)]

    return new_dict

test_list = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8]
print(group_similar(test_list))        



for row in range(7):
    for col in range(5):
        if row==0 or row==6 or col==0:
            print("*",end="")
        else:
            print(end=" ")
    print()

#For printing B

def print_letter_B():
    for row in range(7):
        for col in range(5):
            if (col==0 or col==4) or ((row==0 or row==3 or row==6) and (col>0 and col<4)): 
                print("*",end="")
            else:
                print(end=" ")
        print()
print_letter_B()                                
txt='ABC'
res=[]
for i in txt:
    for j in txt:
        for k in txt:
            if i!=j and j!=k and i!=k:
                res.append(i+j+k)

print(res)


from itertools import permutations
ans=[]
res=permutations(txt)
for i in res:
    ans.append("".join(i))

print(ans)


ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

from collections import Counter

arr1=Counter(ar1)
arr2=Counter(ar2)
arr3=Counter(ar3)

res=dict(arr1 & arr2 & arr3)

print(res)
def print_D():
    for row in range(7):
        for col in range(5):
            if col==0 or row==0 and col>0 and col<4 or col==4 and row>0 and row<6 or row==6 and col>0 and col<4:
                print("*",end="")
            else:
                print(end=" ")
        print()
print_D()                    

def print_E():
    for row in range(7):
        for col in range(5):
            if (col==0) or (row==0 and col!=0) or (row==3 and col!=0) or (row==6 and col!=0):
                print("*",end="")
            else:
                print(end=" ")
        print("")
print_E()               

def print_F():
    for row in range(7):
        for col in range(5):
            if (col==0) or (row==0 and col!=0) or (row==3 and col!=0):
                print("*",end=" ")
            else:
                print(end=" ")
        print()
print_F()        

def print_G():
    for row in range(7):
        for col in range(7):
            if (col==0) or (row==0 and col>0 and col<5) or (row==6 and col>0 and col<5) or (row==3 and col>2) or (col==4 and row>3 and row<6) or (col==6 and row>3):
                print("*",end="")
            else:
                print(end=" ")
        print()
print_G()        


import multiprocessing
import time

def cash_deposit(balance):
    for add in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value+=1
        lock.release()

def cash_withdrawal(balance):
    for sub in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value-=1
        lock.release()

balance=multiprocessing.Value('i',200)
lock=multiprocessing.Lock()

prcs_1=multiprocessing.Process(target=cash_deposit,args=(balance,))
prcs_2=multiprocessing.Process(target=cash_withdrawal,args=(balance,))

prcs_1.start()
prcs_2.start()

prcs_1.join()
prcs_2.join()

print(balance.value)

                                       

import multiprocessing

def calculate_squares(arr):
    for val in arr:
        queue.put(val**2)

def interfere(arr):
    for each in arr:
        queue.put(each**3)

arr=[2,4,6,8,10]

prcs=multiprocessing.Process(target=calculate_squares,args=(arr,))
prcs2=multiprocessing.Process(target=interfere,args=(arr,))

queue=multiprocessing.Queue()

prcs.start()
prcs.join()

prcs2.start()
prcs2.join()

while queue.empty() is False:
    print(queue.get())


def add_substrings(str,val):
    sub_list=[]
    for i in range(len(str)):
        for j in range(i,len(str)+1):
            if str[i:j]!="":
                sub_list.append(str[i:j])
    larger_list=[]
    for sub in sub_list:
        if int(sub) > int(val)
            larger_list.append(int(sub))
    return sum(larger_list)

str="122223"
val="97"
print(add_substrings(str,val))


# File: avg_mark.py

#Get the names from the user and enter their marks and display in a dictionary
user_data = {}

students_count = int(input("How many names do you want to enter: "))
count = 0
base_student_name = 'student'

for student in range(students_count):
    mark = int(input('Enter your mark: '))
    student_name = base_student_name+str(count)
    user_data[student_name] = mark
    count+=1

print(user_data)    


# for i in range(j):
#     name=input("Enter name: ")
#     marks=[]
#     for h in range(k):
#         mark=input("Enter the marks")
#         marks.append(mark)
#     giv_dict[name]=marks
# print(giv_dict)    
for i in range(j):
    giv_dict[input("Enter name")]=[input("enter marks") for f in range(k)]
print(giv_dict)   
# names=str(input("Enter the name you want to know the average: "))
# n=giv_dict[str(names)]
# sum=0
# for i in n:
#     sum+=int(i)
# avg=sum/len(n)
# print(f"Average is {avg}")

'''a = "this is a string"
a = a.split(" ") # a is converted to a list of strings. 
print(a)'''

'''dic={}
n=int(input("enter something : "))
n2=[input(n) for n in range(3)]
dic[n]=n2
print(dic)'''

def some_box_problem():
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




def get_only_integers():
    ps = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

    all_list=[j for i in ps for j in i]
    num_list=[]
    for k in all_list:
        if isinstance(k,int) or isinstance(k,float):
            num_list.append(k)

    print(num_list) 

# File: insert.py

giv_list=[1,3,5,6,8,"oo ",0,2]
target=7
# max_val=max(giv_list)
# if target>max_val:
#     giv_list.append(target)
# for i in giv_list:
#      if target==i:
#         print(giv_list.index(target))
# else:
#      giv_list.append(target)
#      giv_list.sort()
#      print(giv_list.index(target))  

print(giv_list.index("oo "))     
             

# File: loop.py

list=["Karthick","dinesh","ajay","madhan"]
i=0
while i<len(list):
   print(list[i])
   i+=1
A=(2,3,4,5,5,9)
generator=[x**2 for x in A]
print(type(generator))

# File: match_index.py

test_list = ["geekforgeeks", [5, 4, 3, 4], "is", 
             ["best", "good", "better", "average"]]

idx=0
res=[]
k=4
while idx<k:
    temp=[]
    for iter in test_list:
        if not isinstance(iter,list):
            temp.append(iter)
        else:
            temp.append(iter[idx])
    res.append(temp)
    idx+=1

print(res)

new_tup=(1,2,3)
if 5 in new_tup:
    print("s")

# File: oddeven.py

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

# File: prefix.py

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

# File: stringcheck.py

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

# File: studentmark.py

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

# File: transpose_of_matrix.py

# Program to transpose a matrix using a nested loop

X = [[12,7],
    [4 ,5],
    [3 ,8]]

res=[[0 for col in range(3)] for row in range(2)]   


for row in range(len(X)):
    for col in range(len(X[0])):
        res[col][row]=X[row][col]

print(res)

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

class Check:
    var1=3
    def usevar(self):
        print(Check.var1)

obj=Check()
obj.usevar()    

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

from itertools import permutations
A=[1,2,3]
print(list(permutations([1,2,3])))

class FindMedian:
    common_array = []
    def addNumber(self,num):
        FindMedian.common_array.append(num)

    def findMedian(self):
        if len(FindMedian.common_array)%2==0:
            return FindMedian.common_array[len(FindMedian.common_array)//2]

commands = ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
help = [[], [1], [2], [], [3], []] 

giv_list=[1,2,3,4,5,6,8,9]
target =6
for i in range(len(giv_list)):
    if giv_list[i]==target:
        print(i)                   #To find the target number's index or to find where it is inserted

else:
    for i in range(len(giv_list)):
        if (giv_list[i] < target) and  (giv_list[i+1] > target):
            print(i+1)

test_list1 = [[4, 3, 5, ], [1, 2, 3], [3, 7, 4]]
test_list2 = [[1, 3], [9, 3, 5, 7], [8]]
res_list=[]
for i in range(len(test_list1)):
    res_list.append(test_list1[i]+test_list2[i])
print(res_list)    

d={}
lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
for i in lst:
    d[i]=lst.count(i)
print(d) 
from collections import Counter
print(Counter(lst))

from functools import reduce
list1 = [1, 2, 8,10]
list2 = [3, 2, 4]
ans=reduce(lambda x,y:x+y,list1)
print(ans)

tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'), 
                  ('krishna', 'akbar', '45'), ('',''),()]
for i in tuples:
    if i==():
        tuples.remove(i)
print(tuples) 

new_tup=[tup for tup in tuples if tup]
print(new_tup)

shop={6:45,7:48,8:50,9:60,10:65,11:70}
stocks={6:2,7:3,8:1,9:4,10:2,11:1}
total=0
while True:
    n=int(input("Enter 1 to buy shoe.0 to exit: "))
    if n==0:
        break
    else:
        print("The shoe sizes and price in dollars\n")
        for i in shop.items():
            print(i)
        print("Number of stocks")
        print(stocks)
        size=int(input("Enter the size: "))
        num=int(input("Enter the number of shoes: "))
        stocks[size]-=num
        total+=shop[size]*num
print("Total = ",total)        

test_list = [[1, 4, 3, 1, 3], [3, 4, 5, 2, 4],
             [23, 5, 5, 3], [2, 3, 5, 1, 6]]
x,y = 1, 3 
new_dict={}
for i in test_list:                          #To sort the list using sum of index of range values
    new_dict[sum(i[x:y])]=i
res_list=[]
for i in sorted(new_dict.keys()):
     res_list.append(new_dict[i])
print(res_list)     

res=sorted(test_list,key=lambda k:sum(k[x:y]))
print(res)                                         #Alternate

nl=[12,67,98,34]
sum_list=[]
for i in nl:
    sum=0
    for j in str(i):
        sum+=int(j)
    sum_list.append(sum)
print(sum_list)    

text="Hacker Rank"
res=""
for i in text:
    if i.isupper():
        res+=i.lower()
    elif i.islower():
        res+=i.upper()
    elif i==" ":
        res+=" "
print(res)        

txt="HackerRank"
print(txt.ljust(20,'-'))
print(txt.rjust(20,'-'))
print(txt.center(60,'*'))

mat=[[0 for j in range(2)]for i in range(2)]
txt="ABCD"
for i in range(2):
    for j in range(2):
        for k in txt:
            mat[i][j]=k
print(mat)            

new_str='welcome2ourcountry34'
i=0
flag=None
while i<len(new_str):
    if new_str[i].isalpha():
        flag=1
    elif  new_str[i].isdigit() and flag==1:
        print("Yes")
        break
    i+=1


new_str='welcome to geeks for geeks'
nl=new_str.split()
res_list=[]
for i in nl:
    res_str=''
    for j in range(len(i)):
        if j!=0 and j!=len(i)-1:
            res_str+=i[j]
        else:
            res_str+=i[j].upper()
    res_list.append(res_str)

res=' '.join(res_list)
print(res)

new_str='geeksforgeeks'
length=len(new_str)
half=len(new_str)//2
res=''
for i in range(len(new_str)):
    if i in range(half,length):
        res+=new_str[i].upper()
    else:
        res+=new_str[i]
print(res)        

import re
nums=[0,1,2,2,3,0,4,2]
val=2
temp_list=['_' for i in range(len(nums))]
for i in range(len(nums)):
    if nums[i]!=val:
        temp_list[i]=nums[i]
res_list=[]
for i in temp_list:
    if str(i).isdigit():
        res_list.append(i)
for val in range(len(nums)-len(res_list)):
    res_list.append('_')
print(res_list)    

print(__name__)

new_list=['Gfg', 3, 'is', 8, 'Best', 10, 'for', 18, 'Geeks', 33]
res_list=[]
for i in range(len(new_list)):
    if i%2==0:
        new_dict={}
        new_dict['name']=new_list[i]
        new_dict['number']=new_list[i+1]
        res_list.append(new_dict)
print(res_list)    

key=['name','number']
res_list2=[{key[0]:new_list[k],key[1]:new_list[k+1]} for k in range(0,len(new_list),2)] #Alternate
print(res_list2)

new_list=[[4, 5, 6], [2, 4, 5], [6, 7, 5]]
res=[]
for i in new_list:
    res.append([[j,i[-1]]for j in i[:-1]])
print(res)    

new_list=[['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]
new_dict={}
for i in new_list:
    key=[i[k] for k in range(len(i)//2)]
    val=[i[v] for v in range(len(i)//2,len(i))]
    new_dict[tuple(key)]=tuple(val)
print(new_dict)    

res={tuple(sub[:2]):tuple(sub[2:]) for sub in new_list}   #Alternate
print(res)

new_list=[[4, 5, 5], [2, 7, 4], [8, 6, 3]]
temp_list=[j for i in new_list for j in i]
import random
res=random.choice(temp_list)
print(res)

new_list=[2,4,[],9,6,[],1,4,[]]
res=list(filter(None,new_list))
print(res)


for i in new_list:
    if i==[]:
        new_list.remove(i)
print(new_list)

new_list=[[4, 1, 6], [7, 8], [4, 10, 8]]
rev_list=[sorted(i,reverse=True) for i in new_list]
print(rev_list)


country_code={'India':10044,
        'Australia':10004,
        'England':91004}
print(country_code['India'])
country_code.setdefault('England',1000006)
country_code.setdefault('south_africa',123456)
print(country_code['south_africa'])
print(country_code.get('England'))

from collections import defaultdict
country_code=defaultdict(lambda:'key not found')
print(country_code['sri_lanka'])   #It wont throw you error because defaultdict is set

new_dict={'name':'sriram',
        "age":21,
        'gender':"male"}
new_dict['address']='chennai'
new_dict.pop('address')
print(new_dict)
print(dict([(1,"age"),(2,"sex")]))

print(dict.fromkeys(new_dict,'oops'))

b=set([9,3,56,3,3432,235,2])
print(sorted(b))

test_dict = {'month' : [1, 2, 3],
             'name' : ['Jan', 'Feb', 'March']}
print(dict(zip(test_dict["month"],test_dict["name"])))

new_tuple=(1,2,)
print(new_tuple)

data = [("Apples", 5, "20"), ("Pears", 1, "5"), ("Oranges", 6, "10")]

print(sorted(data,key=lambda x:x[1]))


print(new_dict.get("address","chennai"))

key=new_dict.keys()

new_dict.update({"mob":1244})
print(key)
val=new_dict.items()
print(val)
print(new_dict)






















       
def find_diff_avgs(arr):
    pos_count=0
    neg_count=0
    zero_count=0
    res_arr=[]
    for char in arr:
        if char<0:
            neg_count+=1
        elif char>0:
            pos_count+=1
        elif char==0:
            zero_count+=1
    length=len(arr)        
    pos_avg=pos_count/length
    neg_avg=neg_count/length
    zero_avg=zero_count/length
    print("%.6f %.6f %.6f"%(pos_avg,neg_avg,zero_avg))


arr=[-4,3,-9,0,4,1]
find_diff_avgs(arr)

import subprocess as sp
import re

result=sp.getoutput("iwlist scanning")
essid=re.findall("ESSID.*",result)
bit_rate=re.findall("Bit Rates.*\n.*Mb\/s",result)
print(essid)
for i in range(len(bit_rate)):
    bit_rate[i]=bit_rate[i].replace(" ","")
print(bit_rate)

string = "apple,banana,grapes orange,pine-apple,apple,orange=peach,grapes+guava,papaya@banana"

import re
from collections import Counter

string_list=re.split(",| |-|=|\+|@",string)

new_dict=Counter(string_list)

for key,val in new_dict.items():
    temp_list=[]
    inc=0
    for count in range(val):
        idx=string.find(key,inc,len(string))
        print(idx)
        temp_list.append(idx)
        inc=idx+1
    new_dict[key]=temp_list

print(new_dict)    

def sort_independently(arr):
    odd_list=[]
    even_list=[]
    for idx in range(len(arr)):
        if idx%2==0:
            even_list.append(arr[idx])
        else:
            odd_list.append(arr[idx])
    odd_list.sort(reverse=True)
    even_list.sort()
    result=[]
    for char in range(len(odd_list)):
        result.append(even_list[char])
        result.append(odd_list[char])
    return result 

arr=[4,1,2,3]
print(sort_independently(arr))

import sys
import os

print(sys.version)
print(sys.argv)

print(os.chroot)
def convert_decimal(bit):
    pow=0
    sum=0
    while bit>0:
        rem=bit%10
        sum+=rem * 2**pow
        bit=bit//10
        pow+=1

    return sum

bit=11101101
print(convert_decimal(bit))        
import sys

print(sys.version)

set_1={1,2,3,4,5,6,8,9}
set_2={12,4,3,2,7,5,10}

res=set_1.union(set_2)
print(res)

import sys

print(sys.version)
import re

regex=re.compile("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9\-\.]+)\.([a-zA-Z]{2,5})$")

string="srirampanneer90@gmail.com"

print(regex.search(string))

help("modules")

import paramiko

import time

host="192.168.0.114"
username="muthu"
password="muthu"
port=22

session=paramiko.SSHClient()

session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

session.connect(hostname=host,
        username=username,
        port=port,
        password=password)

stdin,stdout,stderr=session.exec_command("ls")
#time.sleep(0.5)

print(stdout.read().decode())


import paramiko

import time

host="192.168.0.112"
port=22
username="nisha"
password="123"

command="ls"

ssh=paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(host, port, username, password)

stdin, stdout, stderr = ssh.exec_command(command)

lines = stdout.read().decode()

error = stderr.read().decode().strip()
print(lines)
time.sleep(0.5)

ssh.close()


from getpass import getpass

password=getpass("Enter the password: ")

new=input() or "enter panuda"
print(type(password))

print(new)

                                  #compile using regex
import re

regex=re.compile(r"[^a-zA-Z0-9]")

string="#$%$^#^(*"

print(len(string))
print(len(regex.findall(string)))

import subprocess as sp
import re

res=sp.getoutput("ifconfig")

res_list=re.match("([a-z0-9]{2}:){5}[a-z0-9]{2}",res)
            #         ([a-z0-9]{2}:){5}[a-z0-9]{2}

print(res_list)

import subprocess as sp
import re


def get_ip(cmd):
    result=sp.getoutput(cmd)
    if_list=re.search("\b\d:",result)
    print(if_list)
    
    
command="ip add"
#get_ip(command)

import paramiko
from time import sleep

host="192.168.0.114"
port=22
password="muthu"
user="muthu"

session=paramiko.SSHClient()

session.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #This will add the host keys in the knownhost list

#session.load_system_host_keys() #This line is used when the remote host is already added in the known host list

#To check the key generated for the remote_host  is $ssh-keygen -F <ip_addr>

#To see the known host list $nano ~/.ssh/knownhosts

session.connect(hostname=host,
        port=port,
        username=user,
        password=password)

#stdin,stdout,stderr=session.exec_command("ls")
#sleep(0.5)
#print(stdout.read().decode("utf-8"))
commands=['mkdir race','cd race ; touch file.txt']
for cmd in commands:
    stdin,stdout,stderr=session.exec_command(cmd)
    sleep(0.5)
    print(stdout.read().decode())

session.close()


row=7
col=5

for row in range(row):
    for col in range(col):
        if col==0 or col==4 or col>0 and row==3 and col<4:
            print("*",end="")
        else:
            print(" ",end="")
    print()            
# Python 3 program to demonstrate subprocess
# module

import subprocess
import os

def excuteC():

	# store the return code of the c program(return 0)
	# and display the output
	s = subprocess.check_call("gcc HelloWorld.c -o out1;./out1", shell = True)
	print(", return code", s)

def executeCpp():

	# create a pipe to a child process
	data, temp = os.pipe()

	# write to STDIN as a byte object(convert string
	# to bytes with encoding utf8)
	os.write(temp, bytes("5 10\n", "utf-8"));
	os.close(temp)

	# store output of the program as a byte string in s
	s = subprocess.check_output("g++ HelloWorld.cpp -o out2;./out2", stdin = data, shell = True)

	# decode s to a normal string
	print(s.decode("utf-8"))

def executeJava():

	# store the output of
	# the java program
	s = subprocess.check_output("javac HelloWorld.java;java HelloWorld", shell = True)
	print(s.decode("utf-8"))


# Driver function
if __name__=="__main__":
	excuteC()	
	executeCpp()
	executeJava()


new_str="12a"
asc_0=48
res=0

for char in new_str:
    try:
        int_val=int(char)
    except:
        res=-1
        break
    int_val=ord(char)-asc_0
    res=(res*10) + int_val

print(res)    

nl=[]

nl.append(2,4)
str = "GEEGEEKSSGEK"
sub_str = "GEEKS"

str = "GEEGEEKSKS"
sub_str = "GEEKS"
length=len(sub_str)

if sub_str in str:
    idx=str.find(sub_str)

end=idx+(length-1)

res=str[:idx]+str[end+1:]

if res==sub_str:
    print("Yes")
else:
    print("No")


S = "i.like.this.program.very.much"

nl=[11,2,23]

nl.
def get_args(*tup):
    new_list=[]
    for i in tup:
        new_list.append(i)
    return new_list

print(get_args(1,2,3,5,8))


def use(fun_list):
    global res_list
    res_list=[]
    if fun_list[0]=='insert':
        idx=int(fun_list[1])
        res_list[idx]=fun_list[2]

    if fun_list[0]=='append':
        res_list.append[fun_list[1]]
    
for i in range(3):
    user=input("Input: ")
    lis=user.split()
    print(lis)
    use(lis)            

#print(res_list)    

import logging

logging.basicConfig(filename='test_file.log',level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

x=15
y=5

add_result=add(x,y)
sub_result=sub(x,y)
mul_result=mul(x,y)
div_result=div(x,y)

logging.debug("Result for addition of {} and {} is {}".format(x,y,add_result))
logging.debug("Result for subtraction of {} and {} is {}".format(x,y,sub_result))
logging.debug("Result for multiplication of {} and {} is {}".format(x,y,mul_result))
logging.debug("Result for division of {} and {} is {}".format(x,y,div_result))

class Employee():

    def __init__(self,first,last):
        self.fname=first
        self.lname=last

        logging.info("Created Employee:{}-{}".format(self.name,self.email))

    @property
    def name(self):
        return '{} {}'.format(self.fname,self.lname)

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.fname,self.lname)


emp1=Employee('Hanish','Kumar')
emp2=Employee('Veera','mani')


def reverse_a_number(num):
    ans=0
    while num>0:
        rem=num%10
        ans*=10
        ans+=rem
        num=num//10

    return ans


n=1750
print(reverse_a_number(n))

class Employee():

    def __init__(self,first,last):
        self.fname=first
        self.lname=last
        
        print("Created Employee:{}-{}".format(self.name,self.email))
        print("Line executed")

    @property
    def name(self):
        return '{} {}'.format(self.fname,self.lname)

    @property    
    def email(self):
        return '{}.{}@gmail.com'.format(self.fname,self.lname)
             

emp1=Employee('Hanish','Kumar')
emp2=Employee('Veera','Baagu')

import logging

logging.basicConfig(filename='test_file.log',level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s',filemode='a')

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

x=15
y=5

add_result=add(x,y)
sub_result=sub(x,y)
mul_result=mul(x,y)
div_result=div(x,y)

logging.debug("Result for addition of {} and {} is {}".format(x,y,add_result))
logging.debug("Result for subtraction of {} and {} is {}".format(x,y,sub_result))
logging.debug("Result for multiplication of {} and {} is {}".format(x,y,mul_result))
logging.debug("Result for division of {} and {} is {}".format(x,y,div_result))

class Employee():

    def __init__(self,first,last):
        self.fname=first
        self.lname=last

        logging.info("Created Employee:{}-{}".format(self.name,self.email))

    @property
    def name(self):
        return '{} {}'.format(self.fname,self.lname)

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.fname,self.lname)


emp1=Employee('Hanish','Kumar')
emp2=Employee('Veera','mani')
logging.info("Just printing {} and {}".format(x,y))

class Employee():

    def __init__(self,first,last):
        self.fname=first
        self.lname=last
        
        print("Created Employee:{}-{}".format(self.name,self.email))
        print("Line executed")

    @property
    def name(self):
        return '{} {}'.format(self.fname,self.lname)

    @property    
    def email(self):
        return '{}.{}@gmail.com'.format(self.fname,self.lname)
             

emp1=Employee('Hanish','Kumar')
emp2=Employee('Veera','Baagu')

def remove_last_line(filename):
    with open(filename,"r") as old_file:
        txt=old_file.read()
        new_list=txt.split("\n")
        new_list.pop(len(new_list)-2)
        new_list.pop()
          
        try:  
            with open("New_file.txt","a") as new_file:
                for each_line in new_list:
                    new_file.write(each_line)
                    new_file.write("\n")
        except Exception as error:
            print(error)

filename="test_file.log"
remove_last_line(filename)

key_value ={}   
  
# Initializing the value
key_value[2] = 56      
key_value[1] = 2
key_value[5] = 12
key_value[4] = 24
key_value[6] = 18     
key_value[3] = 323

res=sorted(key_value.items(),key=lambda kv:kv[1])

print(res)


print(key_value.get(9,"aa"))

row=int(input("Enter the number of rows: "))
k=1

for i in range(row):
    for j in range(1,k+1):
        print("*",end="")
    k+=2
    print()    
n=4

for i in range(1,n+1):
    for j in range(0,n-i):
        print(" ",end="")
    for k in range(i):
        print("*",end=" ")
    print()        

for i in range(n-1,0,-1):
    for j in range(0,n-i):
        print(" ",end="")
    for k in range(i):
        print("*",end=" ")
    print()               
def find_missing(nums):
    length=len(nums)
    missing_list=[]
    for val in range(length+1):
        if val not in nums:
            missing_list.append(val)
    if len(missing_list)==1:
        return missing_list[0]        


nums = [9,6,4,2,3,5,7,0,1]
print(find_missing(nums))

n=int(input('Enter the number of rows: '))

for row in range(n):
    for space in range(n-row-1):
        print(" ",end="")
    for star in range(row):
        print("+",end=" ")
    print()    

for row in range(n,0,-1):
    for space in range(n-row):
        print(" ",end="")
    for star in range(row):
        print("* ",end="")
    print()    

#An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

def ugly_number(num):

    prime_list=[]

    for val in range(2,num+1):
        for factors in range(2,val):
            if val % factors == 0:
                break
        else:
            prime_list.append(val)

    for each_num in prime_list:
        if each_num==2 or each_num==3 or each_num==5:
            pass 
        else:
            print(False)
            break
    else:
        print(True)


num=6
ugly_number(num)

lis = [{ "name" : "Nandini", "age" : 39},
{ "name" : "Manjeet", "age" : 20 },
{ "name" : "Nikhil" , "age" : 19 }]

res=sorted(lis,key=lambda x:x["age"])

print(res)

'''country_code = {'India' : '0091',
                'Australia' : '0025',
                'Nepal' : '00977'}
country_code.setdefault('Bopal',123)country_code = {'India' : '0091',
                'Australia' : '0025',
                'Nepal' : '00977'}
print(country_code['Bopal'])'''

nl=[2,3,4]
print(prod(nl))

from tkinter import *

window=Tk()
window.title("Sriram Tkinter program")
label=Label(window,text="World of cricket")
label.pack()
window.mainloop()

def find_word():
    word="ORANGE"
    print("HINT ...... The word you are finding is a fruit")
    find=['_','_','_','_','_']
    for char in find:
        print(char,end=" ")
    print("You have only 10 chances")
    chance=0
    while chance<=10:
        user_input=input("\nEnter a letter to guess: ")
        if user_input.lower() in word or user_input.upper() in word:
            idx=word.find(user_input.upper())
            find[idx]=user_input.upper()
        print()    
        for char in find:
            print(char,end=" ")
        print()    
        chance+=1 
        user_word="".join(find)
        if user_word==word:
            print("\nYou have won with {} tries".format(chance))
            break
    else:
        print("\nYou have exceeded the maximum chances")   
        print(f"\nThe correct answer is {word}")    
find_word()
            

import random

def first():
    return "Add"

def second():
    return "sub"
    
def third():
    return "mul"

new_list=[first,second,third]

for i in range(3):
    print(random.choice(new_list)())
new_set=set()  #will create a empty set

sample_list=[28,12,13,1,2,12,33,2,0,28,2,1]

for char in sample_list:
    if char not in new_set:
        new_set.add(char)

print(new_set)

data = [("Apples", 5, "20"), ("Pears", 1, "5"), ("Oranges", 6, "10")]

data.sort(key=lambda x:x[0])

print(data)

new_list=[4,2,2,1,7,5,9]

new_list.sort(reverse=True)
new_str="Helloworld"

res=new_list.index(2)

print(res)

sort_list_last=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

sort_list_last.sort(key=lambda x:x[1])
print(sort_list_last)

new_list=[1,2,3,4,56,7]
print(list(enumerate(new_list,-1)))


list1=[2,3,7]
list1.reverse()
print(list1)















#!/bin/bash

import random

def one():
    print("______________________")
    print("\n")
    print("\t*",end="\t")
    print("\n")
    print("______________________")
#one()
    
def two():
    print()
    print("______________________")
    print("\n")
    for row in range(3):
        for col in range(3):
            if row==col and row!=1:
                print("*",end=" ")
            else:
                print("   ",end="  ")
        print("\n")
    print("______________________")
    
#two()

def three():
    print()
    print("______________________")
    print("\n")
    for row in range(3):
        for col in range(3):
            if row==col:
                print("*",end="\t")
            else:
                print(" ",end="\t")
        print("\n")
    print("______________________")
    
#three()

def four():
    print()
    print("______________________")
    print("\n")
    for row in range(2):
        for col in range(2):
            print("*",end="\t\t")
        if row!=1:
            print("\n\n\n")
        else:
            print("\n")
    print("______________________")
      
#four()

def five():
    print()
    print("______________________")
    print("\n")
    for row in range(3):
        for col in range(3):
            if row%2==0 and col%2==0 or row==col:
                print("*",end="\t")
            else:
                print(" ",end="\t")
        print("\n")
    print("______________________")
    
#five()        

def six():
    print()
    print("______________________")
    print("\n")
    for row in range(3):
        for col in range(3):
            print("*",end="\t")
        print("\n")
    print("______________________")
    
#six()

choice_list=[one,two,three,four,five,six]

user_input=int(input("Enter how many times do you want to roll the dice: "))

for times in range(user_input):
    random.choice(choice_list)()


'''If n is even, replace n with n / 2.
If n is odd, replace n with either n + 1 or n - 1.'''



def replace_int(num):
    count=0

    while num!=1:
        if num%2==0:
            num=num//2
        elif num%2!=0:
            num=num+1
        count+=1

    return count

print(replace_int(7))

def rotate_and_add(num_list):
    sum_list=[]
    for val in num_list:
        idx=num_list.index(val)
        temp_list=num_list[idx:]+num_list[:idx]
        sum=0
        for key in range(len(num_list)):
            sum+=key*temp_list[key]
        sum_list.append(sum)
    return max(sum_list)

num_list=[4,3,2,6]
print(rotate_and_add(num_list))



    

import subprocess as sp

output=sp.getoutput("ifconfig")

print(output)

new_str="geeksforgeeks"

lis=list(new_str)

res=[]

for char in lis:
    if char not in res:
        res.append(char)

print("".join(res))


#Python program to store "ls" command values in a file and parse through it

import os

os.system("ls > new.txt")

with open("new.txt","r+") as f:
    try:
        re=f.read()
        list=re.split("\n")
    
        import re 

        for each in list:
            reg=re.findall("^n.*",each)
            if reg:
                print(reg[0])

    except:
        pass

txt="GeeksForGeeks"

import re

reg=re.findall(r"[^\w\d]",txt)

if reg:
    print("String is not accepted")
else:
    print("String accepted")


#Using compile

txt="GeeksForeeks"
regex=re.compile(r"[!@#$%^&*():]")

res=regex.search(txt)

if res:
    print("Not accepted")
else:
    print("Accepted")
    

nl=[0, 10, 20, 30, 40, 60,70,80]

for i in range(len(nl)-1):
    if nl[i]+10==nl[i+1]:
        pass
    else:
        print("False")
        break
else:
    print("True")

#New file    

import subprocess as sp

get_input=sp.getoutput("cat >> File")

print(get_input)

#new-LINE


with open("file1","w") as f1:
    f1.write("""\nWelcome to w3resource.com.                                                                                    
        Append this text.Append this text.Append this text.                                                           
        Append this text.                                                                                             
        Append this text.                                                                                             
        Append this text.                                                                                             
        Append this text. """)

with open("file1","r") as f2: 
    print(f2.read())

words = ["abcw","baz","foo","bar","xtfn","abcdef"]

words = ["a","ab","abc","d","cd","bcd","abcd"]

prdct_list=[]

for word in range(len(words)-1):
    for nxt in range(word+1,len(words)):
        if len(words[word])==len(words[nxt]):
            prdct_list.append(len(words[word])**2)

print(max(prdct_list))            

import subprocess as sp

out=sp.getoutput("netstat -i")

open_list=out.split("\n")

each_line_list=[]

for each  in open_list:
    each_line_list.append(each.split())


print(each_line_list[4][0],each_line_list[4][2],each_line_list[4][6])


n=98

while True:
    sum=0
    for i in str(n):
        sum+=int(i)
    n=sum
    if len(str(n))==1:
        break

print(n)    


n=96
sum=0
cnt=0

while True:
    r=n%10
    sum+=r**2
    n=n//10
    cnt+=1

    if n<1 and sum!=1:
        n=sum
        sum=0

    if sum==1 and n==0:
        print("Happy number")
        break

    if cnt>30:
        print("Unhappy number")
        break

import json
import re 
from getpass import getpass
from Json_handler import Basic_Functions
import Json_handler
import logging
import queue
import threading
import random

class Online_Bank:
    def __init__(self,User_Dict,Associated_Account_Numbers_List):
            self.User_Dict = User_Dict
            self.Associated_Account_Numbers = Associated_Account_Numbers_List

    def Deposit_Module(self):
        try :
            logging.basicConfig(filename = 'Test_log_Bank_Server.log',level = logging.DEBUG,\
                    format = '%(asctime)s-%(levelname)s- DEPOSIT_HISTORY -%(message)s')
            self.Ac_no = input("\nEnter your Account Number: ")
            if self.Ac_no not in self.Associated_Account_Numbers :
                print("\nEnter a Valid Account Number")
            self.Password = getpass("\nEnter your password: ")
            self.Amount = int(input("\nEnter the amount you want to deposit: "))
            for users in self.User_Dict:
                user = self.User_Dict[users]
                for details in user.values():
                    if self.Ac_no == details :
                        self.user = users
            self.Current_Balance = self.User_Dict[self.user]["Bank_Balance"]
            self.User_Name = self.User_Dict[self.user]["Cus_Name"]
            print("\nSuccessfully Credited your amount ")
            User_Instance.Deposit_Function()
            logging.info(" AC_NO : {},{} Credited Amount of {}".format(self.Ac_no,self.User_Name,self.Amount))
        except : 
            pass

    def Withdrawal_Module(self):
        try :

            logging.basicConfig(filename = 'Test_log_Bank_Server.log',level = logging.DEBUG,\
                    format = '%(asctime)s-%(levelname)s- WITHDRAW_HISTORY -%(message)s')
            self.Ac_no = input("\nEnter your Account Number: ")
            self.Password = getpass("\nEnter your password: ")
            self.Amount = int(input("\nEnter the amount you need to withdraw: "))
            for users in self.User_Dict:
                user = self.User_Dict[users]
                for details in user.values():
                    if self.Ac_no == details :
                        self.user = users
            user_balance = self.User_Dict[self.user]["Bank_Balance"]
            User_name = self.User_Dict[self.user]["Cus_Name"]
            if user_balance - self.Amount < 0 :
                print("\nYou have Insufficient Balance in your account")
                logging.error("{},{} tried debitting amount with insufficient balance".format(self.Ac_no,User_name))
            else:
                self.Amount_Withdrawn = self.Amount
                self.Remaining_Balance = user_balance - self.Amount
            print("\nAmount Withdrawn successfully")
            User_Instance.Withdraw_Function()
            User_Balance_Ask = input("\nDo you want to display the Balance ?(y/n) : ")
            if User_Balance_Ask == 'y' :
                print("\nRemaining Balance : {}".format(self.Remaining_Balance))
            else:
                pass
            logging.info(" AC_NO : {},{} Debited Amount of {}".format(self.Ac_no,User_name,self.Amount)) 
        
        except :
            pass

    def UPI_Module(self):
        try :
            logging.basicConfig(filename = 'Test_log_Bank_Server.log',level = logging.DEBUG,\
                    format = '%(asctime)s-%(levelname)s- UPI_TRANSFER -%(message)s')
            print("\nWelcome to UPI Payments Bank\n")
            self.UPI_User_Num = input("\nEnter your Mobile Number : ")
            if self.UPI_User_Num :
                mob_valid = re.search("[6789]\d{9}",self.UPI_User_Num)
                if mob_valid :
                    self.UPI_User_Num = self.UPI_User_Num
                else:
                    print("\nEnter valid Mobile Number ")    
                self.UPI_or_Mob = input("\nEnter UPI_id or mobile number you want to send money : ")
                if self.UPI_or_Mob :
                    self.Mob_number = 0
                    self.UPI_Id = 0
                    mob_valid = re.search("[6789]\d{9}",self.UPI_or_Mob)
                    if mob_valid :
                        self.Mob_number = self.UPI_or_Mob
                    UPI_valid = re.search("[a-z0-9]{1,15}@[a-z0-9]{1,15}",self.UPI_or_Mob)
                    if UPI_valid:
                        self.UPI_Id = self.UPI_or_Mob
                    if ( self.Mob_number == 0 and self.UPI_Id ==0 ):
                        print("\nEnter valid UPI ID or Mobile number\n")
                    for users in self.User_Dict:
                        user = self.User_Dict[users]
                        for details in user.values():
                            if ( self.Mob_number == details ) or ( self.UPI_Id == details ) :
                                self.user = users
                            if self.UPI_User_Num == details :
                                self.UPI_User = users
                    self.sender = self.User_Dict[self.UPI_User]["Cus_Name"] 
                    self.sender_AC_No = self.User_Dict[self.UPI_User]["Ac_No"]
                    self.send_recipient = self.User_Dict[self.user]["Cus_Name"]
                    self.Ac_num_to_transfer = self.User_Dict[self.user]["Ac_No"]
                    print("\nCustomer name : {}".format(self.send_recipient))
                    self.Amount_To_Send = int(input("\nEnter the amount you want to transfer : "))
                    if self.Amount_To_Send :
                        self.UPI_Pin_Check = int(getpass("\nEnter your four digit UPI PIN to continue : "))
                        if self.UPI_Pin_Check :
                            if self.User_Dict[self.UPI_User]["UPI_Pin"] == self.UPI_Pin_Check :
                                print("\nSuccessfully Sent Money")
                                User_Instance.UPI_Function()
                                Transaction_Id = "AX10105"+str(random.randrange(5000,6000))
                                print(f"\nYour Transaction ID : {Transaction_Id}")
                                logging.info("{} AC_No: {} sent amount of {} to {} AC_No: {} TxnId : {}"\
                                        .format(self.UPI_User_Num,self.sender_AC_No,self.Amount_To_Send\
                                        ,self.Mob_number,self.Ac_num_to_transfer,Transaction_Id))
                            else :
                                print("\nEnter the Correct UPI PIN ")
                                logging.error("{} Tried sending money with wrong UPI_PIN".format(self.UPI_User_Num))
                        UPI_Queue.put(self.UPI_User_Num)
                        UPI_Queue.put(self.Mob_number)
                        UPI_Queue.put(self.Amount_To_Send)
                        UPI_Queue.put(Transaction_Id)
                        UPI_Event.set()

        except:
            pass
class Customer(Online_Bank,Basic_Functions):
    def __init__(self,Json_File_Name):
        self.Json_File_Name = Json_File_Name
        User_Dict = Basic_Functions.Read_File(self.Json_File_Name)
        Associated_Account_Numbers_List = [User_Dict[User][details] for User in User_Dict for details in\
                User_Dict[User] if details == 'Ac_No']
        Online_Bank.__init__(self,User_Dict,Associated_Account_Numbers_List)


    def Deposit_Function(self):
        try :
            self.User_Dict[self.user]["Bank_Balance"] += self.Amount
            Basic_Functions.Write_File(self.Json_File_Name,self.User_Dict)
        except Exception as error:
            print("\nEnter the credentials correctly")
            
    def Withdraw_Function(self):
        try :
            if self.Remaining_Balance :
                self.User_Dict[self.user]["Bank_Balance"] = self.Remaining_Balance
                Basic_Functions.Write_File(self.Json_File_Name,self.User_Dict)
        except :
            print("\nEnter the credentials correctly")

    def UPI_Function(self):
        try :
            for users in self.User_Dict:
                user = self.User_Dict[users]
                for details in user.values():
                    if self.Ac_num_to_transfer == details :
                        self.user = users
                    if self.UPI_User == details :
                        self.UPI_User_username = users

            self.User_Dict[self.UPI_User]["Bank_Balance"] -= self.Amount_To_Send            
            self.User_Dict[self.user]["Bank_Balance"] += self.Amount_To_Send 
            Basic_Functions.Write_File(self.Json_File_Name,self.User_Dict)
        except :
            print("\nEnter the credentials correctly")

UPI_Event = threading.Event()
UPI_Queue = queue.Queue()

def UPI_Transaction_History():
    try :
        Main_Database = Json_handler.Basic_Functions.Read_File("server_entries.json")
        show_list = []
        UPI_Event.wait()
        for get_data in range(4):
            show_list.append(UPI_Queue.get())
        Sender_Number = show_list[0]
        Receiver_Number = show_list[1]
        Amount = show_list[2]
        Txn_Id = show_list[3]
        for users in Main_Database :
            user = Main_Database[users]
            for details in user.values():
                if Sender_Number == details :
                    Send_User = users
                if Receiver_Number == details :
                    Receive_User = users
        Sender_Ac_No = Main_Database[Send_User]["Ac_No"]
        Receiver_Ac_No = Main_Database[Receive_User]["Ac_No"]
        logging.info("{} AC_No : {} Received Amount of {} from {} AC_No : {} TxnId : {}".\
                format(Receiver_Number,Receiver_Ac_No,Amount,Sender_Number,Sender_Ac_No,Txn_Id))

    except :
        print("\nEnter the credentials correctly")

User_Instance = Customer("server_entries.json")
UPI_Transfer_Process = threading.Thread(target = User_Instance.UPI_Module)
UPI_Receiver_Process = threading.Thread(target = UPI_Transaction_History)

def View_Transaction_History():
    try :
        Mobile_Number = input("\nEnter your mobile number : ")
        with open("Test_log_Bank_Server.log","r") as log_file :
            log_list = (log_file.read()).split("\n")
        for log in log_list :
            #if (Mobile_Number and "UPI_TRANSFER") in log and ("ERROR" not in log) :
            if Mobile_Number in log and "UPI_TRANSFER" in log and "ERROR" not in log :
                start_index = log.find("UPI_TRANSFER")
                print(log[start_index:])
    except :
        print("\nEnter the credentials correctly")

def Balance_Check():
    Json_handler.Feature_Instance.Check_Bank_Balance()

def Mini_Statement():
    Json_handler.Feature_Instance.Check_Mini_Statement()

No_Of_Tries = 3

while No_Of_Tries > 0 :
    Password_Check = getpass("\nEnter Password to Enter : ")
    print()
    if Password_Check == "1234":
        while True :
            print()
            Txt_To_Display = "Welcome to Online Banking Service"
            Nxt_txt_to_display = """1) CASH_WITHDRAWAL
2) CASH_DEPOSIT
3) UPI_MONEY_TRANSFER
4) NEW_ACCOUNT_CREATE
5) BALANCE_ENQUIRY
6) MINI_STATEMENT
7) VIEW_UPI_TRANSACTION_HISTORY
                   """
            print(Nxt_txt_to_display)                              
    
            try :
                User_Option = int(input("\nWhat have you got to do. Select an option : "))
            except ValueError :
                print("\nEnter a Valid Input")
                continue
            
            if User_Option == 1 :
                User_Instance.Withdrawal_Module()
            elif User_Option == 2 :
                User_Instance.Deposit_Module()
            elif User_Option == 3 :
                UPI_Transfer_Process.start()
                UPI_Receiver_Process.start()
                break
            elif User_Option == 4 :
                print("\n*****Only Admin Can Add New Users*****")
                User_Check = getpass("\nEnter Password : ")
                if User_Check == 'admin' :
                    from New_User_Addition import Add_New_User
                else :
                    print("\nEnter the Correct Password")
            elif User_Option == 5 :
                Balance_Check()
            elif User_Option == 6 :
                Mini_Statement()
            elif User_Option == 7 :
                View_Transaction_History()
            elif User_Option > 7  or User_Option < 1:
                print("\nEnter a valid option")
                continue


            User_Continuation = int(input("\nDo You want to continue Banking.Press 1 to continue .0 to terminate : "))
            if User_Continuation == 1 :
                continue
            elif User_Continuation == 0 :
                print()
                Exit_txt = "Thanks for Banking with Us"
                print(Exit_txt.center(100))
                No_Of_Tries = -1
                break 
    else :
        if No_Of_Tries == 1:
            break
        print("\nEnter the correct password and try again")
    No_Of_Tries -= 1    


import json
import re 
from getpass import getpass
from Json_handler import Basic_Functions
import Json_handler
import logging
import queue
import threading
import random

class Online_Bank:
    def __init__(self,User_Dict,Associated_Account_Numbers_List):
            self.User_Dict = User_Dict
            self.Associated_Mobile_Numbers = Associated_Account_Numbers_List

    def Deposit_Module(self):
        try :
            logging.basicConfig(filename = 'Test_log_Bank_Server.log',level = logging.DEBUG,\
                    format = '%(asctime)s-%(levelname)s- DEPOSIT_HISTORY -%(message)s')
            self.Ac_no = input("\nEnter your Account Number: ")
            self.Password = getpass("\nEnter your password: ")
            self.Amount = int(input("\nEnter the amount you want to deposit: "))
            for users in self.User_Dict:
                user = self.User_Dict[users]
                for details in user.values():
                    if self.Ac_no == details :
                        self.user = users
            self.Current_Balance = self.User_Dict[self.user]["Bank_Balance"]
            self.User_Name = self.User_Dict[self.user]["Cus_Name"]
            print("\nSuccessfully Credited your amount ")
            User_Instance.Deposit_Function()
            logging.info(" AC_NO : {},{} Credited Amount of {}".format(self.Ac_no,self.User_Name,self.Amount))
        except : 
            pass

    def Withdrawal_Module(self):
        try :

            logging.basicConfig(filename = 'Test_log_Bank_Server.log',level = logging.DEBUG,\
                    format = '%(asctime)s-%(levelname)s- WITHDRAW_HISTORY -%(message)s')
            self.Ac_no = input("\nEnter your Account Number: ")
            self.Password = getpass("\nEnter your password: ")
            self.Amount = int(input("\nEnter the amount you need to withdraw: "))
            for users in self.User_Dict:
                user = self.User_Dict[users]
                for details in user.values():
                    if self.Ac_no == details :
                        self.user = users
            user_balance = self.User_Dict[self.user]["Bank_Balance"]
            User_name = self.User_Dict[self.user]["Cus_Name"]
            if user_balance - self.Amount < 0 :
                print("\nYou have Insufficient Balance in your account")
                logging.error("{},{} tried debitting amount with insufficient balance".format(self.Ac_no,User_name))
            else:
                self.Amount_Withdrawn = self.Amount
                self.Remaining_Balance = user_balance - self.Amount
            print("\nAmount Withdrawn successfully")
            User_Instance.Withdraw_Function()
            User_Balance_Ask = input("\nDo you want to display the Balance ?(y/n) : ")
            if User_Balance_Ask == 'y' :
                print("\nRemaining Balance : {}".format(self.Remaining_Balance))
            else:
                pass
            logging.info(" AC_NO : {},{} Debited Amount of {}".format(self.Ac_no,User_name,self.Amount)) 
        
        except :
            pass

    def UPI_Module(self):
        try :
            logging.basicConfig(filename = 'Test_log_Bank_Server.log',level = logging.DEBUG,\
                    format = '%(asctime)s-%(levelname)s- UPI_TRANSFER -%(message)s')
            print("\nWelcome to UPI Payments Bank\n")
            self.UPI_User_Num = input("\nEnter your Mobile Number : ")
            if self.UPI_User_Num :
                mob_valid = re.search("[6789]\d{9}",self.UPI_User_Num)
                if mob_valid :
                    self.UPI_User_Num = self.UPI_User_Num
                else:
                    print("\nEnter valid Mobile Number ")    
                self.UPI_or_Mob = input("\nEnter UPI_id or mobile number you want to send money : ")
                if self.UPI_or_Mob :
                    self.Mob_number = 0
                    self.UPI_Id = 0
                    mob_valid = re.search("[6789]\d{9}",self.UPI_or_Mob)
                    if mob_valid :
                        self.Mob_number = self.UPI_or_Mob
                    UPI_valid = re.search("[a-z0-9]{1,15}@[a-z0-9]{1,15}",self.UPI_or_Mob)
                    if UPI_valid:
                        self.UPI_Id = self.UPI_or_Mob
                    if ( self.Mob_number == 0 and self.UPI_Id ==0 ):
                        print("\nEnter valid UPI ID or Mobile number\n")
                    for users in self.User_Dict:
                        user = self.User_Dict[users]
                        for details in user.values():
                            if ( self.Mob_number == details ) or ( self.UPI_Id == details ) :
                                self.user = users
                            if self.UPI_User_Num == details :
                                self.UPI_User = users
                    self.sender = self.User_Dict[self.UPI_User]["Cus_Name"] 
                    self.sender_AC_No = self.User_Dict[self.UPI_User]["Ac_No"]
                    self.send_recipient = self.User_Dict[self.user]["Cus_Name"]
                    self.Ac_num_to_transfer = self.User_Dict[self.user]["Ac_No"]
                    print("\nCustomer name : {}".format(self.send_recipient))
                    self.Amount_To_Send = int(input("\nEnter the amount you want to transfer : "))
                    if self.Amount_To_Send :
                        self.UPI_Pin_Check = int(getpass("\nEnter your four digit UPI PIN to continue : "))
                        if self.UPI_Pin_Check :
                            if self.User_Dict[self.UPI_User]["UPI_Pin"] == self.UPI_Pin_Check :
                                print("\nSuccessfully Sent Money")
                                User_Instance.UPI_Function()
                                Transaction_Id = "AX10105"+str(random.randrange(5000,6000))
                                print(f"\nYour Transaction ID : {Transaction_Id}")
                                logging.info("{} AC_No: {} sent amount of {} to {} AC_No: {} TxnId : {}"\
                                        .format(self.UPI_User_Num,self.sender_AC_No,self.Amount_To_Send\
                                        ,self.Mob_number,self.Ac_num_to_transfer,Transaction_Id))
                            else :
                                print("\nEnter the Correct UPI PIN ")
                                logging.error("{} Tried sending money with wrong UPI_PIN".format(self.UPI_User_Num))
                        UPI_Queue.put(self.UPI_User_Num)
                        UPI_Queue.put(self.Mob_number)
                        UPI_Queue.put(self.Amount_To_Send)
                        UPI_Queue.put(Transaction_Id)
                        UPI_Event.set()

        except:
            pass
class Customer(Online_Bank,Basic_Functions):
    def __init__(self,Json_File_Name):
        self.Json_File_Name = Json_File_Name
        User_Dict = Basic_Functions.Read_File(self.Json_File_Name)
        Associated_Account_Numbers_List = [User_Dict[User][details] for User in User_Dict for details in\
                User_Dict[User] if details == 'Ac_No']
        Online_Bank.__init__(self,User_Dict,Associated_Account_Numbers_List)


    def Deposit_Function(self):
        try :
            self.User_Dict[self.user]["Bank_Balance"] += self.Amount
            Basic_Functions.Write_File(self.Json_File_Name,self.User_Dict)
        except Exception as error:
            print("\nEnter the credentials correctly")
            
    def Withdraw_Function(self):
        try :
            if self.Remaining_Balance :
                self.User_Dict[self.user]["Bank_Balance"] = self.Remaining_Balance
                Basic_Functions.Write_File(self.Json_File_Name,self.User_Dict)
        except :
            print("\nEnter the credentials correctly")

    def UPI_Function(self):
        try :
            for users in self.User_Dict:
                user = self.User_Dict[users]
                for details in user.values():
                    if self.Ac_num_to_transfer == details :
                        self.user = users
                    if self.UPI_User == details :
                        self.UPI_User_username = users

            self.User_Dict[self.UPI_User]["Bank_Balance"] -= self.Amount_To_Send            
            self.User_Dict[self.user]["Bank_Balance"] += self.Amount_To_Send 
            Basic_Functions.Write_File(self.Json_File_Name,self.User_Dict)
        except :
            print("\nEnter the credentials correctly")

UPI_Event = threading.Event()
UPI_Queue = queue.Queue()

def UPI_Transaction_History():
    try :
        Main_Database = Json_handler.Basic_Functions.Read_File("server_entries.json")
        show_list = []
        UPI_Event.wait()
        for get_data in range(4):
            show_list.append(UPI_Queue.get())
        Sender_Number = show_list[0]
        Receiver_Number = show_list[1]
        Amount = show_list[2]
        Txn_Id = show_list[3]
        for users in Main_Database :
            user = Main_Database[users]
            for details in user.values():
                if Sender_Number == details :
                    Send_User = users
                if Receiver_Number == details :
                    Receive_User = users
        Sender_Ac_No = Main_Database[Send_User]["Ac_No"]
        Receiver_Ac_No = Main_Database[Receive_User]["Ac_No"]
        logging.info("{} AC_No : {} Received Amount of {} from {} AC_No : {} TxnId : {}".\
                format(Receiver_Number,Receiver_Ac_No,Amount,Sender_Number,Sender_Ac_No,Txn_Id))

    except :
        print("\nEnter the credentials correctly")

User_Instance = Customer("server_entries.json")
UPI_Transfer_Process = threading.Thread(target = User_Instance.UPI_Module)
UPI_Receiver_Process = threading.Thread(target = UPI_Transaction_History)

def View_Transaction_History():
    try :
        Mobile_Number = input("\nEnter your mobile number : ")
        with open("Test_log_Bank_Server.log","r") as log_file :
            log_list = (log_file.read()).split("\n")
        for log in log_list :
            #if (Mobile_Number and "UPI_TRANSFER") in log and ("ERROR" not in log) :
            if Mobile_Number in log and "UPI_TRANSFER" in log and "ERROR" not in log :
                start_index = log.find("UPI_TRANSFER")
                print(log[start_index:])
    except :
        print("\nEnter the credentials correctly")

def Balance_Check():
    Json_handler.Feature_Instance.Check_Bank_Balance()

def Mini_Statement():
    Json_handler.Feature_Instance.Check_Mini_Statement()

No_Of_Tries = 3

while No_Of_Tries > 0 :
    Password_Check = getpass("\nEnter Password to Enter : ")
    print()
    if Password_Check == "1234":
        while True :
            print()
            Txt_To_Display = "Welcome to Online Banking Service"
            Nxt_txt_to_display = """1) CASH_WITHDRAWAL
2) CASH_DEPOSIT
3) UPI_MONEY_TRANSFER
4) NEW_ACCOUNT_CREATE
5) BALANCE_ENQUIRY
6) MINI_STATEMENT
7) VIEW_UPI_TRANSACTION_HISTORY
                   """
            print(Nxt_txt_to_display)                              
    
            try :
                User_Option = int(input("\nWhat have you got to do. Select an option : "))
            except ValueError :
                print("\nEnter a Valid Input")
                continue
            
            if User_Option == 1 :
                User_Instance.Withdrawal_Module()
            elif User_Option == 2 :
                User_Instance.Deposit_Module()
            elif User_Option == 3 :
                UPI_Transfer_Process.start()
                UPI_Receiver_Process.start()
                break
            elif User_Option == 4 :
                print("\n*****Only Admin Can Add New Users*****")
                User_Check = getpass("\nEnter Password : ")
                if User_Check == 'admin' :
                    from New_User_Addition import Add_New_User
                else :
                    print("\nEnter the Correct Password")
            elif User_Option == 5 :
                Balance_Check()
            elif User_Option == 6 :
                Mini_Statement()
            elif User_Option == 7 :
                View_Transaction_History()
            elif User_Option > 7  or User_Option < 1:
                print("\nEnter a valid option")
                continue


            User_Continuation = int(input("\nDo You want to continue Banking.Press 1 to continue .0 to terminate : "))
            if User_Continuation == 1 :
                continue
            elif User_Continuation == 0 :
                print()
                Exit_txt = "Thanks for Banking with Us"
                print(Exit_txt.center(100))
                No_Of_Tries = -1
                break 
    else :
        if No_Of_Tries == 1:
            break
        print("\nEnter the correct password and try again")
    No_Of_Tries -= 1    


import socket
client = socket.socket()
client.connect(('192.168.1.22',5005))


def Withdraw_Module():
    client.send((input("\nEnter your Account Number: ")).encode())
    client.send((input("\nEnter the amount you need to withdraw: ").encode()))
    try :
        Insufficient_msg = client.recv(1024).decode()
        print(Insufficient_msg)
    except :
        pass
    Balance_Show = input("\nDo you want to show the balance?(y/n) ")
    if Balance_Show == 'y' :
        client.send("Show_Balance".encode())
        print(client.recv(1024).decode())
    else :
        client.send("No Balance Show".encode())


def Deposit_Module():
    client.send((input("\nEnter your Account Number: ")).encode())
    client.send((input("\nEnter the amount you want to deposit: ")).encode())
    print(client.recv(1024).decode())

Services_Offered = """1.CASH_WITHDRAWAL
2.CASH_DEPOSIT"""

while True :
    print(Services_Offered)
    User_Option = int(input("\nEnter your choice: "))
    client.send(str(User_Option).encode())
    if User_Option == 1 :
        Withdraw_Module()
    elif User_Option == 2 :
        Deposit_Module()
    User_Opinion = int(input("\nDo you want to continue.Enter 2 to continue.0 to terminate :"))
    if User_Opinion == 0 :
        break

'''           
            for users in self.User_Dict:
                user = self.User_Dict[users]
                for details in user.values():
                    if self.Ac_no == details :
                        self.user_name = users
            user_balance = self.User_Dict[self.user_name]["Bank_Balance"]
            User_name = self.User_Dict[self.user_name]["Cus_Name"]
            if user_balance - self.Amount < 0 :
                print("\nYou have Insufficient Balance in your account")
                logging.error("{},{} tried debitting amount with insufficient balance".format(self.Ac_no,User_name))
            else:
                self.Amount_Withdrawn = self.Amount
                self.Remaining_Balance = user_balance - self.Amount
            print("\nAmount Withdrawn successfully")
            User_Balance_Ask = input("\nDo you want to display the Balance ?(y/n) : ")
            if User_Balance_Ask == 'y' :
                print("\nRemaining Balance : {}".format(self.Remaining_Balance))
            else:
                pass
            logging.info(" AC_NO : {},{} Debited Amount of {}".format(self.Ac_no,User_name,self.Amount))

        except :
            pass
'''

import os
import json
class Basic_Functions:
    def __init__(self):
        pass

    def Read_File(filepath):
        try :
            if os.path.isfile(filepath):
                with open(filepath,"r") as file:
                    file_txt = file.read()
                    Read_Content = json.loads(file_txt)
        except Exception as error:
            print(error)
        return Read_Content

    def Write_File(filepath,content):
        try:
            if os.path.isfile(filepath):
                with open(filepath,"w") as file:
                    file.write(json.dumps(content,indent = 4,separators = ',:'))
                    return 'Success'
        except Exception as error :
            print("Unsuccessful")
        return 'Failure'


class Added_Features(Basic_Functions):
    def Check_Bank_Balance(self):
        try :
            Mob_Number = input("\nEnter Your Mobile number associated with UPI Bank : ")
            Main_Database = Basic_Functions.Read_File("server_entries.json")
            for users in Main_Database :
                user = Main_Database[users]
                for data in user.values() :
                    if data == Mob_Number :
                        User = users
        
            Bank_Balance = Main_Database[User]["Bank_Balance"] 
            Customer_Name = Main_Database[User]["Cus_Name"]
            print(f"\nCustomer Name : {Customer_Name}")
            print(f"\nAvailable Bank Balance : {Bank_Balance}")

        except :
            print("\nEnter the credentials correctly")

    def Check_Mini_Statement(self):
        try :
            AC_NUM = input("\nEnter Your Account Number : ")
            print()
            Main_Database = Basic_Functions.Read_File("server_entries.json")
            for users in Main_Database :
                user = Main_Database[users]
                for data in user.values() :
                    if data == AC_NUM :
                        User = users
            with open("Test_log_Bank_Server.log","r") as log_file :
                log_content = log_file.read()
            log_list = log_content.split("\n")
            User_log_list = []
            for user_statement in log_list :
                if AC_NUM in user_statement :
                    User_log_list.append(user_statement)
            for all_entries in User_log_list :
                if "INFO" in all_entries :
                    idx = all_entries.find("INFO")
                    only_needed_data = all_entries[idx+6 :]
                    print(only_needed_data)
        except :
            print("\nEnter the credentials correctly")

Feature_Instance = Added_Features()
#Feature_Instance.Check_Mini_Statement()

import re
from Json_handler import Basic_Functions 
import logging

class Add_New_User(Basic_Functions):
    def __init__(self):
        logging.basicConfig(filename = 'Test_log_Bank_Server.log',level = logging.DEBUG,format = '%(asctime)s-%(levelname)s- NEW_ACCOUNT -%(message)s')
    def Get_Bio_Data(self):
        print()
        try:
            Welcome_Text = "Welcome to Adding New Account to Online Bank "
            print(Welcome_Text.center(100))
            self.First_Name = input("\nEnter your first Name.First Name should start with Capital letter and should not exceed 10 characters : ")
            Fname_Check = re.search("[A-Z][a-z]{2,10}",self.First_Name)
            if Fname_Check :
                self.First_Name = self.First_Name
            else : 
                print("\nPlease enter Valid First Name")
            self.Last_Name = input("\nEnter your Last Name.Last Name should start with Capital letter should not exceed 10 characters : ")
            Lname_Check = re.search("[A-Z][a-z]{2,10}",self.Last_Name)
            if Lname_Check :
                self.Last_Name = self.Last_Name 
            else :
                print("\nPlease enter Valid Last Name")
            self.Age = int(input("\nEnter your Age : "))
            self.Email = input("\nEnter your Email ID : ")
            Email_Check = re.search("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9-\-]+)\.([a-zA-Z]{2,5})$",self.Email)
            if Email_Check :
                self.Email = self.Email
            else :
                print("\nEnter a Valid Email")
            self.Mobile_Number = input("\nEnter your Mobile Number : ")
            mob_valid = re.search("[6789]\d{9}",self.Mobile_Number)
            if mob_valid :
                self.Mobile_Number = self.Mobile_Number
            else :
                print("\nEnter Valid mobile number")
            self.First_Deposit = int(input("\nEnter the amount you want to credit in your account : "))
            print("\nYou have successfully created Account")
       
        except :
            print("\nEnter the credentials correctly")

    def Update_Details(self):
        try :
            User_Credentials = Basic_Functions.Read_File("User_Credentials.json")
            User = User_Credentials["User"]
            New_User = {}
            New_User["Ac_No"] = str(User_Credentials["Account_Number"])
            New_User["First_Name"] = self.First_Name 
            New_User["Last_Name"] = self.Last_Name
            New_User["Cus_Name"] = self.First_Name + " " + self.Last_Name
            New_User["Age"] = self.Age
            New_User["Email"] = self.Email
            New_User["Mob_Num"] = self.Mobile_Number
            New_User["Bank_Balance"] = self.First_Deposit
            New_User["UPI_Id"] = self.First_Name + self.Last_Name + "@" + "ybl" + str(User_Credentials["UPI_Num"])
            New_User["UPI_Pin"] = User_Credentials["UPI_Pin"]
            Main_Database = Basic_Functions.Read_File("server_entries.json")
            Main_Database["User_"+str(User)] = New_User
            User_Credentials = {key : value+1 for key,value in User_Credentials.items()}
            Basic_Functions.Write_File("User_Credentials.json",User_Credentials)
            Basic_Functions.Write_File("server_entries.json",Main_Database)
            logging.info(" New Account created AC_No : {},{}".format(New_User["Ac_No"],New_User["Cus_Name"]))
        
        except :
            print("\nEnter the credentials correctly")

Add_Instance = Add_New_User()
Add_Instance.Get_Bio_Data()
Add_Instance.Update_Details()


import socket
#import Json_handler
from _thread import *
import os 
import json
import multiprocessing

server = socket.socket()
host = socket.gethostname()
port = 5005
server.bind((host,port))
server.listen(2)

Lock = multiprocessing.Lock()

def Read_File(filepath):
    try : 
        if os.path.isfile(filepath):
            with open(filepath,'r') as json_file :
                Lock.acquire()
                file_txt = json_file.read()
                read_content = json.loads(file_txt)
                Lock.release()
    except Exception as error :
        print(error)
    return read_content

def Write_File(filepath,content):
    try :
        if os.path.isfile(filepath):
            Lock.acquire()
            with open(filepath,'w') as json_file :
                json_file.write(json.dumps(content,indent = 4,separators = ',:'))
                Lock.release()
    except Exception as error:
        print(error)

    return 'success'    

def Withdrawal_Module(client):
    Main_Database = Read_File("Server_Entries.json")
    Ac_No = client.recv(1024).decode()
    Amount = client.recv(1024).decode()
    for users in Main_Database :
        user = Main_Database[users]
        for details in user.values() :
            if details == Ac_No :
                User_Name = users
    Balance_Amount = Main_Database[User_Name]["Bank_Balance"]
    Remaining_Balance = Main_Database[User_Name]["Bank_Balance"] - int(Amount)
    if int(Amount) < Balance_Amount :
        Main_Database[User_Name]["Bank_Balance"] -= int(Amount)
        client.send("\nSuccessfully Debited".encode())
    else :
        client.send("\nInsufficient_Balance".encode())
    if client.recv(1024).decode() == "Show_Balance" :
        client.send(f"\nRemaining_Balance : {Remaining_Balance}".encode())
    else :
        pass
    Write_File("Server_Entries.json",Main_Database)
    #Json_handler.Basic_Functions.Write_File("Server_Entries.json",Main_Database)

def Deposit_Module(client):
    Main_Database = Read_File("Server_Entries.json")
    Ac_No = client.recv(1024).decode()
    Amount = client.recv(1024).decode()
    for users in Main_Database :
        user = Main_Database[users]
        for details in user.values():
            if Ac_No == details :
                User_Name = users
    Main_Database[User_Name]["Bank_Balance"] += int(Amount)
    client.send("\nSuccessfully Credited".encode())
    Write_File("Server_Entries.json",Main_Database)

def Init_Function(client):
    User_Option = client.recv(1024).decode()
    if User_Option == '1':
        Withdrawal_Module(client)
    if User_Option == '2':
        Deposit_Module(client)

while True :
    client,address = server.accept()
    print(f"Connected with client {address}")
    start_new_thread(Init_Function,(client,))




test_dict = {'abc' : [10, 30], 'bcd' : [30, 40, 10]}
res_dict = {}
temp_set = {char for List in test_dict.values() for char in List}
for char in temp_set :
    temp_list = [key for key,val in test_dict.items() if char in val]
    res_dict[char] = temp_list
print(res_dict)    


from collections import defaultdict
res = defaultdict(list)
print(res)

test_dict = {'gfg' : [5, 6, 7, 8],
             'is' : [10, 11, 7, 5],
             'best' : [6, 12, 10, 8],
             'for' : [1, 2, 5]}


res = list(sorted({char for List in test_dict.values() for char in List}))

print(res)

new_set = {2,9,6,7,9}

new_set = list(new_set)
print(sorted(new_set))



from selenium import webdriver

driver = webdriver.Firefox(executable_path='/home/sriram/geckodriver-v0.30.0-linux64/geckodriver.exe')

driver.get('https://www.google.com')

s = "geek"
t = "geek"
added_char = 0

for char in range(len(s)+1):
    print(s[char])
    if s[char] == t[char]:
        pass
    else :
        s = s[:char] + t[char] + s[char:]
        added_char +=1

print(added_char)        

Mar_16

Today's Update :

-Learned http protocol ,web servers and proxy servers

-Done the basic configurations in jenkins tool for the CI/CD pipeline  

-Learned basics of selenium to automate web browser in python 

array = [1,1,2,6,4,6]

for char in range(len(array)) :
    if array[char] in array[:char] or array[char] in array[char+1:] :
        while True :
            inc_value = array[char]+1
            if inc_value in array[:char] or inc_value in array[char+1:] :
                array[char] = inc_value
            else :
                return_value = inc_value
                break
        array[char] = return_value

print(array)        

def check_one(array):
    res = 0
    large = max(array)
    if large < 0 :
        res = 1
    for char in range(large+1):
        if char not in array :
            res = char
    if res == 0 :
        res = large + 1
    return res

array = [-1,-3]
print(check_one(array))

array = [1,2,3,4,5,6,7,8,9,10]
n = 15

res_list = []
for i in range(len(array)):
    for j in range(len(array)+1):
        if sum(array[i:j]) == n:
            print(i,j)
            res_list.append(i+1)
            res_list.append(j)
print(array)            
print(res_list[:2])            

import random

list = [1,2,3,4,5]

random.shuffle(list)
print(list)

tups = [("akash", 10), ("gaurav", 12), ("anand", 14), 
     ("suraj", 20), ("akhil", 25), ("ashish", 30)]

res_dict = {}

for name,number in tups :
    res_dict.setdefault(name,[]).append(number)

print(res_dict)    

easy_dict = dict(tups)
print(easy_dict)

def accept_args(arg1,arg2,arg3):
    print(arg1,arg2,arg3)

new_tuple = ('Hello','world','python')
accept_args(*new_tuple)

new_dict = {'arg1' : 'hello','arg2' : 'world','arg3' : 'java'}
accept_args(**new_dict)  #Function will return the values of the dictionaries if it matches with the key names in the dictionary



dict_list = [{'manoj': 'java', 'bobby': 'python'},
        {'manoj': 'php', 'bobby': 'java'},
        {'manoj': 'cloud', 'bobby': 'big-data'}]

temp = dict_list[0]
res_dict = {key : [] for key in temp}

for dict in dict_list :
    for key in dict :
        if key in res_dict :
            res_dict[key].append(dict[key])

print(res_dict)

# Alternate

result = {key : [dict[key] for dict in dict_list] for key in dict_list[0]}

print(result)


my_list = [1, 2, 3, 1, 5, 4]

result = [idx for idx,char in enumerate(my_list) if char == 1]

print(result)

new_list = ['sravan', 98, 'harsha', 'jyothika', 'deepika', 78, 90, 'ramya']

result = [idx for idx,val in enumerate(new_list) if isinstance(val,str)]

print(result)

# Alternate 

idx_list = []

for value in new_list :
    if type(value) is str :
        idx_list.append(new_list.index(value))

print(idx_list)        

a = 'apple'
print(a.index('l'))

#! /bin/python3

def accept_any(n,arr=[1,3,5,7,9]):
    for i in range(n):
        for j in arr :
            print(i+j)

#accept_any(2)  #You can also give like this without arr argument
#accept_any(3,[2,4,6,8,10])            




a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]

a = set(a)
b = set(b) 

result = b-a  # Will return the elements of b that is not in a
result2 = a.difference(b) # It also do the same work
print(result2)
print(result)

test_dict =  {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

sort_list = [val for val in test_dict.values()]
sort_list.sort(reverse = True)

result_dict = {key :val for char in sort_list for key,val in test_dict.items() if char == val}
print(result_dict)

import array

new_array = array.array('i',[2,3,2,5,7])

new_array[1] = 2

for i in new_array:
    print(i)

new_array = array.array('f',{2,1,4,3,9})   # 'd' used to store double elements 'f' for float

new_array.insert(2,4)
new_array.append(1234)
new_array.pop(3)
print(new_array)
new_array.remove(2)
new_list = [1,2,34,8]
new_list.pop()
print(new_list)


vari = {'a':2}
mem = id(vari)      #To show the memory location of the variables stored
print(hex(mem))
var = 10
var1 = 11
var2 = 12
print(id(var))
print(id(var1))
print(id(var2))

test_list = ["geekforgeeks", [5, 4, 3, 4], "is",
			["best", "good", "better", "average"]]

cnt=
k=4
res=[]

while cnt <= k-1:
    temp=[]
    for i in test_list:                  #To group the list using conditions
        if not isinstance(i,list):
            temp.append(i)
        else:
            temp.append(i[cnt])
    cnt+=1
    res.append(temp)
for i in res:
    print(i)

lis=[11, 12, 14, 13, 13, 15, 14]
len=len(lis)
idx5=lis[4]
count=0
for j in lis:
    if j==idx5:
        count+=1

if len==8 and count==3:
    print("True")
else:
    print("False")   
giv_list=[4,6,4,3,3,4,3,4,3,8]
k=3
res_list=[]
new_list=set(giv_list)             #To get the count of repeated values
for i in new_list:
    if giv_list.count(i) > k:
        res_list.append(i)
print(res_list)

A_list=[12,12,12,44,33,44,9,9,9,2]
res=[]
for i in range(len(A_list)-3):
    if A_list[i]==A_list[i+1] and A_list[i+1]==A_list[i+2]:   #To find three consecutive values
        res.append(A_list[i])
print(res)        

print("Hello world")
nums=[0,1,2,2,3,0,4,2]
val=2
temp_list=['_' for i in range(len(nums))]
for i in range(len(nums)):
    if nums[i]!=val:
        temp_list[i]=nums[i]
res_list=[]
for i in temp_list:
    if str(i).isdigit():
        res_list.append(i)
for val in range(len(nums)-len(res_list)):
    res_list.append('_')
print(res_list)    

n1=int(input("Enter the start value: "))
n2=int(input("Enter the end value: "))
time=int(input("Enter time: "))
new_list=[]
for i in range(n1,n2+1):
    new_list.append(i)
rev_list=new_list[::-1]    
ret_value=n2-n1
rem=int(time%ret_value)   #To print the position of time value in the given range
ans=0
q=time//ret_value
if q%2==0:
    for j in range(len(new_list)):
        ans+=new_list[rem]
        break
elif q%2!=0:
    for h in range(len(new_list),-1,-1):
        new_list
        ans+=rev_list[rem]
        break       
print(ans)      


ip="10.10.278.1"
l=ip.split(".")

for i in l:
    if int(i)>255:
        print("Invalid IP")
        break
else:
    print("valid IP")    
test_list = ["geekforgeeks", [5, 4, 3, 4], "is",
			["best", "good", "better", "average"]]

cnt=
k=4
res=[]

while cnt <= k-1:
    temp=[]
    for i in test_list:                  #To group the list using conditions
        if not isinstance(i,list):
            temp.append(i)
        else:
            temp.append(i[cnt])
    cnt+=1
    res.append(temp)
for i in res:
    print(i)

giv_list=[4,6,4,3,3,4,3,4,3,8]
k=3
res_list=[]
new_list=set(giv_list)             #To get the count of repeated values
for i in new_list:
    if giv_list.count(i) > k:
        res_list.append(i)
print(res_list)

A_list=[12,12,12,44,33,44,9,9,9,2]
res=[]
for i in range(len(A_list)-3):
    if A_list[i]==A_list[i+1] and A_list[i+1]==A_list[i+2]:   #To find three consecutive values
        res.append(A_list[i])
print(res)        

A=[2,6,4,2,5,9]
print(list(reversed(A)))
newlist=[]
for i in range(3):
    val=int(input())
    newlist.append(val)
for i in range(3):
    value=[input(),input(),input()]
    newlist.append(value)
print(newlist)

new_list=[3,56,67,3,14,2,1,56,9]
from collections import Counter
val=Counter(new_list).keys()
print(val)

test_list=[(4,5),(5,6),(1,3),(0,0),(5,3),(2,4),(5,5),(2,1),(5,6,6,9)]
for i in test_list:
    for j in range(len(i)):
        if j<len(i)-1:                                           #To remove a list containing consecutive x values
            if i[j]==i[j+1]:
                test_list.remove(i)
                continue
print(test_list)            


Ai=['A','B','C']
for i in range(3):
    for j in range(3):                    #permutations
        for k in range(3):
            if i!=j and j!=k and i!=k:
                print(Ai[i],Ai[j],Ai[k]) 
                                           
from itertools import permutations               #using itertools
comb=permutations([1,2,3])
for i in comb:
    print(i)

my_list=['a','b','c','1','2','3']
length=len(my_list)//2
new_dict={}
for i in range(length):
     new_dict[my_list[i]]=my_list[i+length]
print(new_dict)     


test_list = ['Gfg is good for learning', 'Gfg is for geeks', 'I love G4G']
new_list=[]
k="l"
for i in test_list:
    new_list.append(i.split())            #To filter words starting from k
for i in new_list:
    for j in i:
        if j[0]==k:
            print(j)
#Using list comprehension
res=[j for i in test_list for j in i.split() if j[0].lower()==k.lower()]
print(res)




test_list = ['gfgisbest', 'geeks', 'gfgfreak', 'gfgCS', 'Gcourses']
sub_str='gfg'
count=0
length=len(sub_str)
for i in test_list:
    if i[:length]==sub_str:
        count+=1
print(f"The frequency of {sub_str} in test_list is {count}")        


test_list2 = ['Gfg is best', 'for Geeks', 'Preparing']
res=[]
for k in test_list2:
    sub=k.split()
    res.extend(sub)
print(res)        

test_list = ['G', 'F', 'G', 'I', 'S', 'B', 'E', 'S', 'T']
repl_chr = '*'
ret_chr = 'G' 
for i in range(len(test_list)):
    if test_list[i]=='G':
        pass
    else :
        test_list[i]='*'
print(test_list)        

test_list = [[4, 1, 6], [7, 8], [4, 10, 8]]
for i in test_list:
    i.sort(reverse=True) 
    print(i)
res=[sorted(i,reverse=True) for i in test_list]
print(res)
        
test_list2 = ['Gfg', 'is', 'best', 'for', 'Geeks']
res=",".join(test_list2)
res=res.replace("G","e").replace("e","G").replace("_","e").split(",")
print(res)


test_list3 = ['geekforgeeks', 'is', 'best', 'for', 'geeks']
K = 21
                                                              #To find the kth index of the word
result=[]
for sub in enumerate(test_list3):
    for ele in enumerate(sub[1]):
       result.append(ele[0])

print(result[22])  

#Using list comprehension
res_list=[j[0] for i in enumerate(test_list3) for j in enumerate(i[1])]
print(res_list[21])


class Person:
    def __init__(self,name,id,adress):
        self.name=name
        self.id=id
        self.address=address

    def display(self):
        print(self.name)
        print(self.id)
        print(self.address)
        #print(self.number)

class Employee(person):
    def __init__(self,name,id,number,address):
        self.name=name
        self.id=id
        self.number=number
        self.address=address
        Person.__init__(self,name,id,address,number)  #Invoking the init of the parent class

empobj=Employee("sri",20217,52,"chennai")
empobj.display()

new_list=[1,2,34,5]
res=iter(new_list)
print(next(res))
print(next(res))
# new_list=[76,3,42,23,456,7,8,90]
# res=list(filter(lambda a: a%2!=0,new_list))
# print(res)

ages=[12,45,34,21,15,17,23]
res=list(filter(lambda age:age<18,ages))
print(res)


# print(list(map(lambda age:age+age,ages)))

# from functools import reduce
# li=[5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
# res1=reduce((lambda x,y: x+y),li)    #in reduce lambda takes two arguments
# print(res1)

# new_li=["doggy","catty","puppy"]
# result=list(map(lambda str: str.upper(),new_li))
# print(result)

# alf="abcdf"
# print("Some alphabets are {}".format(alf),end="")
# print("ghikj")

# import functools
# lis1=[1,3,4,8,9,1,5,7]                   #To find the largest number
# print(functools.reduce((lambda x,y: x if x>y else y),lis1))

# pow_list=[2,4,5,7,9]
# cube=map(lambda x:pow(x,2),pow_list)
# print(list(cube))

# try: 
#     import pandas as pd
#     df=pd.DataFrame({'Name':['sriram','varsha'],'age':[23, 19]})
# except Exception as Error:
#     pass


# map_list=[1,-2,4,-5,7]
# print(list(map(abs,map_list)))

# x=lambda : "Hello world"      #lambda function without any argument
# print(x())                      

lis=[11, 12, 14, 13, 13, 15, 14]
len=len(lis)
idx5=lis[4]
count=0
for j in lis:
    if j==idx5:
        count+=1

if len==8 and count==3:
    print("True")
else:
    print("False")   
'''for i in range(5):
   print(i**2)'''
'''giv_list=[2,3,6,5]
max=giv_list[0]
for i in range(1,len(giv_list)):
    if giv_list[i]>max:
       max=giv_list[i]
giv_list.remove(max)
max=giv_list[0]                           #find second largest number  
for j in range(len(giv_list)):
     if giv_list[j]>max:
       max=giv_list[j]
print("The second largest number is {}".format(max))'''

'''i=0
while i<5:
    i+=1
    print(i)
else:
    print("Im done")'''
my_list=[1,3,5]
n=len(my_list)
i=0
while i < n:
    if my_list[i] % 2 == 0:
        print("I\'m even number")
        break
    i+=1
else:
    print("Im odd number")
def contains_even_number(l):
	
	n = len(l)
	i = 0
	while i < n:
		if l[i] % 2 == 0:
			print("list contains an even number")
			break
		i += 1

	# This else executes only if break is NEVER
	# reached and loop terminated after all
	# iterations
	else:
		print("list does not contain an even number")

# Driver code
print ("For List 1:")
contains_even_number([1, 9, 8])
print (" \nFor List 2:")
contains_even_number([1, 3, 5])


x=20
count=0
for i in range(1,x+1):
    if not x%i:
        count+=1
print(count)

import re
"""mob=int(input("Enter : "))
r=re.search("^[789]\d{9}$",str(mob))
if r:
    print("Valid mobile number")
else:
    print("Invalid number")    
"""
txt="H123"
ans=re.search("^H\d{3}$",txt)
print(ans.string)
first_3=8
last_3=6
diff=last_3-first_3
list_len=6
divider=(list_len-6)+1
common_difference=diff//divider
starting_dig=first_3-(2*common_difference)
list2=[]
for i in range(list_len):
    list2.append(starting_dig)
    starting_dig+=common_difference
print(list2)    


print("data")

import mysql.connector
mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="9600pdsv"
        )
print(mydb)

print("Hello world")
n=10
for i in range(n):
    if i is 0:
        print("Current number: {} Previous number: {} Sum: {}".format(0,0,0))
    else:
        prev=i-1
        sum=prev+1
        print("Current number: {} Previous number: {} Sum: {}".format(i,prev,sum))

for row in range(1,6):
    for col in range(row):
        print(row,end="")
    print()    
n=832647

while n>0:
    rem=n%10
    n=n//10
    print(rem,end="")
print()


num=2992
temp=num
res=""
while num>0:
    r=num%10
    num=num//10
    res+=str(r)

if int(res)==temp:
    print("Palindrome")
else:
    print("Not a palindrome")     
list1=[[2,3,4,7],[8,4,30,3,87],[56,7,34,1,23]]
new_list=[sorted(i) for i in list1]
for i in new_list: 
    print(i[len(i)-2])
print(new_list) 

gl=[5,5,3,2,8,2]
length=len(gl)
for i in range(length):
    if i<length-1:
        for j in range(i+1,length):
            if gl[i]>gl[j]:
                gl[i],gl[j]=gl[j],gl[i]
print(gl)                

import mysql.connector

mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="8428"
        )
print(mydb)


ip="10.10.278.1"
l=ip.split(".")

for i in l:
    if int(i)>255:
        print("Invalid IP")
        break
else:
    print("valid IP")    
a=3
total=0
for i in range(a):
	str_temp=""
	for j in range(i+1):
		str_temp+=str(a)
	print(str_temp)
	total+=int(str_temp)
print(total)

