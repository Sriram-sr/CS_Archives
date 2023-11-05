import os

def merge_files_in_subfolders(main_folder, target_file, encoding='utf-8'):
    try:
        with open(target_file, 'w', encoding=encoding) as target:
            for root, dirs, files in os.walk(main_folder):
                for file_name in files:
                    if file_name.endswith('.py'):
                        with open(os.path.join(root, file_name), 'r', encoding=encoding) as source_file:
                            target.write(source_file.read() + '\n')
        print('Merging successful!')
    except IOError as e:
        print('An error occurred while merging files:', str(e))


if __name__ == '__main__':
    # Get the folder of the script being executed
    script_folder = os.path.dirname(os.path.abspath(__file__))
    main_folder = script_folder  # Use the script folder as the main folder
    target_file = 'last_file.py'  # Replace with the desired merged file name

    merge_files_in_subfolders(main_folder, target_file)


import mysql.connector as mc

mydb = mc.connect(
    host='localhost',
    user= 'root',
    password= '',
    database= 'instagram',
)

cursor = mydb.cursor()
cursor.execute("select*from post_like where liked_post_id=6")
tables = cursor.fetchall()
print([i for i in tables])


import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="devsearch",
)
cursor = mydb.cursor()

cursor.execute("select*from users_profile;")
#cursor.execute("SELECT * FROM users_profile")
table_data = cursor.fetchall()
for i in table_data:
    print(i)
def rangeBitwiseAnd(left: int, right: int) -> int:
        bit_ans = 0
        for num in range(left, right+1):
            if bit_ans==0:
                bit_ans = num
            # print('before', bit_ans)    
            bit_ans&=num
            # print('after', bit_ans)    

        return bit_ans   

left = 5
right = 7
ans = rangeBitwiseAnd(left, right)        
# print(15&15)
print(ans)
input_array = [1, 2, 3, 1, 4, 5, 2, 3, 6]
k = 3
length = len(input_array)
large_num_list = []

for num in range(length-k+1):
    sub_array = input_array[num:num+k]
    large_num_list.append(max(sub_array))

print(large_num_list)

class Geek:
     # private members
     _name = 'Sri'
     __roll = 'Sroll'
     __branch = 'Sbranch'
 
 
     # private member function 
     def __displayDetails(self):
           
           # accessing private data members
           print("Name: ", self.__name)
           print("Roll: ", self.__roll)
           print("Branch: ", self.__branch)
    
     # public member function
     def accessPrivateFunction(self):
            
           # accessing private member function
           self.__displayDetails() 
 
class SubClass(Geek):
     def trigger_function(self):
          print('Calling private method')
          print(self._name)

sub_instance = SubClass()
sub_instance.trigger_function()          
s = "dog dog dog dog"
pattern = "abba"
splitted = s.split()
match_dict = dict()
flag = True

for idx in range(len(splitted)):
	if (match_dict.get(pattern[idx]) == None or match_dict.get(pattern[idx]) == splitted[idx]):
		try:
		    list(match_dict.keys())[list(match_dict.values()).index(splitted[idx])]
		except:    
		    match_dict[pattern[idx]] = splitted[idx]
	else:
	    flag = False

print(flag)


def get_prime_numbers(n):
	lesser_primes = []
    for number in range(n):
    	for small in range(2,number):
    		if number%small==0:
    			break
        else:
            lesser_primes.append(number)		
	    		
        
number = 10
primes = get_prime_numbers(number)	    	
print(primes)
	    		
# 2 1 4 17

normal_days = 2
extra_days = 1
interval = 4
find_day = 17
year = 1
days = 0
div = 1

while True:
    before = days

    if year/(interval*div)==1.0:
        days+=(normal_days+extra_days)
        div+=1
        added = extra_days
    else:
        days+=normal_days
        added = normal_days

    year+=1
    after = days   

    if find_day>before and find_day<=after:
        if added==extra_days:
            print("Yes")
        else:
            print("No")    
        break    

    
total_money = 6
person_money = [10, 8, 6, 4]
check_string = ''

for person in person_money:
    if person<=total_money:
        total_money-=person
        check_string+='1'
    else:
        check_string+='0'    

print(check_string)        
# def check_easy_pronounce():
#     pronounce_str = "polish"
#     check_margin = 4

#     vowels = ['a', 'e', 'i', 'o', 'u']

#     count = 0
#     for char in pronounce_str:
#         if char in vowels:
#             count = 0
#         else:
#             count+=1
#         if count>4:
#             print("NO")
#             break

#     print("YES")

# check_easy_pronounce()    

