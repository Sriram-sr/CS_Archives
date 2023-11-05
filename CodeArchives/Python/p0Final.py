def OuterFunction(function_to_execute):
    def innerFunc(*args):
        print('Before execution')
        print(function_to_execute(*args))
        print('after execution')
    return innerFunc

@OuterFunction
def findFactorial(num):
    val = 1
    while num>0:
        val*=num
        num-=1
    return val  

findFactorial(5)   


import re

txt="perlrlrlrlABCrl"

regex=re.match(r"perl(rl)*ABC\1",txt)
print(regex)

txt="""php code
python code
java code
c stack
php     code"""

reg=re.findall("[a-z]+\s(?=code)",txt) # lookup assertion
print(reg)

txt="""file.txt
file.pdf
file.pkt
file_fyt"""

reg=re.findall(r"\w+(?=\.\w{3})",txt)
print(reg)
import json
txt= '{ "name":"John", "age":30, "city":"New York"}'

# so loads is used when you read a file as text and loads into python dictionary
retrieved_as_json=json.loads(txt)
print(type(retrieved_as_json))  # dictionary
# print(retrieved_as_json["age"])

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

retrieved_as_json=json.dumps(x,indent=4,separators=",=")
#This is dumping the python format into json string format
print(type(retrieved_as_json))

with open("json_file.json","w") as json_file:
    json_file.write(retrieved_as_json)



res=["abc","def","ghc"]

res=['1','2','3','4','5']
ans=list(map(int,res))
print(ans)
print(type(ans[1]))

test_list1 = ['Gfg', 'is', 'best']
test_list2 = [0, 1, 2, 1, 0, 0, 0, 2, 1, 1, 2, 0]

result = list(map(lambda x : test_list1[x],test_list2))
print(result)

res=["abc","def","ghc"]
result = list(map(lambda x : len(x),res))
print(result)

def User_Defined(number):
    return str(number)[::-1]

#List elements contains numbers which have to be reversed
List = [3345,92746,73298,9273,8899]
# result = list(map(User_Defined,List))
result = list(map(lambda x : str(x)[::-1],List))
print(result,True)

a = [1,2,3]
b = [1,2,3]   #To add the two list elements

result = list(map(lambda x,y : x+y,a,b))
print(result)

List_Every_Char = ['sweet','dreams','hello','world']
result = list(map(list,List_Every_Char))
print(result)

new_list = [2,3,4,5,[6],7,8,9]

result = list(map(lambda val : val*val,new_list))

print(result)

greater_than_5 = list(filter(lambda val : val >5,new_list))

print(greater_than_5)

val1,val2,val3 = map(int ,input('Enter values line : ').split())
# To get the numbers as input for three values given in a single line
print(val1,val2,val3)

res=[]
test_list = ["geeks", "for", "geeks", "is", "best"]
for i in test_list:
    i=i[::-1]
    res.append(i)

# print(res)    

res=list(map(lambda x: x[::-1],test_list))
print(res)


from click import version_option


sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

def checkVowel(char):
    vowelList = ['a', 'e', 'i', 'o', 'u']
    if char in vowelList:
        return True
    return False

output = filter(checkVowel, sequence)
ans = [i for i in output]
print(ans)

lis=[2,-1,3,4,-8,-4,-1]
res=tuple(filter(lambda x:x>=0,lis))  #can filter those search in a list or tup, or set
print(res)

new_list=[5,6,9,7,2,[],66,37,8,[],8,[],15]
new_res=list(filter(None,new_list))
print(new_list)

test_list = ['GeeksforGeeks', 'Geeky', 'Computers', 'Algorithms']

sub='Geek'

res=list(filter(lambda x:sub in x,test_list))
print(res)


import json

sample_txt = '''{
    "name": "jane doe",
    "salary": 9000,
    "skills": [
        "Raspberry pi",
        "Machine Learning",
        "Web Development"
    ],
    "email": "JaneDoe@pynative.com",
    "projects": [
        "Python Data Mining",
        "Python Data Science"
    ]
}'''

# This is just loads the json_text into python dictionary
json_object = json.loads(sample_txt)


# To directly load from json file into dictionary by reading the file
with open('sample_json.json','r') as json_file :
    # temp_read_content = json_file.read()  # if you read the file it wont load
    workable_dict = json.load(json_file)
    print(workable_dict)
print(workable_dict['skills'])    
import logging

logging.basicConfig(filename='test_file.log',level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')

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

logger = logging.getLogger()
logger.setLevel(logging.ERROR)

logger.debug("Result for addition of {} and {} is {}".format(x,y,add_result))
logger.debug("Result for subtraction of {} and {} is {}".format(x,y,sub_result))
logger.debug("Result for multiplication of {} and {} is {}".format(x,y,mul_result))
logger.debug("Result for division of {} and {} is {}".format(x,y,div_result))


import utils.util

print("About to do something cool!")
utils.util.doSomethingCool()
import json

new_dict = {'key1':'value1','key2':'value2'}

 # This is the step to write into json file  ( Using dump )
# with open('new_file.json','w') as json_dump_file :
#     json.dump(new_dict,json_dump_file)

 # This is the step to create the json object and write into json file ( Using dumps )
json_object = json.dumps(new_dict,indent = 4,separators= ',=')

with open('json_object_write_file.json','w') as json_f :
    json_f.write(json_object)



#Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0)

import re
str="!@$%^&*(*^%^%$#"
regex=re.compile(r"[^a-zA-Z0-9]")
res=regex.search(str)
if res:
    print("True")
else:
    print("False")

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
    target_file = 'class_concepts.py'  # Replace with the desired merged file name

    merge_files_in_subfolders(main_folder, target_file)

import re

pattern = '^a...s$'
test_string = 'abyss'
result = re.match(pattern, test_string)
print(result)
if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")	


ns="Heab wocarld of pcctaon"
res=re.findall(r"[^abc]",ns)
print(res)

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


import re
str="100,000,000.000"
str=str.replace(".",",")
ans=re.split(",",str)
for i in ans:
    print(i)    
import re
str='Geeksforgeeks'
x=re.findall('e',str)  #return list of matches
print(x)

x=re.findall('j',str)  #return [] as there is no match
print(x)

x=re.search('e',str)  #Return the starting index of matching word
print(x.start())

x=re.search('j',str)    #Return none as there is no match
print(x)

x=re.search('ee',str)   #Return the span of index of the match
print(x.span()) 

print(x.string)     #will return the exact string 

x=re.split('e',str)
print(x)

str='geeks for geeks is best'
x=re.split(' ',str,2)
print(x)

x=re.sub('e','z',str,2)  #replace on 2 occurances
print(x)





import re
line="We are the citezen from India"
regex=re.compile("[a-z]rom")
match=regex.sub("of",line)
print(match)

line="""Vijay 
is 
a 
boy
"""
regex=re.compile("\n")
match=regex.sub(" ",line)
print(match)

ph="044-2248-4998"

if re.search(r"\w{3}-\w{4}-\w{4}",ph):    #You can also \d instead \w
    print("Valid")
else:
    print("Invalid")   

fullname="Mahendra Dhoni"
if re.search(r"\w{2,15}\s\w{2,20}",fullname):
    print("name valid")     


phone = "2004-959-559 # This is Phone Number boy"

mat=re.sub(r"#.*$","",phone)
print(mat)

ans=re.sub(r"\D","",mat)
print(ans)

ans=re.sub(r"Ma.* ","Ms ",fullname)
print(ans)
import re
line="pet:cat dog bat"
match=re.search(r"pet:\w\w",line)
print(match)

line="Welcome to faceprep and the mall"
match=re.search("faceprep",line)
if match:
    print("Found")
else:
    print("Not found")

line="vijay k123mar and ajith bro"
if re.search(r"k\d{3}m",line)!=None:
    print("Digit found")
else:
    print("NOt found")              

#Date month using match and group
def display(string):
    match=re.match("([a-zA-Z]+) (\d+)",string)
    print("Month: ",match.group(1))
    print("Date: ",match.group(2))

str="June 09"
display(str) 

line="There are guys like sri is 21 and vijay is  22 also hanish is  20 so we can come up with this"
ages=re.findall(r"\d{1,3}",line)
print(ages)

line="we need to inform him with the latest information"
match=re.findall(r"inform",line)
print(match)

line="We are the citezen from India"
regex=re.compile("[a-z]rom",line)
match=regex.sub("of",line)
print(match)
import re
line="pet:cat dog bat"
match=re.search("pet",line)
print(match)

letter_string=[chr(asci) for asci in range(65,91)]*3
print(letter_string)
order=7
matrix_result=[[" " for column in range(order)] for row in range(order)]
print(matrix_result)
letter_index=0
row_pos=0
col_pos=0
#for m in range(3):
while(order>0):
	for loop in range(4):
		if(loop==0):
			print(order)
			for box in range(order):
				print(row_pos,col_pos)
				if(letter_index<len(letter_string)):
					matrix_result[row_pos][col_pos]=letter_string[letter_index]
					letter_index+=1
				col_pos+=1
			col_pos-=1
			row_pos+=1
			order-=1
		elif(loop == 1):
			print(order)
			for box in range(order):
				print(row_pos,col_pos)
				if(letter_index<len(letter_string)):
					matrix_result[row_pos][col_pos]=letter_string[letter_index]
					letter_index+=1
				row_pos+=1
		elif(loop == 2):
			print(order)
			col_pos-=1
			row_pos-=1
			for box in range(order):
				print(row_pos,col_pos)
				if(letter_index<len(letter_string)):
					matrix_result[row_pos][col_pos]=letter_string[letter_index]
					letter_index+=1
				col_pos-=1
			order-=1
		elif(loop == 3):
			print(order)
			#print(row_pos)
			row_pos-=1
			col_pos+=1
			for box in range(order):
				print(row_pos,col_pos)
				if(letter_index<len(letter_string)):
					matrix_result[row_pos][col_pos]=letter_string[letter_index]
					letter_index+=1
				row_pos-=1
	row_pos+=1
	col_pos+=1
	print(order,"order")

for row in matrix_result:
	print(row)
import re
str="Hello world "
x=re.findall("H.*o",str)
print(x)
import re

str='examples for meta characters in regular expression'
x=re.findall('[for]',str) #returs any one of charactres in 'for'
print(x)

x=re.findall('[^in]',str)
print(x)   #returns all characters except 'in'
x=re.findall('^ex',str)   #returns the same pattern if it starts with that and [] if not
print(x)
    
x=re.findall('expression$',str) #returns same if ends with pattern and [] if not
print(x)

x=re.findall('exp....',str)
print(x)  #returns 'expres' as 3 dots followed 'exp' 

x=re.findall('..ta',str)
print(x)    #returns 'meta'

str2='Friend in need is a friend indeed'
x=re.findall('in*',str2) #returns in 0 or more occurances
print(x)

x=re.findall('ed+',str2)
print(x)  #returns 1 or more occurances of 'ed'

x=re.findall('e{2}',str2) #returns 'ee' in number of occations
print(x)

x=re.findall('\s',str)
print(x)

x=re.findall('\S',str)
print(x)

new_str='I have 31mangoes'
x=re.findall('\d',new_str)
print(x)

x=re.findall('\D',new_str)
print(x)

x=re.findall('\w',new_str) #returns all word charactres including digits except spaces
print(x)

x=re.findall('\W',new_str)
print(x)   #returns only spaces

x=re.findall('[31]',new_str)
print(x)  #returns '3', '1' as any one of digits

x=re.findall('[^1]',new_str) #returns except 1 
print(x)

x=re.findall('[0-9][0-9]',new_str)
print(x)

x=re.findall('[A-Z]',new_str)
print(x)








import re
str='Welcome to the world of colours'
x=re.findall('[o?]',str)  #returns 'o' in 0 ar 1 occurances
print(x)

new='There are different animals cat,rat,fat,mat,sat etc.,'
animal=re.findall('[crfms]at',new)
for i in animal:
    print(i)

an=re.findall('[c-mC-M]at',new)
for j in an:
    print(an)
    
an=re.findall('[^Cr]at',new)
print(an)

new_str="my self and you's is true"  #r stands for raw string
x=re.findall(r"'s",new_str)
print(x)    

new_str="He completed I.A.S in the M.K.R IAS academy"
x=re.findall(".\..\..",new_str) #. means any character \ for escape 
print(x)

new_str="""welcome
to add
three lines"""
x1=re.compile("\n")
new_str=x1.sub('',new_str)
print(new_str)
         
phnum="044-254-2555"
if re.search("\w{3}-\w{3}-\w{4}",phnum):
    print("It is phone number")
         
if re.search("\w{2,20}\s\w{2,20}","Harley Davinson"):
    print("Yes it is valid full name")         
         
def reverse_a_number(num):
    ans=0
    while num>0:
        rem=num%10
        ans=(ans*10)+rem
        num=num//10

    return ans


n=1750
print(reverse_a_number(n))

def sort_by_keys(dict):
    new_list=[key for key in dict.keys()]
    new_list.sort()
    res={key : new_dict[key] for key in new_list}
    return res


new_dict={1:"Vijay",3:"Sri",5:"Kohli",2:"Ajith",4:"Sachin"}

print(sort_by_keys(new_dict))

def return_multiple():
    for i in range(100):
        if i%2==0:
            yield i
    yield i        

for j in return_multiple():
    print(j)            
import socket 

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_address = 'localhost'

port = 9555

client.connect((server_address,port))

while True :
    received_data = client.recv(500).decode()
    if received_data == "bye" :
        break
    print(f"Server : {received_data}")
    client_message = input("Client :")
    client.send(client_message.encode())

# Import socket module
import socket


def Main():
	# local host IP '127.0.0.1'
	host = '127.0.0.1'

	# Define the port on which you want to connect
	port = 12345

	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	# connect to server on local computer
	s.connect((host,port))

	# message you send to server
	message = "shaurya says geeksforgeeks"
	while True:

		# message sent to server
		s.send(message.encode('ascii'))

		# message received from server
		data = s.recv(1024)

		# print the received message
		# here it would be a reverse of sent message
		print('Received from the server :',str(data.decode('ascii')))

		# ask the client whether he wants to continue
		ans = input('\nDo you want to continue(y/n) :')
		if ans == 'y':
			continue
		else:
			break
	# close the connection
	s.close()

if __name__ == '__main__':
	Main()

# import socket programming library
import socket

# import thread module
from _thread import *
import threading

print_lock = threading.Lock()

# thread function
def threaded(c):
	while True:

		# data received from client
		data = c.recv(1024)
		if not data:
			print('Bye')
			
			# lock released on exit
			# print_lock.release()s
			break

		# reverse the given string from client
		data = data[::-1]

		# send back reversed string to client
		c.send(data)

	# connection closed
	c.close()


def Main():
	host = ""

	# reserve a port on your computer
	# in our case it is 12345 but it
	# can be anything
	port = 12345
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host, port))
	print("socket binded to port", port)

	# put the socket into listening mode
	s.listen(5)
	print("socket is listening")

	# a forever loop until client wants to exit
	while True:

		# establish connection with client
		c, addr = s.accept()

		# lock acquired by client
		# print_lock.acquire()
		print('Connected to :', addr[0], ':', addr[1])

		# Start a new thread and return its identifier
		start_new_thread(threaded, (c,))
	s.close()