def check_easy_pronounce(pronounce_str):
    check_margin = 4

    vowels = ['a', 'e', 'i', 'o', 'u']

    count = 0
    for char in pronounce_str:
        if char in vowels:
            count = 0
        else:
            count+=1
        if count>4:
            print("NO")
            break

    if count<4:
        print("YES")


test_cases = int(input())
for test in range(test_cases):
    count = int(input())
    pronounce_str = input()
    check_easy_pronounce(pronounce_str)
class FpdUpgrade:
    individual_fpd_times = []
    def __init__(self, fpd_obj, fpd, location, process=None, pkg_out=None, force=False, proc_restart=False,
                     preVerify=True, postVerify=True, delay=60, retries=10, interval=60, check_led=False):
        pass             
        # if not hasattr(FpdUpgrade, 'individual_fpd_times'):
        #     individual_fpd_times = []

    def checker(self, fpd):
        print('before ', FpdUpgrade.individual_fpd_times)
        FpdUpgrade.individual_fpd_times.append(fpd)
        print('after ', FpdUpgrade.individual_fpd_times)


def call_ten_times(n):
    fpd_name = 'fpd'
    fpd = fpd_name+str(n)
    upgrade_obj = FpdUpgrade(fpd_obj='fpd_obj', location='location', fpd=fpd, force='force', pkg_out='fpd_pkg',
                                        postVerify=False, delay=0, interval=0, retries=120)
    upgrade_obj.checker(fpd=fpd)
    print("Function Job is over")                                        

for number in range(1,11):
    call_ten_times(number)
import sys

print(sys.version)
print("Hello World")
def print_fibonnaci_series(num_range):
	a = 0
	b = 1
	while num_range>0:
		print(a)
		temp = a+b
		a = b
		b = temp
		num_range-=1



# print_fibonnaci_series(10)

def prime_number(number):
	for sub in range(2, number):
		if number%sub==0:
			return 'Not a prime number'
	return 'Prime number'	

print(prime_number(7))


arr = [15, 12, 13, 10]
total = sum(arr)
print(total)
all_fpd_times = {
	'Bios': [29, '/rp0/cpu'],
	'Bootloader': [129, '/rp0/cpu'],
	'Iofpga': [18, '/rp1/cpu'],
	'x86fpga': [138, '/rp1/cpu']
}

result = ''
headers = ['LOCATION', 'FPD_NAME', 'TIME_IN_SECONDS']
result+="-"*60+"\n"
result+=f'{headers[0]: <20}{headers[1]: <20}{headers[2]}\n'
result+="-"*60+"\n"
for key, value in all_fpd_times.items():
    result+=f'{value[1]: <20}{key: <20}{value[0]}\n'
result+="-"*60+"\n"

print(result)
import os 

env_vars = os.environ.get('email')
print(env_vars)


name = 'Sriram'
age = 22

places = ['Tm', 'Spt']
data = {'mob': 223, 'ms': 11}

print(__name__)
print(globals())
arr = [2, 3, 1, 1, 2, 4, 2, 0, 1, 1] 
idx_tracker = 0
jump_count = 0

for idx in range(len(arr)):
    if idx<idx_tracker:
        continue
    else:
        idx_tracker+=arr[idx]
        print(idx_tracker)
        if not idx==len(arr)-1:
            jump_count+=1

print(jump_count)
#!/usr/bin/python3

list1 = [2,3,4,5,9]

#cube_list = list(map(lambda x: x**2, list1))

def square_it(n):
    print('im executing')
    return n**2

cube_list = list(map(square_it, list1))

print(cube_list)

competitors = list(map(int, input().split()))

high_flag = "No"

for idx in range(len(competitors)):
    competitor = competitors[idx]
    others = competitors[:idx] + competitors[idx+1:]
    others_revenue = sum(others)
    if competitor > others_revenue:
        high_flag = "Yes"
    
print(high_flag)        



def findMedianSortedArrays(nums1, nums):
        common_list = nums1 + nums2
        if len(common_list)%2==0:
            nxt_idx = len(common_list)//2
            prev_idx = nxt_idx-1
            value = (common_list[prev_idx]+common_list[nxt_idx])/2

            formatted = format(value, '.4f')
            intted = float(formatted)
            print(intted)
            
        else:
            idx = len(common_list)//2
            value = common_list[idx]

            return int(format(value, '.5f'))

nums1 = [1,2]
nums2 = [3,4]

print(findMedianSortedArrays(nums1,nums2))

# Program to find if a given number is Palindrome or not.

num = 54045
check_num = num
rev_check = 0

while num>0:
	last_num = num%10
	rev_check = rev_check*10 + last_num
	num//=10

if check_num==rev_check:
	print('It is a Palindrome')
else: 
    print('The number is not Palindrome')	

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
    target_file = 'onebyone.py'  # Replace with the desired merged file name

    merge_files_in_subfolders(main_folder, target_file)


K = 77
arr = [35, 56, 48, 21, 87]
count = 0

last_reversed_idx = -1
for i in range(len(arr)):
	count+=1
	if count%K==0:
		temp = []
		for j in range(count-1,count-K-1,-1):
			temp.append(arr[j])
		arr[count-K:count] = temp
		last_reversed_idx = count-1
	if i==len(arr)-1:
	    if count%K!=0:
	        from_idx = last_reversed_idx+1
	        temp = arr[from_idx:]
	        temp = temp[::-1]
	        arr[from_idx:] = temp

print(arr)	        




X = 5
Y = 4
string = "surprokrptkrpolpr"

total_count = 0
pr_rem_flag = False

while True:
    if 'pr' in string:
        string = string.replace('pr','',1)
        total_count+=X
        pr_rem_flag = True

    if 'rp' in string:
        if not pr_rem_flag:
            string = string.replace('rp','',1)
            total_count+=Y
    pr_rem_flag = False
    if 'pr' not in string and 'rp' not in string:
        break


print(total_count)
    
    
string = "acccbb"
sorted_list = []
count = 0

for char in string:
	if string.count(char)>=count:
		sorted_list.insert(0,char)
		count = string.count(char)
	else:
	    sorted_list.append(char)	

print(sorted_list)			


#!/bin/zsh

def check_square(n):
    if n < 1:
        return False
    while (n % 3 == 0):
        n //= 3
    return n == 1


n = 45
print(check_square(n))

from generate.generate import Table
# array = [1,2,3,4,5,6,7,8,9,10]
array = [142, 112, 54, 69, 148, 45, 63, 158, 38, 60, 124, 142, 130, 179, 117, 36, 191, 43, 89, 107, 41, 143, 65, 49, 47, 6, 91, 130, 171, 151, 7, 102, 194, 149, 30, 24, 85, 155, 157, 41, 167, 177, 132, 109, 145, 40, 27, 124, 138, 139, 119, 83, 130, 142, 34, 116, 40, 59, 105, 131, 178, 107, 74, 187, 22, 146, 125, 73, 71, 30, 178, 174, 98, 113]

Target = 665

def sum_range():
    for idx in range(len(array)):
        # print(idx)
        flag = 0
        temp = array[idx]
        for nxt in range(idx+1,len(array)):
            # print(nxt)
            temp+=array[nxt]
            if temp==Target:
                # print('ll')
                return [idx+1, nxt+1]
                flag = 1
                break
        if flag==1:
            break  
    if flag==0:
        return -1     

print(sum_range())         

from tabulate import tabulate

table = [["FPD_NAME","TIME_IN_SECONDS"],["Bios",29],["Iofpga",120],["Bootloader", 80]]

result =  tabulate(table, headers="firstrow", tablefmt="rounded_grid")

print(result)
teams, duration, break_time = map(int, input().split())

total_time = 0

while teams>=2:
    total_time+=duration

    if teams!=2:
        total_time+=break_time

    teams = teams//2

print(total_time)    
sample_array = [7, 4, 2, 1, 16]

large_num = max(sample_array)
second_large = sample_array[0]

for num in sample_array:
    if num!=large_num:
    	if num>second_large:
    		second_large = num

print(second_large)    		
from functools import reduce

class Student:
    def __init__(self, name, marks_english, marks_maths):
        self.name = name
        self.marks_english = marks_english
        self.marks_maths = marks_maths

students = [
    Student("John", 80, 90),
    Student("Jane", 85, 95),
    Student("Jim", 75, 92),
    Student("Jill", 70, 88)
]

# Use the reduce function to find the student with the highest marks in mathematics
highest_marks_student = reduce(lambda x, y: x if x.marks_maths >= y.marks_maths else y, students)

print(f"The student with the highest marks in mathematics is {highest_marks_student.name}")

def triplet_sum1(arr):
    found = False
    n = len(arr)
    loop_count = 0

    for i in range(n-2):   #0
        for j in range(i+1,n-1): #1
            for k in range(j+1,n): #2 
                loop_count+=1
                if arr[i]+arr[j]+arr[k]==0:
                    print(i,j,k)
                    found = True
    print(loop_count)
    if not found:
        print("Not exists")