if __name__ == '__main__':
	Main()

x = 21

def modify():
	global x
	x +=2
	print("After Changed x ", x)

modify()
print('After', x)	
import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# stream denotes it is a tcp, DGRAM denotes udp
server_address = 'localhost'  # or '127.0.0.1'
name = socket.gethostname()
print(name)
port = 9555

server.bind((server_address,port))

server.listen()

client_connection,client_address = server.accept()

print(f"Connected to client {client_address}")

while True :
    server_message = input("Server : ")
    client_connection.send(server_message.encode())
    received_data = client_connection.recv(1024).decode()
    print(f"Client : {received_data}")
    # client_connection.close()

lis=[19,3,4,5,19,23,5,3,5]
print(lis.count(5))
count_19=0
count_5=0
for i in lis:
    if i==19:
        count_19+=1
    elif i==5:
        count_5+=1
if count_19==2 and count_5>=3:
    print("True")
else:
    print("False")                
num=1001
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

new_list=[1,2,34,5]
res=iter(new_list)
print(next(res))
print(next(res))
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
n=5
for i in range(n*2):
	if(i<=((2*n)/2)):
		print('*'*(i+1))
	else:
		print("*"*((2*n)-i))

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
import threading
import queue
from time import sleep

Enqueue = queue.Queue()
event = threading.Event()