def triplet_sum2(arr):
    n = len(arr)
    uniques = set()
    for i in range(n-1):
        for j in range(n):
            check_num = -(arr[i]+arr[j])
            if check_num in uniques:
                print(check_num, arr[i], arr[j])
            else:
                uniques.add(arr[j])

# Python3 program to find triplets
# in a given array whose sum is zero

# function to print triplets with 0 sum


def findTriplets(arr, n):
	found = False
	for i in range(n - 1):

		# Find all pairs with sum
		# equals to "-arr[i]"
		s = set()
		for j in range(i + 1, n):
			x = -(arr[i] + arr[j])
			if x in s:
				print(x, arr[i], arr[j])
				found = True
			else:
				s.add(arr[j])
	if found == False:
		print("No Triplet Found")

# arr = [-0, -1, 2, -3, 1]
# findTriplets(arr,len(arr))
# triplet_sum2(arr)

# python program to find triplets in a given
# array whose sum is zero

# function to print triplets with 0 sum


def findTriplets(arr, n):

	found = False

	# sort array elements
	arr.sort()

	for i in range(0, n-1):

		# initialize left and right
		l = i + 1
		r = n - 1
		x = arr[i]
		while (l < r):

			if (x + arr[l] + arr[r] == 0):
				# print elements if it's sum is zero
				print(x, arr[l], arr[r])
				l += 1
				r -= 1
				found = True

			# If sum of three elements is less
			# than zero then increment in left
			# elif (x + arr[l] + arr[r] < 0):
			# 	l += 1

			# # if sum is greater than zero then
			# # decrement in right side
			else:
				r -= 1

	if (found == False):
		print(" No Triplet Found")

def checkThis(arr, n):
    for i in range(n-1):
        x = arr[i]
        l = i+1
        r = n-1

        while l<r:
            if x+arr[l]+arr[r]==0:
                print(x, arr[l], arr[r])
            l+=1
            r-=1    
# Driven source
arr = [-5,-2,3,-1,-1,0,5]
n = len(arr)
checkThis(arr, n)

# This code is contributed by Smitha Dinesh Semwal


arr = [11,3,7,9,14,2]
hash_map = {}
target = 18

for idx in range(len(arr)):
	check = target-arr[idx]
	value = hash_map.get(check)
	if value!=None:
	else:
	    hash_map[arr[idx]] = idx





class Alarm:
    def __init__(self, *args, **kwargs):
        print('eneterd')
        self.location = None
        self.type = 'alarm'
        self.severity = None
        self.group = None
        self.set_time = None
        self.description = None

    def show(self):
        print(self.location)    

alarm = Alarm()

alarm.show()
def printNos(N):
        #Your code here
        if N==0:
            return 
        printNos(N-1)
        print(N,end=' ')

printNos(10)
import os
import json

def read_from_json(filename):
    if os.path.isfile(filename):
    	with open(filename, 'r') as read_file:
    		# file_content = read_file.read()
    		# read_content = json.loads(file_content)
    		read_content = json.load(read_file)
    return read_content

filename = 'json_file.json'
read_content = read_from_json(filename)
print(read_content)

read_content = x = {
  "name": "John",
  "age": 30,
  "city": "New York",
  "place": "same as city"
}

def write_to_json(content, filename):
	with open(filename,'w') as write_file:
		# write_file.write(json.dumps(content))
		json.dump(content, write_file)

write_to_json(read_content, 'new_json.json')
		



# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

# first = Node(1)
# llist = LinkedList()
# llist.head = first
# print(llist.head.data)  
# print(first.data)

'''The above code is for creating a linked list with single node'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

llist = LinkedList()
llist.head = Node(1)
first = Node(1)
print(llist.head.data)
second = Node(2)
llist.head.next = second
llist.first.next = second
print(llist.first.next)
print(second.data)



class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

first = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
first.next = second
second.next = third
third.next = fourth
fourth.next = first

second_location = id(first.next.data)
print(second_location)

def getNodeData(node):
    return node.data

def getNxtNodeData(node):
    return node.next.data

print(getNxtNodeData(fourth))        
  



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
    target_file = 'twobyone.py'  # Replace with the desired merged file name

    merge_files_in_subfolders(main_folder, target_file)

from dataclasses import dataclass


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printLinkedList(self):
        temp = ll.head
        while temp:
            print(temp.data)    
            temp = temp.next


ll = LinkedList()
ll.head = Node(1)
second = Node(2)
third = Node(3)                
ll.head.next = second
second.next = third
ll.printLinkedList()