def fun_1():
    new_list = [1,2,3,45,6]
    Enqueue.put(len(new_list))
    for val in new_list :
         Enqueue.put(val)
         event.wait()

def fun_2():
    length=Enqueue.get()
    while length > 0:
        print(Enqueue.get())
        event.set()
        length-=1

prcs_1 = threading.Thread(target = fun_1)
prcs_2 = threading.Thread(target = fun_2)

prcs_1.start()
prcs_2.start()

prcs_1.join()
prcs_2.join()


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

import queue

common_queue = queue.Queue()

nl=[2,3,445,5,3]

for val in nl :
    common_queue.put(val)

for val in range(len(nl)):
    print(common_queue.get())
    
rev_queue = queue.LifoQueue()

for val in nl :
    rev_queue.put(val)

for i in range(len(nl)) :
    print(rev_queue.get())

priority_queue = queue.PriorityQueue()

pri_list = [{1:3.5},(2,"Hello_world"),(4,True),(3,45)]

for pair in pri_list :
    priority_queue.put(pair)

while not priority_queue.empty():
    print(priority_queue.get())

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


import thread
import time

def function(thread_name,delay):
    count=0
    while True:
        time.sleep(delay)
        print("%s : %s"%(thread_name,time.ctime(time.time())))
        count+=1

try:
    _thread.start_new_thread(function,("Thread_1",1))
    _thread.start_new_thread(function,("Thread_2",2))

except Exception as error:
    pass


from ..utils import util

def doHelp(x):
    return "help {}".format(x)
print('Before import')

from .shared import helper

def doSomethingCool():
    print(helper.doHelp("Doing something cool"))

given=["eat","tea","tan","ate","nat","bat"]
temp=[]
for word_index in range(len(given)-1,0,-1):
     index=-1
     for word in given[:-1]:
          count=0
          for letter in word[word_index]:
                if len(word)==count:
                    temp.append(word)
print(temp)
                      

given=["tea","tan","ate","bat","nat","eat"]
res_list=[]
for i in given[:-1]:
    count=0
    for j in given[-1]:
        if j in i:
          count+=1
    if count==len(given[-1]):
       res_list.append(i)
print(res_list)

       

from subprocess import call
call(["ls","-a"])

import os
# Access all environment variables 
print('*----------------------------------*')
print(os.environ)
print('*----------------------------------*')
# Access a particular environment variable 
print(os.environ['HOME'])
print('*----------------------------------*')
print(os.environ['PATH'])
print('*----------------------------------*')

import getpass
print(getpass.getuser())

print("__________________________________________________________________")

import sys
print(sys.copyright)

lis=[19,3,4,5,19,23,5,3,5]
print(lis.count(5))
count_19=0
count_5=0
for i in lis:
    if i==19:
        count_19+=1
    elif i==5:
        count_5+=1
if count_19==2 and count_5>=3:
    print("True")
else:
    print("False")                
def two():
    for row in range(3):
        for col in range(3):
            if row==col and row!=1:
                print(f"*",end="\t")
            else:
                print(f" ",end="\t")
        print("\n")

def three():
    pass
list1=[two,three]

for i in list1:
    s=i+"()"

n=int(input("Enter number: "))
n=str(n)
sum=0
k=1
for i in n:
    sum+=int(i)**k
    k+=1
print(sum)
if sum==n:
   print("Yes it\'s  a Disssarium")
else:
   print("NOt Dissarium")

new_matrix=[[5,8,4],[4,6,3],[55,4,21]]
temp=[]
row=len(new_matrix)
col=len(new_matrix[0])
res_matrix=[[0 for i in range(col)]for j in range(row)] 
k=0


for i in range(row):
   for j in range(col): 
       temp.append(new_matrix[i][j])                #printing original matrix

for i in range(row):
    for j in range(col-1,-1,-1):
         res_matrix[i][j]=temp[k]                  #printing mirror matrix
         k+=1
for i in range(row):
    for j in range(col):
        print(new_matrix[i][j],end="\t")                     #for printing
    print()
print()                                       

for i in range(row):
    for j in range(col):
       print(res_matrix[i][j],end="\t")
    print()      

row=int(input("number of rows: "))
col=int(input("number of columns: "))
n=1
orig_matrix=[[0 for i in range(col)] for j in range(row)]
reverse_matrix=[[0 for i in range(col)] for j in range(row)]


for i in range(row):
    for j in range(col):
        orig_matrix[i][j]=n
        n+=1
k=1	
for i in range(row):
   for j in range(col-1,-1,-1):
        reverse_matrix[i][j]=k
        k+=1
print("original matrix :\n")
for k in range(row):
     for l in range(col):
         print(orig_matrix[k][l],end="\t")
     print()
print("reverse matrix : \n")

for x in range(row):
    for y in range(col):
       print(reverse_matrix[x][y],end="\t")
    print()   

n=int(input("Enter the number of rows: "))
new_list=[[0 for i in range(n)]for j in range(n)]
count=int(n/2)+1
low=0
high=n-1
num=1
for i in range(count):
     for j in range(low,high+1):
          new_list[i][j]=num
          num+=1
     for j in range(low+1,high+1):
          new_list[j][high]=num
          num+=1
     for j in range(high-1,low-1,-1):
         new_list[high][j]=num
         num+=1
     for j in range(high-1,low,-1):
         new_list[j][i]=num
         num+=1
     low+=1
     high-=1
for i in range(n):
    for j in range(n):
        print(new_list[i][j],end="\t")
    print()

def remove(lis):
        for j in range(0,len(given_list),3):
            if given_list[j]:
                print(given_list.pop(j))
given_list=[10,30,68,44,3,88,23,5,53]
while len(given_list)>0:
       remove(given_list)

def return_multiple():
    for i in range(100):
        if i%2==0:
            yield i
    yield i        

for j in return_multiple():
    print(j)            
