
numbers = int(input('Enter number to check: '))

for number in range(numbers):
    for num in range(2, number):
        if number%num == 0:
            break
    else:
        print(number)

import mysql.connector as sql

db = sql.connect(
    host = 'localhost',
    user = 'root',
    password = 'sriram'
)

cursor = db.cursor()
cursor.execute('use store;')

def show_customers():
    cursor.execute('select*from customer;')
    result = cursor.fetchall()
    for customer in result:
        print(customer)

def add_customer():
    name = input('Enter your name: ')
    mobile = input('Enter your mobile number: ')
    cursor.execute('select*from customer;')
    result = cursor.fetchall()
    id = result[-1][0] + 1
    query = 'insert into customer (id, name, mobile) values (%s, %s, %s)'
    values = (id, name, mobile)
    cursor.execute(query, values)
    db.commit()
    print('Successfully added')

def show_products():
    cursor.execute('select*from product')
    all_products = cursor.fetchall()
    for product in all_products:
        print(product)

def add_product():
    cursor.execute('select*from product;')
    all_products = cursor.fetchall()
    id = all_products[-1][0] + 1
    product_name = input('Enter product name: ')
    price = float(input('Enter price of product: '))
    description = input('Enter any description about product: ')
    add_query = 'insert into product (id, name, price, description) values (%s, %s, %s, %s)'
    values = (id, product_name, price, description)
    cursor.execute(add_query, values)
    db.commit()
    print('Success')

def place_order():
    mobile = input('Enter your mobile number: \n')
    cursor.execute(f'select*from customer where mobile={mobile}')    
    single_customer = cursor.fetchall()
    print(single_customer)
    customer_name = single_customer[0][1]
    customer_id = single_customer[0][0]
    print(f'Welcome {customer_name}\n')
    show_products()
    product_id = int(input("\nSelect a product from above: "))
    order_query = 'insert into orders (cid, pid) values (%s, %s)'
    values = (customer_id, product_id)
    cursor.execute(order_query, values)
    db.commit()
    print('Success')

print('Select any option')
print(
    """
    1. Show Customers
    2. Add Customer
    3. Show Products
    4. Add Products
    5. Place Order
    """
)    
user_option = int(input())
if user_option == 1:
    show_customers()
elif user_option == 2:
    add_customer()
elif user_option == 3:
    show_products()    
elif user_option == 4:
    add_product()    
elif user_option == 5:
    place_order()



    
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
import random

driver = webdriver.Chrome(executable_path="E:\Selenium\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.youtube.com/results?search_query=tamil+hit+songs")

link_list = []

one = driver.find_elements(By.ID,'video-title')
for i in one:
    link = i.get_attribute('href')
    link_list.append(link)

driver.execute_script("window.scrollTo(0, 1000);")

one = driver.find_elements(By.ID,'video-title')
for i in one:
    link = i.get_attribute('href')
    link_list.append(link)

randomLink = random.choice(link_list)
driver.execute_script(f'''window.open({randomLink},"_blank");''')

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
    target_file = 'bulkycommit.py'  # Replace with the desired merged file name

    merge_files_in_subfolders(main_folder, target_file)

import mysql.connector as mysql
db=mysql.connect(
   host="localhost",
   user="root",
   passwd="9600pdsv",
   database="real_time_shop"
   )
cursor=db.cursor()     


def sales():
    cursor.execute("select count(distinct(bill_ID)) from sales")
    K=cursor.fetchall()
    bill1_ID=K[0][0]+1
    name1=input("\nEnter your name again: ")
    def add_product(name1):
        stock_list=[]
        cursor.execute("select cust_ID from customer where name=%s",(name1,))
        cID=cursor.fetchall()
        print()
        print("\tWhich category you want?")
        print("""\n
                    1.Dairy
                    2.Fruits
                    3.Beverages
                    4.Snacks
               """)
        category=int(input("\nSelect the category: "))       
        if category==1:
            cursor.execute("select prod_ID,prod_name from product,dairy where product.prod_ID=dairy.pID")
            for i in cursor:
                print("\t\t"+str(i))
            pID=int(input("\nEnter the product you want: "))
            cursor.execute("select no_of_stocks from dairy where pID=%s",(pID,))
            stock=cursor.fetchall()
            if stock[0][0]>0:
                quantity=int(input("\nEnter the quantity of product: "))
                cursor.execute("select no_of_stocks from dairy where pID=%s",(pID,))
                stocks=cursor.fetchall()
                rem_stock=stocks[0][0]-quantity
                cursor.execute("update dairy set no_of_stocks=%s where pID=%s",(rem_stock,pID))
                cursor.execute("select price_per_unit from product where prod_ID=%s",(pID,))
                price=cursor.fetchall()
                product=quantity*price[0][0]
                query="insert into sales(bill_ID,cust_ID,prod_ID,no_of_units,price) values(%s,%s,%s,%s,%s)"
                values=(bill1_ID,cID[0][0],pID,quantity,product)
                cursor.execute(query,values)
                db.commit()
            else:
                print("Sorry the product you are selected is not available")            
        elif category==2:
            cursor.execute("select prod_ID,prod_name from product,fruits where product.prod_ID=fruits.pID")
            for j in cursor:
                print("\t\t"+str(j))
            pID=int(input("\nEnter the product you want: "))
            quantity=int(input("\nEnter the quantity of product: "))
            cursor.execute("select no_of_stocks from fruits where pID=%s",(pID,))
            stocks=cursor.fetchall()
            rem_stock=stocks[0][0]-quantity
            cursor.execute("update fruits set no_of_stocks=%s where pID=%s",(rem_stock,pID))
            cursor.execute("select price_per_unit from product where prod_ID=%s",(pID,))
            price=cursor.fetchall()
            product=quantity*price[0][0]
            query="insert into sales(bill_ID,cust_ID,prod_ID,no_of_units,price) values(%s,%s,%s,%s,%s)"
            values=(bill1_ID,cID[0][0],pID,quantity,product)
            cursor.execute(query,values)
            db.commit()    
        elif category==3:
            cursor.execute("select prod_ID,prod_name from product,beverages where product.prod_ID=beverages.pID")
            for k in cursor:
                print("\t\t"+str(k))
            pID=int(input("\nEnter the product you want: "))
            quantity=int(input("\nEnter the quantity of product: "))
            cursor.execute("select no_of_stocks from beverages where pID=%s",(pID,))
            stocks=cursor.fetchall()
            rem_stock=stocks[0][0]-quantity
            cursor.execute("update beverages set no_of_stocks=%s where pID=%s",(rem_stock,pID))
            cursor.execute("select price_per_unit from product where prod_ID=%s",(pID,))
            price=cursor.fetchall()
            product=quantity*price[0][0]
            query="insert into sales(bill_ID,cust_ID,prod_ID,no_of_units,price) values(%s,%s,%s,%s,%s)"
            values=(bill1_ID,cID[0][0],pID,quantity,product)
            cursor.execute(query,values)
            db.commit()    
        elif category==4:        
            cursor.execute("select prod_ID,prod_name from product,snacks where product.prod_ID=snacks.pID")
            for l in cursor:
                print("\t\t"+str(l))
            pID=int(input("\nEnter the product you want: "))
            quantity=int(input("\nEnter the quantity of product: "))
            cursor.execute("select no_of_stocks from snacks where pID=%s",(pID,))
            stocks=cursor.fetchall()
            rem_stock=stocks[0][0]-quantity
            cursor.execute("update snacks set no_of_stocks=%s where pID=%s",(rem_stock,pID))
            cursor.execute("select price_per_unit from product where prod_ID=%s",(pID,))
            price=cursor.fetchall()
            product=quantity*price[0][0]
            query="insert into sales(bill_ID,cust_ID,prod_ID,no_of_units,price) values(%s,%s,%s,%s,%s)"
            values=(bill1_ID,cID[0][0],pID,quantity,product)
            cursor.execute(query,values)
            db.commit()    
        
        
    def billing():
        cursor.execute("select prod_ID,cust_ID,no_of_units,price from sales where bill_ID=%s",(bill1_ID,))
        L=cursor.fetchall()
        new_list=[]
        for i in L:
            new_list.append(i)
        cursor.execute("select name from customer where cust_ID=%s",(new_list[0][1],))
        H=cursor.fetchall()
        cust_namelist=[]
        for k in H:
            cust_namelist.append(k)
        print("\n\n******************************BILL**************************************")
        print("\nCustomer name: "+cust_namelist[0][0])
        cursor.execute("select sales_date from sales where sales_id=1")
        date=cursor.fetchall()
        print("Date - {}".format(date[0][0]))
        for i in range(len(new_list)):            
            cursor.execute("select prod_name from product where prod_ID=%s",(new_list[i][0],))
            F=cursor.fetchall()
            p_name=[]
            for d in F:
                p_name.append(d[0]) 
            cursor.execute("select price_per_unit from product where prod_ID=%s",(new_list[i][0],))
            U=cursor.fetchall()
            no_of_unitlist=[]
            for u in U:
                no_of_unitlist.append(u[0]) 
            print()            
            print(p_name[0]+"---------- "+str(new_list[i][2])+"  *  "+str(no_of_unitlist[0])+"  =  "+str(new_list[i][3]))
            cursor.execute("select price from sales where bill_ID=%s",(bill1_ID,))
            total=cursor.fetchall()
            total_list=[]
            for i in total:
                total_list.append(i[0])
        print("\n                                       Total amount={}".format(sum(total_list)))
        print("                                       GST=8.52%")        
        print("\n\n**************Thank You Visit Again!******************")    
                
    while True:
        choice=int(input("\nEnter 1 to add product, 2 to exit:  "))
        if choice==1:
            add_product(name1)
        else:
            billing()
            break     
def customer_registration():
    name=input("\nEnter your name: ")
    mobile=int(input("\nEnter your number: "))
    age=int(input("\nEnter your age: "))
    gender=input("\nYour gender: ")
    query="insert into customer(name,ph_number,age,gender) values(%s,%s,%s,%s)"
    values=(name,mobile,age,gender)
    cursor.execute(query,values)
    db.commit()
    sales()
    
 
def customer_valid():
    number_list=[]
    mobile=int(input("\nEnter your mobile number: "))
    name=input("\nEnter your name: ")
    cursor.execute("select ph_number,name from customer")
    number=cursor.fetchall()
    for i in number:
        number_list.append(i[0])
        if mobile in number_list and i[1]==name:
            print("\nExisting customer")
            sales()
            break
            
    else:
        print("\n\tRegister your mobile number")
        customer_registration()        
print("\t\t\t\t\t\t\t\tWELCOME ADMIN")


def daily_turnover():
        date=int(input("\n\nEnter the date for which you need the total turnover: "))
        cursor.execute("select price from sales where sales_date=%s",(date,))
        df=cursor.fetchall()
        total=0
        for i in df:
            for j in i:
                total+=j    
        print("\nTotal amount for the date you entered is: {}".format(total))
 
def product_add():
    print("\t\nWhich category you want to add?")
    print("""\n
                     1.Dairy
                     2.Fruits
                     3.Beverages
                     4.Snacks
               """)
    category=int(input("\nSelect the category: "))       
    if category==1:
        cursor.execute("select prod_ID,prod_name from product,dairy where product.prod_ID=dairy.pID")
        for d in cursor:
            print("\t\t\t"+str(d))
        pID=int(input("\nWhich product do you want to add: "))
        quantity=int(input("\nEnter number of units you want to add: "))
        cursor.execute("select no_of_stocks from dairy where pID=%s",(pID,))
        stock=cursor.fetchall()
        add=stock[0][0]+quantity
        cursor.execute("update dairy set no_of_stocks=%s where pID=%s",(add,pID))
        db.commit()
    elif category==2:
        cursor.execute("select prod_ID,prod_name from product,fruits where product.prod_ID=fruits.pID")
        for d in cursor:
            print("\t\t\t"+str(d))
        pID=int(input("\nWhich product do you want to add: "))
        quantity=int(input("\nEnter number of units you want to add: "))
        cursor.execute("select no_of_stocks from fruits where pID=%s",(pID,))
        stock=cursor.fetchall()
        add=stock[0][0]+quantity
        cursor.execute("update fruits set no_of_stocks=%s where pID=%s",(add,pID))
        db.commit()
        
    elif category==3:
        cursor.execute("select prod_ID,prod_name from product,beverages where product.prod_ID=beverages.pID")
        for d in cursor:
            print("\t\t\t"+str(d))
        pID=int(input("\nWhich product do you want to add: "))
        quantity=int(input("\nEnter number of units you want to add: "))
        cursor.execute("select no_of_stocks from beverages where pID=%s",(pID,))
        stock=cursor.fetchall()
        add=stock[0][0]+quantity
        cursor.execute("update beveerages set no_of_stocks=%s where pID=%s",(add,pID))
        db.commit()
    elif category==4:
        cursor.execute("select prod_ID,prod_name from product,snacks where product.prod_ID=snacks.pID")
        for d in cursor:
            print("\t\t\t"+str(d))
        pID=int(input("\nWhich product do you want to add: "))
        quantity=int(input("\nEnter number of units you want to add: "))
        cursor.execute("select no_of_stocks from snacks where pID=%s",(pID,))
        stock=cursor.fetchall()
        add=stock[0][0]+quantity
        cursor.execute("update snacks set no_of_stocks=%s where pID=%s",(add,pID))
        db.commit()



def selection(): 
    print("""\n\n
    1.Add product
    2.Buy product
    3.Daily turnover
      """)     
    print("\n\nWhat are you going to do?")
    selection=int(input("\nEnter your choice : "))
    if selection==1:
        product_add()
    elif selection==2:
        customer_valid()
    elif selection==3:
        daily_turnover()
    else:
        pass        
    


while True:
    passw=input("\nEnter password to Enter: ")
    if passw=="12345":
        selection()
        break
    else:
        print("\nEnter the correct password")
            
db.close()

from unittest import installHandler


class Laptop:
    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price

    def show_details():
        print(f'The Laptop\'s name is ')    

instance1 = Laptop('Thinkpad', 'Lenovo', 45000)
instance1.show_details()
# Laptop.show_details()
import pyautogui

# Holds down the alt key
pyautogui.keyDown("alt")

# Lets go of the alt key
pyautogui.keyUp("alt")
def receive_any(arg1,*args):
    print(f'first argument is {arg1}')
    print()
    print(f'Nxt argument is {[i for i in args]}')

def receive_dicts(**kwargs):
    for i,j in kwargs.items():
        print(i,j)
        
# import array 

# new_array = array.array('i',[1,2,3,4,5])

# print(new_array)
# # new_array[6] = 120
# # new_array[2:5] = array.array('i',[12,13,14])
# print(type(new_array))
# print(new_array)

# from django.shortcuts import render
# import datetime

# Create your views here.
from datetime import datetime


import datetime

def home():
    "nothis "
    currentdate = datetime.date.today()
    print('cur ', currentdate)
    formatDate = currentdate.strftime("%d-%b-%y")
    print(formatDate)

home()

def find_max_binary_gap(num) :
    binary = bin(num).replace('0b','')
    zeros_length = []
    loop_range = len(binary) - 1
    for char in range(loop_range) :
        if binary[char] == '1' :
            temp = 0
            temp_str = binary[char+1 :]
            for zero in range(len(temp_str)) :
                if temp_str[zero] == '1' :
                    break
                else :
                    temp += 1
            if temp > 0 :        
                zeros_length.append(temp)
    print(zeros_length)

number =  25637
find_max_binary_gap(number)
from timeit import timeit

func = '''
def binary_search(array,value) :
    array = [5,9,17,23,25,45,59,63,71,89]    
    value = 25
    left = 0
    right = len(array) - 1

    while left <= right :
        mid = (left+right)//2 
        if value == array[mid] :
            return mid
            break
        elif value < array[mid] :
            right = mid - 1
        elif value > array[mid] :
            left = mid + 1  

'''

t = timeit("binary_search",setup=func)
print(t)
# print(binary_search(array,value))
# print(array.index(value))
def binary_sort(arr) :
    length = len(arr)
    for i in range(length) :
        flag = 0
        for j in range(length-1-i) :
            if arr[j] > arr[j+1] :
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                flag = 1
        if flag == 0 :
            break    
    return arr
 
arr = [3,2,6,1,13,9]
print(binary_sort(arr))
def time_elapsed(series,duration):
    elapsed_time = 0
    current_time = 0
    for attack_time in series :
        if attack_time == current_time :
            elapsed_time += 1
            continue
        else :
            current_time = attack_time + (duration - 1 )
            elapsed_time += 2    

    return f"Time elapsed until start of the attack is {elapsed_time}"            

timeSeries = [1,4,6,7,9]
duration = 2
print(time_elapsed(timeSeries,duration))
# Recursive function to find the n-th
# element of sequence
def sequence(n):
	if n == 1 or n == 2:
		return 1
	else:
		return sequence(sequence(n-1)) + sequence(n-sequence(n-1))
		
# Driver code
def main():
	n = 10
	print(sequence(n))
	
if __name__ == '__main__':
	main()




class Check:
    def __init__(self):
        print("This condtructor is called when an object is instantiated")

    def __init__(self):
        print("This is a overridden constructor")        

obj = Check()        

class Calculation1:  
    def Summation(self,a,b):  
        return a+b;  
class Calculation2:  
    def Multiplication(self,a,b):  
        return a*b;  
class Derived(Calculation1,Calculation2):  
    def Divide(self,a,b):  
        return a/b;  
obj = Derived()
print(issubclass(Calculation2,Calculation1))  

txt = "Hello"
print(isinstance(obj,Derived))
import unittest
from selenium import webdriver
from time import sleep

class SearchEnginesTest(unittest.TestCase):
    def test_Google(self):
        self.driver = webdriver.Chrome(executable_path = 'E:\Selenium\chromedriver.exe')
        self.driver.get('http://www.google.com/')
        print(self.driver.title)
        sleep(3)
        self.driver.close()
    def test_Bing(self):
        self.driver = webdriver.Chrome(executable_path = 'E:\Selenium\chromedriver.exe')
        self.driver.get('http://bing.com')
        print(self.driver.title)
        sleep(3)

if __name__ == '__main__':
    unittest.main()        
class Checker:
    cvar = 21
    
    @classmethod
    def method1(cls):
        print('this is method 1', cls.cvar)

    def method2():
        print('This is method 2')  

Checker.method1()  
Checker.method2()
import os
SECRET_KEY = os.environ['PATH']
lis = SECRET_KEY.split(';')

for i in lis:
    print(i)
class check :
    def normal():
        print("Im without self variable")
    def self_fun(self):
        print("Im a class method accessible by a instance")
  
instance = check()
check.normal()   # You can call this method only by using class name
instance.self_fun() # You can only call using instance created

print(check.__dict__)
# def club_everything(dict):
#     res_list = []
#     for key,val in dict.items() :
#         temp_list = []
#         temp_list.append(key)
#         for char in val :
#             temp_list.append(char)
#         res_list.append(temp_list)
#     return res_list  
 
# test_dict = {'gfg': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}
# print(club_everything(test_dict))

# # Alternate

# res_list = [[key] + val for key,val in test_dict.items()]
# print(res_list)

class Softwares:
    names = []
    versions = {}
    def __init__(self,names):
        if names:
            self.names = names.copy()
            for name in names:
                self.versions[name] = 1
            print(self.versions)    
        else:
            raise Exception("Please Enter the names")

p = Softwares(['S1','S2','S3'])
print(p)
# p1 = Softwares([])
# height = [1,8,6,2,5,4,8,3,7]
# max_area = 0

# for i in range(len(height)):
#     for j in range(i+1,len(height)):
#         if j<len(height):
#             # print(i,j)
#             result = min(height[i],height[j])*(j-i)
#             if result>max_area:
#                 max_area = result

# print(max_area)                

nums = [2,7,11,15]
target = 9
result = []

for i in range(len(nums)-1):
    if (nums[i] + nums[i+1]) == target:
        result.append(i)
        result.append(i+1)

print(result)        
object1 = {
    'Name': 'Sriram',
    'Age': 22
}

list1 = [2,3,4,5]
list2 = list1

list2.append(9)
list1.append(333)
print(list1[4])
print(list2)
array = [3,4,5,8,9]
resultList = []

targetValue = array[0]
resultList.append(targetValue)

for number in array:
    if number>targetValue:
        resultList.append(number)

print(len(resultList))        
def check(username, password, email):
    if not username:
        raise ValueError('set username mandatory')
    print('success')    

username = ''
password = 'loop'
email = 'srsr'

check(username=username, password=password, email=email)
def hello_decorator(func):
	def inner1(*args, **kwargs):
		
		print("before Execution")
		
		# getting the returned value
		returned_value = func(*args, **kwargs)
		print("after Execution")
		
		# returning the value to the original frame
		return returned_value
		
	return inner1


# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
	print("Inside the function")
	return a + b

a, b = 1, 2

# getting the value through return of the function
print("Sum =", sum_two_numbers(a, b))

test_dict = {'Gfg' : 3, 'is' : 7, 'best' : 10, 'for' : 6, 'geeks' : 'CS'} 
K = 7 

res = {}
for key in test_dict :
    if not (isinstance(test_dict[key],int) and test_dict[key] >= K ) :
       res[key] = test_dict[key] 

print(res)       

# Alternate 

res = {key : val for key,val in test_dict.items() if not(isinstance(val,int) and val >= 7)}
print(res)

test_list = [[2, 4, 1], [8, 1, 2], [9, 1, 10], [4, 3, 2]]
tar_list = [2, 3, 10, 7, 5, 4]

not_tar = [number for sub_list in test_list for number in sub_list if number not in tar_list]
print(not_tar)
temp_test_list = [value for sub in test_list for value in sub]

not_test = [number for number in tar_list if number not in temp_test_list]
# not_test = [number for number in tar_list for sub_list in test_list if number not in sub_list]

result = abs(sum(not_tar) - sum(not_test))

print(result)
nums = [4,3,2,7,8,2,3,1]
max_num = max(nums)
res_list = []

for num in range(1,max_num+1):
    if num in nums:
        pass
    else:
        res_list.append(num)

print(res_list)        

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

new_records = [[1], [2], [4], [5]]

def do_foo(x, y):
    print('foo', x, y)

def receive_args(*args):
    do_foo(*args)

receive_args(2,3,4)

def do_bar(s):
    print('bar', s)


# for tag, *args in new_records:
#     # if tag == 'foo':
#     #     do_foo(*args)
#     # elif tag == 'bar':
#     #     do_bar(*args)
#     print(tag)
from array import array


class DynamicArray:
    def __init__(self):
        self.array = [2,3,4]
        self.size = 1
        self.count = 3
    
    def growSize(self):
        newsize = self.size * 2
        temp = [0 for num in range(newsize)]
        for num in range(len(self.array)):
            temp[num] = self.array[num]
        self.array = temp        

    def addElement(self,num):
        if self.size == self.count:
            self.growSize()
        self.array.append(num)
        print(self.array)    

obj = DynamicArray()
obj.addElement()
row = 5
col = 5 
const = 1

for i in range(row):
    for j in range(col):
        print(const, end=" ")
        const+=1
    print()    
n = 2
count = 0
for i in range(0,100) :
    if len(str(i)) == n-1:
        count +=1
    if len(str(i)) == n :
        if str(i)[0] == str(i)[1] :
            pass
        else :
            count += 1

print(count)            
        

#!/usr/bin/python3

import os

all_env = os.environ

#for i in all_env:
#    print(f"{i}={all_env[i]}")

print(os.environ['MY_HOME'])

lis = [2,34,0]

# a= 23k

b="Hello"

# c=9s

file_path = r"C:\Users\Admin\Pictures\Camera Roll\myimage.jpg"

with open(file_path,'wb+') as img:
    for chunck in file_path.chunks():
        print(chunck)
def find_binary(num) :
    binary_text = ''
    while num >= 1 :
        val = num % 2
        binary_text += str(val)
        num = num//2 
    return binary_text[::-1]

num = 1041
print(find_binary(num))

num = 1041
binary = bin(num).replace('0b','')


def return_first(nums1,nums2):
    res_list = []
    for sub in nums1 :
        idx = nums2.index(sub)
        for nxt in nums2[idx+1:] :
            if nxt > sub :
                res_list.append(nxt)
                break
        else :
            res_list.append(-1)
    return res_list            

nums1 = [2,4]
nums2 = [1,2,3,4]

print(return_first(nums1,nums2))
def find_and_replace(test_dict,test_list,K) :
    if K in test_list :
        result = test_dict.get(K)
        return f'Exctracted value is {result}'
    else :
        return f'Key not present in the list'

test_list = ["Gfg","is", "Good", "for", "Geeks"]
K = "Gfg"
test_dict = {"Gfg" : 2, "is" : 4, "Best" : 6}

if all(K in sub for sub in [test_dict,test_list]) :
    print(True)
else :
    print(False)    


print(find_and_replace(test_dict,test_list,K))

def find_perfect_square(number) :
    number = number**0.5
    if number - int(number) == 0 :
        return True 
    else :
        return False 

number = 64
print(find_perfect_square(number))


#!/usr/bin/python3

num = 12345
res = ""

for char in str(num):
    res = char + res

print(res)    

def word_index(string_list,target):
    count = -1
    for word in string_list :
        for char in word :
            count+=1
            if count == target :
                target_word = word
                target_char = char
    # print(target_word,target_char)        
    target_index = target_word.find(target_char) 
    return f'The target index is {target_index}'           

test_list = ["geekforgeeks","python","Java"]
target = 12
print(word_index(test_list,target))

# Alternate
test_list = ["geekforgeeks", "is", "best", "for", "geeks"]
index_by_word_list = [char_index[0] for word in enumerate(test_list) for char_index in enumerate(word[1])]
print(index_by_word_list[target])

def firstElementKTime(array, k):
    match_dict = dict()
    if k==1:
        return array[0]
    flag = 0
    for idx in range(len(array)-1):
    	count = 1
    	for nxt in range(idx+1, len(array)):
    		if array[nxt]==array[idx]:
    			count+=1
    			if count>=k:
    				if array[idx] not in match_dict:
    					# flag = 1
    				    match_dict[array[idx]] = nxt
    				    break
    if flag==0:
    	return -1
    else:
        print("Nop flag")				
    
    return list(match_dict.keys())[list(match_dict.values()).index(min(match_dict.values()))]
    
array = [5,4,3,4]    
k = 3

def sortArrays(arr):

    # Finding the length of array 'arr'
    length = len(arr)

    # Sorting using a single loop
    j = 0

    while j < length - 1:

        # Checking the condition for two
        # simultaneous elements of the array
        print('bef',j)
        if (arr[j] > arr[j + 1]):

            # Swapping the elements.
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

            j = -1
        print('aft', j)    
        j += 1
   
    return arr

# Driver Code
if __name__ == '__main__':
    
    # Declaring an integer array of size 11.
    arr = [1, 2, 99, 9, 8,
        7, 6, 0, 5, 4, 3]

    # Printing the original Array.
    print("Original array: ", arr)

    # Sorting the array using a single loop
    arr = sortArrays(arr)

    # Printing the sorted array.
    print("Sorted array: ", arr)

# This code is contributed by Mohit Kumar



numbers = int(input('Enter number to check: '))

for number in range(numbers):
    for num in range(2, number):
        if number%num == 0:
            break
    else:
        print(number)

import mysql.connector as sql

db = sql.connect(
    host = 'localhost',
    user = 'root',
    password = 'sriram'
)

cursor = db.cursor()
cursor.execute('use store;')

def show_customers():
    cursor.execute('select*from customer;')
    result = cursor.fetchall()
    for customer in result:
        print(customer)

def add_customer():
    name = input('Enter your name: ')
    mobile = input('Enter your mobile number: ')
    cursor.execute('select*from customer;')
    result = cursor.fetchall()
    id = result[-1][0] + 1
    query = 'insert into customer (id, name, mobile) values (%s, %s, %s)'
    values = (id, name, mobile)
    cursor.execute(query, values)
    db.commit()
    print('Successfully added')

def show_products():
    cursor.execute('select*from product')
    all_products = cursor.fetchall()
    for product in all_products:
        print(product)

def add_product():
    cursor.execute('select*from product;')
    all_products = cursor.fetchall()
    id = all_products[-1][0] + 1
    product_name = input('Enter product name: ')
    price = float(input('Enter price of product: '))
    description = input('Enter any description about product: ')
    add_query = 'insert into product (id, name, price, description) values (%s, %s, %s, %s)'
    values = (id, product_name, price, description)
    cursor.execute(add_query, values)
    db.commit()
    print('Success')

def place_order():
    mobile = input('Enter your mobile number: \n')
    cursor.execute(f'select*from customer where mobile={mobile}')    
    single_customer = cursor.fetchall()
    print(single_customer)
    customer_name = single_customer[0][1]
    customer_id = single_customer[0][0]
    print(f'Welcome {customer_name}\n')
    show_products()
    product_id = int(input("\nSelect a product from above: "))
    order_query = 'insert into orders (cid, pid) values (%s, %s)'
    values = (customer_id, product_id)
    cursor.execute(order_query, values)
    db.commit()
    print('Success')

print('Select any option')
print(
    """
    1. Show Customers
    2. Add Customer
    3. Show Products
    4. Add Products
    5. Place Order
    """
)    
user_option = int(input())
if user_option == 1:
    show_customers()
elif user_option == 2:
    add_customer()
elif user_option == 3:
    show_products()    
elif user_option == 4:
    add_product()    
elif user_option == 5:
    place_order()



    
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
import random

driver = webdriver.Chrome(executable_path="E:\Selenium\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.youtube.com/results?search_query=tamil+hit+songs")

link_list = []

one = driver.find_elements(By.ID,'video-title')
for i in one:
    link = i.get_attribute('href')
    link_list.append(link)

driver.execute_script("window.scrollTo(0, 1000);")

one = driver.find_elements(By.ID,'video-title')
for i in one:
    link = i.get_attribute('href')
    link_list.append(link)

randomLink = random.choice(link_list)
driver.execute_script(f'''window.open({randomLink},"_blank");''')

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
    target_file = 'bulkycommit.py'  # Replace with the desired merged file name

    merge_files_in_subfolders(main_folder, target_file)

import mysql.connector as mysql
db=mysql.connect(
   host="localhost",
   user="root",
   passwd="9600pdsv",
   database="real_time_shop"
   )
cursor=db.cursor()     


def sales():
    cursor.execute("select count(distinct(bill_ID)) from sales")
    K=cursor.fetchall()
    bill1_ID=K[0][0]+1
    name1=input("\nEnter your name again: ")
    def add_product(name1):
        stock_list=[]
        cursor.execute("select cust_ID from customer where name=%s",(name1,))
        cID=cursor.fetchall()
        print()
        print("\tWhich category you want?")
        print("""\n
                    1.Dairy
                    2.Fruits
                    3.Beverages
                    4.Snacks
               """)
        category=int(input("\nSelect the category: "))       
        if category==1:
            cursor.execute("select prod_ID,prod_name from product,dairy where product.prod_ID=dairy.pID")
            for i in cursor:
                print("\t\t"+str(i))
            pID=int(input("\nEnter the product you want: "))
            cursor.execute("select no_of_stocks from dairy where pID=%s",(pID,))
            stock=cursor.fetchall()
            if stock[0][0]>0:
                quantity=int(input("\nEnter the quantity of product: "))
                cursor.execute("select no_of_stocks from dairy where pID=%s",(pID,))
                stocks=cursor.fetchall()
                rem_stock=stocks[0][0]-quantity
                cursor.execute("update dairy set no_of_stocks=%s where pID=%s",(rem_stock,pID))
                cursor.execute("select price_per_unit from product where prod_ID=%s",(pID,))
                price=cursor.fetchall()
                product=quantity*price[0][0]
                query="insert into sales(bill_ID,cust_ID,prod_ID,no_of_units,price) values(%s,%s,%s,%s,%s)"
                values=(bill1_ID,cID[0][0],pID,quantity,product)
                cursor.execute(query,values)
                db.commit()
            else:
                print("Sorry the product you are selected is not available")            
        elif category==2:
            cursor.execute("select prod_ID,prod_name from product,fruits where product.prod_ID=fruits.pID")
            for j in cursor:
                print("\t\t"+str(j))
            pID=int(input("\nEnter the product you want: "))
            quantity=int(input("\nEnter the quantity of product: "))
            cursor.execute("select no_of_stocks from fruits where pID=%s",(pID,))
            stocks=cursor.fetchall()
            rem_stock=stocks[0][0]-quantity
            cursor.execute("update fruits set no_of_stocks=%s where pID=%s",(rem_stock,pID))
            cursor.execute("select price_per_unit from product where prod_ID=%s",(pID,))
            price=cursor.fetchall()
            product=quantity*price[0][0]
            query="insert into sales(bill_ID,cust_ID,prod_ID,no_of_units,price) values(%s,%s,%s,%s,%s)"
            values=(bill1_ID,cID[0][0],pID,quantity,product)
            cursor.execute(query,values)
            db.commit()    
        elif category==3:
            cursor.execute("select prod_ID,prod_name from product,beverages where product.prod_ID=beverages.pID")
            for k in cursor:
                print("\t\t"+str(k))
            pID=int(input("\nEnter the product you want: "))
            quantity=int(input("\nEnter the quantity of product: "))
            cursor.execute("select no_of_stocks from beverages where pID=%s",(pID,))
            stocks=cursor.fetchall()
            rem_stock=stocks[0][0]-quantity
            cursor.execute("update beverages set no_of_stocks=%s where pID=%s",(rem_stock,pID))
            cursor.execute("select price_per_unit from product where prod_ID=%s",(pID,))
            price=cursor.fetchall()
            product=quantity*price[0][0]
            query="insert into sales(bill_ID,cust_ID,prod_ID,no_of_units,price) values(%s,%s,%s,%s,%s)"
            values=(bill1_ID,cID[0][0],pID,quantity,product)
            cursor.execute(query,values)
            db.commit()    
        elif category==4:        
            cursor.execute("select prod_ID,prod_name from product,snacks where product.prod_ID=snacks.pID")
            for l in cursor:
                print("\t\t"+str(l))
            pID=int(input("\nEnter the product you want: "))
            quantity=int(input("\nEnter the quantity of product: "))
            cursor.execute("select no_of_stocks from snacks where pID=%s",(pID,))
            stocks=cursor.fetchall()
            rem_stock=stocks[0][0]-quantity
            cursor.execute("update snacks set no_of_stocks=%s where pID=%s",(rem_stock,pID))
            cursor.execute("select price_per_unit from product where prod_ID=%s",(pID,))
            price=cursor.fetchall()
            product=quantity*price[0][0]
            query="insert into sales(bill_ID,cust_ID,prod_ID,no_of_units,price) values(%s,%s,%s,%s,%s)"
            values=(bill1_ID,cID[0][0],pID,quantity,product)
            cursor.execute(query,values)
            db.commit()    
        
        
    def billing():
        cursor.execute("select prod_ID,cust_ID,no_of_units,price from sales where bill_ID=%s",(bill1_ID,))
        L=cursor.fetchall()
        new_list=[]
        for i in L:
            new_list.append(i)
        cursor.execute("select name from customer where cust_ID=%s",(new_list[0][1],))
        H=cursor.fetchall()
        cust_namelist=[]
        for k in H:
            cust_namelist.append(k)
        print("\n\n******************************BILL**************************************")
        print("\nCustomer name: "+cust_namelist[0][0])
        cursor.execute("select sales_date from sales where sales_id=1")
        date=cursor.fetchall()
        print("Date - {}".format(date[0][0]))
        for i in range(len(new_list)):            
            cursor.execute("select prod_name from product where prod_ID=%s",(new_list[i][0],))
            F=cursor.fetchall()
            p_name=[]
            for d in F:
                p_name.append(d[0]) 
            cursor.execute("select price_per_unit from product where prod_ID=%s",(new_list[i][0],))
            U=cursor.fetchall()
            no_of_unitlist=[]
            for u in U:
                no_of_unitlist.append(u[0]) 
            print()            
            print(p_name[0]+"---------- "+str(new_list[i][2])+"  *  "+str(no_of_unitlist[0])+"  =  "+str(new_list[i][3]))
            cursor.execute("select price from sales where bill_ID=%s",(bill1_ID,))
            total=cursor.fetchall()
            total_list=[]
            for i in total:
                total_list.append(i[0])
        print("\n                                       Total amount={}".format(sum(total_list)))
        print("                                       GST=8.52%")        
        print("\n\n**************Thank You Visit Again!******************")    
                
    while True:
        choice=int(input("\nEnter 1 to add product, 2 to exit:  "))
        if choice==1:
            add_product(name1)
        else:
            billing()
            break     
def customer_registration():
    name=input("\nEnter your name: ")
    mobile=int(input("\nEnter your number: "))
    age=int(input("\nEnter your age: "))
    gender=input("\nYour gender: ")
    query="insert into customer(name,ph_number,age,gender) values(%s,%s,%s,%s)"
    values=(name,mobile,age,gender)
    cursor.execute(query,values)
    db.commit()
    sales()
    
 
def customer_valid():
    number_list=[]
    mobile=int(input("\nEnter your mobile number: "))
    name=input("\nEnter your name: ")
    cursor.execute("select ph_number,name from customer")
    number=cursor.fetchall()
    for i in number:
        number_list.append(i[0])
        if mobile in number_list and i[1]==name:
            print("\nExisting customer")
            sales()
            break
            
    else:
        print("\n\tRegister your mobile number")
        customer_registration()        
print("\t\t\t\t\t\t\t\tWELCOME ADMIN")


def daily_turnover():
        date=int(input("\n\nEnter the date for which you need the total turnover: "))
        cursor.execute("select price from sales where sales_date=%s",(date,))
        df=cursor.fetchall()
        total=0
        for i in df:
            for j in i:
                total+=j    
        print("\nTotal amount for the date you entered is: {}".format(total))
 
def product_add():
    print("\t\nWhich category you want to add?")
    print("""\n
                     1.Dairy
                     2.Fruits
                     3.Beverages
                     4.Snacks
               """)
    category=int(input("\nSelect the category: "))       
    if category==1:
        cursor.execute("select prod_ID,prod_name from product,dairy where product.prod_ID=dairy.pID")
        for d in cursor:
            print("\t\t\t"+str(d))
        pID=int(input("\nWhich product do you want to add: "))
        quantity=int(input("\nEnter number of units you want to add: "))
        cursor.execute("select no_of_stocks from dairy where pID=%s",(pID,))
        stock=cursor.fetchall()
        add=stock[0][0]+quantity
        cursor.execute("update dairy set no_of_stocks=%s where pID=%s",(add,pID))
        db.commit()
    elif category==2:
        cursor.execute("select prod_ID,prod_name from product,fruits where product.prod_ID=fruits.pID")
        for d in cursor:
            print("\t\t\t"+str(d))
        pID=int(input("\nWhich product do you want to add: "))
        quantity=int(input("\nEnter number of units you want to add: "))
        cursor.execute("select no_of_stocks from fruits where pID=%s",(pID,))
        stock=cursor.fetchall()
        add=stock[0][0]+quantity
        cursor.execute("update fruits set no_of_stocks=%s where pID=%s",(add,pID))
        db.commit()
        
    elif category==3:
        cursor.execute("select prod_ID,prod_name from product,beverages where product.prod_ID=beverages.pID")
        for d in cursor:
            print("\t\t\t"+str(d))
        pID=int(input("\nWhich product do you want to add: "))
        quantity=int(input("\nEnter number of units you want to add: "))
        cursor.execute("select no_of_stocks from beverages where pID=%s",(pID,))
        stock=cursor.fetchall()
        add=stock[0][0]+quantity
        cursor.execute("update beveerages set no_of_stocks=%s where pID=%s",(add,pID))
        db.commit()
    elif category==4:
        cursor.execute("select prod_ID,prod_name from product,snacks where product.prod_ID=snacks.pID")
        for d in cursor:
            print("\t\t\t"+str(d))
        pID=int(input("\nWhich product do you want to add: "))
        quantity=int(input("\nEnter number of units you want to add: "))
        cursor.execute("select no_of_stocks from snacks where pID=%s",(pID,))
        stock=cursor.fetchall()
        add=stock[0][0]+quantity
        cursor.execute("update snacks set no_of_stocks=%s where pID=%s",(add,pID))
        db.commit()



def selection(): 
    print("""\n\n
    1.Add product
    2.Buy product
    3.Daily turnover
      """)     
    print("\n\nWhat are you going to do?")
    selection=int(input("\nEnter your choice : "))
    if selection==1:
        product_add()
    elif selection==2:
        customer_valid()
    elif selection==3:
        daily_turnover()
    else:
        pass        
    


while True:
    passw=input("\nEnter password to Enter: ")
    if passw=="12345":
        selection()
        break
    else:
        print("\nEnter the correct password")
            
db.close()

from unittest import installHandler


class Laptop:
    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price

    def show_details():
        print(f'The Laptop\'s name is ')    

instance1 = Laptop('Thinkpad', 'Lenovo', 45000)
instance1.show_details()
# Laptop.show_details()
import pyautogui

# Holds down the alt key
pyautogui.keyDown("alt")

# Lets go of the alt key
pyautogui.keyUp("alt")
def receive_any(arg1,*args):
    print(f'first argument is {arg1}')
    print()
    print(f'Nxt argument is {[i for i in args]}')

def receive_dicts(**kwargs):
    for i,j in kwargs.items():
        print(i,j)
        
# import array 

# new_array = array.array('i',[1,2,3,4,5])

# print(new_array)
# # new_array[6] = 120
# # new_array[2:5] = array.array('i',[12,13,14])
# print(type(new_array))
# print(new_array)

# from django.shortcuts import render
# import datetime

# Create your views here.
from datetime import datetime


import datetime

def home():
    "nothis "
    currentdate = datetime.date.today()
    print('cur ', currentdate)
    formatDate = currentdate.strftime("%d-%b-%y")
    print(formatDate)

home()

def find_max_binary_gap(num) :
    binary = bin(num).replace('0b','')
    zeros_length = []
    loop_range = len(binary) - 1
    for char in range(loop_range) :
        if binary[char] == '1' :
            temp = 0
            temp_str = binary[char+1 :]
            for zero in range(len(temp_str)) :
                if temp_str[zero] == '1' :
                    break
                else :
                    temp += 1
            if temp > 0 :        
                zeros_length.append(temp)
    print(zeros_length)

number =  25637
find_max_binary_gap(number)
from timeit import timeit

func = '''
def binary_search(array,value) :
    array = [5,9,17,23,25,45,59,63,71,89]    
    value = 25
    left = 0
    right = len(array) - 1

    while left <= right :
        mid = (left+right)//2 
        if value == array[mid] :
            return mid
            break
        elif value < array[mid] :
            right = mid - 1
        elif value > array[mid] :
            left = mid + 1  

'''

t = timeit("binary_search",setup=func)
print(t)
# print(binary_search(array,value))
# print(array.index(value))
def binary_sort(arr) :
    length = len(arr)
    for i in range(length) :
        flag = 0
        for j in range(length-1-i) :
            if arr[j] > arr[j+1] :
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                flag = 1
        if flag == 0 :
            break    
    return arr
 
arr = [3,2,6,1,13,9]
print(binary_sort(arr))
def time_elapsed(series,duration):
    elapsed_time = 0
    current_time = 0
    for attack_time in series :
        if attack_time == current_time :
            elapsed_time += 1
            continue
        else :
            current_time = attack_time + (duration - 1 )
            elapsed_time += 2    

    return f"Time elapsed until start of the attack is {elapsed_time}"            

timeSeries = [1,4,6,7,9]
duration = 2
print(time_elapsed(timeSeries,duration))
# Recursive function to find the n-th
# element of sequence
def sequence(n):
	if n == 1 or n == 2:
		return 1
	else:
		return sequence(sequence(n-1)) + sequence(n-sequence(n-1))
		
# Driver code
def main():
	n = 10
	print(sequence(n))
	
if __name__ == '__main__':
	main()




class Check:
    def __init__(self):
        print("This condtructor is called when an object is instantiated")

    def __init__(self):
        print("This is a overridden constructor")        

obj = Check()        

class Calculation1:  
    def Summation(self,a,b):  
        return a+b;  
class Calculation2:  
    def Multiplication(self,a,b):  
        return a*b;  
class Derived(Calculation1,Calculation2):  
    def Divide(self,a,b):  
        return a/b;  
obj = Derived()
print(issubclass(Calculation2,Calculation1))  

txt = "Hello"
print(isinstance(obj,Derived))
import unittest
from selenium import webdriver
from time import sleep

class SearchEnginesTest(unittest.TestCase):
    def test_Google(self):
        self.driver = webdriver.Chrome(executable_path = 'E:\Selenium\chromedriver.exe')
        self.driver.get('http://www.google.com/')
        print(self.driver.title)
        sleep(3)
        self.driver.close()
    def test_Bing(self):
        self.driver = webdriver.Chrome(executable_path = 'E:\Selenium\chromedriver.exe')
        self.driver.get('http://bing.com')
        print(self.driver.title)
        sleep(3)

if __name__ == '__main__':
    unittest.main()        
class Checker:
    cvar = 21
    
    @classmethod
    def method1(cls):
        print('this is method 1', cls.cvar)

    def method2():
        print('This is method 2')  

Checker.method1()  
Checker.method2()
import os
SECRET_KEY = os.environ['PATH']
lis = SECRET_KEY.split(';')

for i in lis:
    print(i)
class check :
    def normal():
        print("Im without self variable")
    def self_fun(self):
        print("Im a class method accessible by a instance")
  
instance = check()
check.normal()   # You can call this method only by using class name
instance.self_fun() # You can only call using instance created

print(check.__dict__)
# def club_everything(dict):
#     res_list = []
#     for key,val in dict.items() :
#         temp_list = []
#         temp_list.append(key)
#         for char in val :
#             temp_list.append(char)
#         res_list.append(temp_list)
#     return res_list  
 
# test_dict = {'gfg': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}
# print(club_everything(test_dict))

# # Alternate

# res_list = [[key] + val for key,val in test_dict.items()]
# print(res_list)

class Softwares:
    names = []
    versions = {}
    def __init__(self,names):
        if names:
            self.names = names.copy()
            for name in names:
                self.versions[name] = 1
            print(self.versions)    
        else:
            raise Exception("Please Enter the names")

p = Softwares(['S1','S2','S3'])
print(p)
# p1 = Softwares([])
# height = [1,8,6,2,5,4,8,3,7]
# max_area = 0

# for i in range(len(height)):
#     for j in range(i+1,len(height)):
#         if j<len(height):
#             # print(i,j)
#             result = min(height[i],height[j])*(j-i)
#             if result>max_area:
#                 max_area = result

# print(max_area)                

nums = [2,7,11,15]
target = 9
result = []

for i in range(len(nums)-1):
    if (nums[i] + nums[i+1]) == target:
        result.append(i)
        result.append(i+1)

print(result)        
object1 = {
    'Name': 'Sriram',
    'Age': 22
}

list1 = [2,3,4,5]
list2 = list1

list2.append(9)
list1.append(333)
print(list1[4])
print(list2)
array = [3,4,5,8,9]
resultList = []

targetValue = array[0]
resultList.append(targetValue)

for number in array:
    if number>targetValue:
        resultList.append(number)

print(len(resultList))        
def check(username, password, email):
    if not username:
        raise ValueError('set username mandatory')
    print('success')    

username = ''
password = 'loop'
email = 'srsr'

check(username=username, password=password, email=email)
def hello_decorator(func):
	def inner1(*args, **kwargs):
		
		print("before Execution")
		
		# getting the returned value
		returned_value = func(*args, **kwargs)
		print("after Execution")
		
		# returning the value to the original frame
		return returned_value
		
	return inner1


# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
	print("Inside the function")
	return a + b

a, b = 1, 2

# getting the value through return of the function
print("Sum =", sum_two_numbers(a, b))

test_dict = {'Gfg' : 3, 'is' : 7, 'best' : 10, 'for' : 6, 'geeks' : 'CS'} 
K = 7 

res = {}
for key in test_dict :
    if not (isinstance(test_dict[key],int) and test_dict[key] >= K ) :
       res[key] = test_dict[key] 

print(res)       

# Alternate 

res = {key : val for key,val in test_dict.items() if not(isinstance(val,int) and val >= 7)}
print(res)

test_list = [[2, 4, 1], [8, 1, 2], [9, 1, 10], [4, 3, 2]]
tar_list = [2, 3, 10, 7, 5, 4]

not_tar = [number for sub_list in test_list for number in sub_list if number not in tar_list]
print(not_tar)
temp_test_list = [value for sub in test_list for value in sub]

not_test = [number for number in tar_list if number not in temp_test_list]
# not_test = [number for number in tar_list for sub_list in test_list if number not in sub_list]

result = abs(sum(not_tar) - sum(not_test))

print(result)
nums = [4,3,2,7,8,2,3,1]
max_num = max(nums)
res_list = []

for num in range(1,max_num+1):
    if num in nums:
        pass
    else:
        res_list.append(num)

print(res_list)        

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

new_records = [[1], [2], [4], [5]]

def do_foo(x, y):
    print('foo', x, y)

def receive_args(*args):
    do_foo(*args)

receive_args(2,3,4)

def do_bar(s):
    print('bar', s)


# for tag, *args in new_records:
#     # if tag == 'foo':
#     #     do_foo(*args)
#     # elif tag == 'bar':
#     #     do_bar(*args)
#     print(tag)
from array import array


class DynamicArray:
    def __init__(self):
        self.array = [2,3,4]
        self.size = 1
        self.count = 3
    
    def growSize(self):
        newsize = self.size * 2
        temp = [0 for num in range(newsize)]
        for num in range(len(self.array)):
            temp[num] = self.array[num]
        self.array = temp        

    def addElement(self,num):
        if self.size == self.count:
            self.growSize()
        self.array.append(num)
        print(self.array)    

obj = DynamicArray()
obj.addElement()
row = 5
col = 5 
const = 1

for i in range(row):
    for j in range(col):
        print(const, end=" ")
        const+=1
    print()    
n = 2
count = 0
for i in range(0,100) :
    if len(str(i)) == n-1:
        count +=1
    if len(str(i)) == n :
        if str(i)[0] == str(i)[1] :
            pass
        else :
            count += 1

print(count)            
        

#!/usr/bin/python3

import os

all_env = os.environ

#for i in all_env:
#    print(f"{i}={all_env[i]}")

print(os.environ['MY_HOME'])

lis = [2,34,0]

# a= 23k

b="Hello"

# c=9s

file_path = r"C:\Users\Admin\Pictures\Camera Roll\myimage.jpg"

with open(file_path,'wb+') as img:
    for chunck in file_path.chunks():
        print(chunck)
def find_binary(num) :
    binary_text = ''
    while num >= 1 :
        val = num % 2
        binary_text += str(val)
        num = num//2 
    return binary_text[::-1]

num = 1041
print(find_binary(num))

num = 1041
binary = bin(num).replace('0b','')


def return_first(nums1,nums2):
    res_list = []
    for sub in nums1 :
        idx = nums2.index(sub)
        for nxt in nums2[idx+1:] :
            if nxt > sub :
                res_list.append(nxt)
                break
        else :
            res_list.append(-1)
    return res_list            

nums1 = [2,4]
nums2 = [1,2,3,4]

print(return_first(nums1,nums2))
def find_and_replace(test_dict,test_list,K) :
    if K in test_list :
        result = test_dict.get(K)
        return f'Exctracted value is {result}'
    else :
        return f'Key not present in the list'

test_list = ["Gfg","is", "Good", "for", "Geeks"]
K = "Gfg"
test_dict = {"Gfg" : 2, "is" : 4, "Best" : 6}

if all(K in sub for sub in [test_dict,test_list]) :
    print(True)
else :
    print(False)    


print(find_and_replace(test_dict,test_list,K))

def find_perfect_square(number) :
    number = number**0.5
    if number - int(number) == 0 :
        return True 
    else :
        return False 

number = 64
print(find_perfect_square(number))


#!/usr/bin/python3

num = 12345
res = ""

for char in str(num):
    res = char + res

print(res)    

def word_index(string_list,target):
    count = -1
    for word in string_list :
        for char in word :
            count+=1
            if count == target :
                target_word = word
                target_char = char
    # print(target_word,target_char)        
    target_index = target_word.find(target_char) 
    return f'The target index is {target_index}'           

test_list = ["geekforgeeks","python","Java"]
target = 12
print(word_index(test_list,target))

# Alternate
test_list = ["geekforgeeks", "is", "best", "for", "geeks"]
index_by_word_list = [char_index[0] for word in enumerate(test_list) for char_index in enumerate(word[1])]
print(index_by_word_list[target])

def firstElementKTime(array, k):
    match_dict = dict()
    if k==1:
        return array[0]
    flag = 0
    for idx in range(len(array)-1):
    	count = 1
    	for nxt in range(idx+1, len(array)):
    		if array[nxt]==array[idx]:
    			count+=1
    			if count>=k:
    				if array[idx] not in match_dict:
    					# flag = 1
    				    match_dict[array[idx]] = nxt
    				    break
    if flag==0:
    	return -1
    else:
        print("Nop flag")				
    
    return list(match_dict.keys())[list(match_dict.values()).index(min(match_dict.values()))]
    
array = [5,4,3,4]    
k = 3

def sortArrays(arr):

    # Finding the length of array 'arr'
    length = len(arr)

    # Sorting using a single loop
    j = 0

    while j < length - 1:

        # Checking the condition for two
        # simultaneous elements of the array
        print('bef',j)
        if (arr[j] > arr[j + 1]):

            # Swapping the elements.
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

            j = -1
        print('aft', j)    
        j += 1
   
    return arr

# Driver Code
if __name__ == '__main__':
    
    # Declaring an integer array of size 11.
    arr = [1, 2, 99, 9, 8,
        7, 6, 0, 5, 4, 3]

    # Printing the original Array.
    print("Original array: ", arr)

    # Sorting the array using a single loop
    arr = sortArrays(arr)

    # Printing the sorted array.
    print("Sorted array: ", arr)

# This code is contributed by Mohit Kumar



numbers = int(input('Enter number to check: '))

for number in range(numbers):
    for num in range(2, number):
        if number%num == 0:
            break
    else:
        print(number)

import mysql.connector as sql

db = sql.connect(
    host = 'localhost',
    user = 'root',
    password = 'sriram'
)

cursor = db.cursor()
cursor.execute('use store;')

def show_customers():
    cursor.execute('select*from customer;')
    result = cursor.fetchall()
    for customer in result:
        print(customer)

def add_customer():
    name = input('Enter your name: ')
    mobile = input('Enter your mobile number: ')
    cursor.execute('select*from customer;')
    result = cursor.fetchall()
    id = result[-1][0] + 1
    query = 'insert into customer (id, name, mobile) values (%s, %s, %s)'
    values = (id, name, mobile)
    cursor.execute(query, values)
    db.commit()
    print('Successfully added')

def show_products():
    cursor.execute('select*from product')
    all_products = cursor.fetchall()
    for product in all_products:
        print(product)

def add_product():
    cursor.execute('select*from product;')
    all_products = cursor.fetchall()
    id = all_products[-1][0] + 1
    product_name = input('Enter product name: ')
    price = float(input('Enter price of product: '))
    description = input('Enter any description about product: ')
    add_query = 'insert into product (id, name, price, description) values (%s, %s, %s, %s)'
    values = (id, product_name, price, description)
    cursor.execute(add_query, values)
    db.commit()
    print('Success')

def place_order():
    mobile = input('Enter your mobile number: \n')
    cursor.execute(f'select*from customer where mobile={mobile}')    
    single_customer = cursor.fetchall()
    print(single_customer)
    customer_name = single_customer[0][1]
    customer_id = single_customer[0][0]
    print(f'Welcome {customer_name}\n')
    show_products()
    product_id = int(input("\nSelect a product from above: "))
    order_query = 'insert into orders (cid, pid) values (%s, %s)'
    values = (customer_id, product_id)
    cursor.execute(order_query, values)
    db.commit()
    print('Success')

print('Select any option')
print(
    """
    1. Show Customers
    2. Add Customer
    3. Show Products
    4. Add Products
    5. Place Order
    """
)    
user_option = int(input())
if user_option == 1:
    show_customers()
elif user_option == 2:
    add_customer()
elif user_option == 3:
    show_products()    
elif user_option == 4:
    add_product()    
elif user_option == 5:
    place_order()



    
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
import random

driver = webdriver.Chrome(executable_path="E:\Selenium\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.youtube.com/results?search_query=tamil+hit+songs")

link_list = []

one = driver.find_elements(By.ID,'video-title')
for i in one:
    link = i.get_attribute('href')
    link_list.append(link)

driver.execute_script("window.scrollTo(0, 1000);")

one = driver.find_elements(By.ID,'video-title')
for i in one:
    link = i.get_attribute('href')
    link_list.append(link)

randomLink = random.choice(link_list)
driver.execute_script(f'''window.open({randomLink},"_blank");''')

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
    target_file = 'bulkystuff.py'  # Replace with the desired merged file name

    merge_files_in_subfolders(main_folder, target_file)

import mysql.connector as mysql
db=mysql.connect(
   host="localhost",
   user="root",
   passwd="9600pdsv",
   database="real_time_shop"
   )
cursor=db.cursor()     


def sales():
    cursor.execute("select count(distinct(bill_ID)) from sales")
    K=cursor.fetchall()
    bill1_ID=K[0][0]+1
    name1=input("\nEnter your name again: ")
    def add_product(name1):
        stock_list=[]
        cursor.execute("select cust_ID from customer where name=%s",(name1,))
        cID=cursor.fetchall()
        print()
        print("\tWhich category you want?")
        print("""\n
                    1.Dairy
                    2.Fruits
                    3.Beverages
                    4.Snacks
               """)
        category=int(input("\nSelect the category: "))       
        if category==1:
            cursor.execute("select prod_ID,prod_name from product,dairy where product.prod_ID=dairy.pID")
            for i in cursor:
                print("\t\t"+str(i))
            pID=int(input("\nEnter the product you want: "))
            cursor.execute("select no_of_stocks from dairy where pID=%s",(pID,))
            stock=cursor.fetchall()
            if stock[0][0]>0:
                quantity=int(input("\nEnter the quantity of product: "))
                cursor.execute("select no_of_stocks from dairy where pID=%s",(pID,))
                stocks=cursor.fetchall()
                rem_stock=stocks[0][0]-quantity
                cursor.execute("update dairy set no_of_stocks=%s where pID=%s",(rem_stock,pID))
                cursor.execute("select price_per_unit from product where prod_ID=%s",(pID,))
                price=cursor.fetchall()
                product=quantity*price[0][0]
                query="insert into sales(bill_ID,cust_ID,prod_ID,no_of_units,price) values(%s,%s,%s,%s,%s)"
                values=(bill1_ID,cID[0][0],pID,quantity,product)
                cursor.execute(query,values)
                db.commit()
            else:
                print("Sorry the product you are selected is not available")            
        elif category==2:
            cursor.execute("select prod_ID,prod_name from product,fruits where product.prod_ID=fruits.pID")
            for j in cursor:
                print("\t\t"+str(j))
            pID=int(input("\nEnter the product you want: "))
            quantity=int(input("\nEnter the quantity of product: "))
            cursor.execute("select no_of_stocks from fruits where pID=%s",(pID,))
            stocks=cursor.fetchall()
            rem_stock=stocks[0][0]-quantity
            cursor.execute("update fruits set no_of_stocks=%s where pID=%s",(rem_stock,pID))
            cursor.execute("select price_per_unit from product where prod_ID=%s",(pID,))
            price=cursor.fetchall()
            product=quantity*price[0][0]
            query="insert into sales(bill_ID,cust_ID,prod_ID,no_of_units,price) values(%s,%s,%s,%s,%s)"
            values=(bill1_ID,cID[0][0],pID,quantity,product)
            cursor.execute(query,values)
            db.commit()    
        elif category==3:
            cursor.execute("select prod_ID,prod_name from product,beverages where product.prod_ID=beverages.pID")
            for k in cursor:
                print("\t\t"+str(k))
            pID=int(input("\nEnter the product you want: "))
            quantity=int(input("\nEnter the quantity of product: "))
            cursor.execute("select no_of_stocks from beverages where pID=%s",(pID,))
            stocks=cursor.fetchall()
            rem_stock=stocks[0][0]-quantity
            cursor.execute("update beverages set no_of_stocks=%s where pID=%s",(rem_stock,pID))
            cursor.execute("select price_per_unit from product where prod_ID=%s",(pID,))
            price=cursor.fetchall()
            product=quantity*price[0][0]
            query="insert into sales(bill_ID,cust_ID,prod_ID,no_of_units,price) values(%s,%s,%s,%s,%s)"
            values=(bill1_ID,cID[0][0],pID,quantity,product)
            cursor.execute(query,values)
            db.commit()    
        elif category==4:        
            cursor.execute("select prod_ID,prod_name from product,snacks where product.prod_ID=snacks.pID")
            for l in cursor:
                print("\t\t"+str(l))
            pID=int(input("\nEnter the product you want: "))
            quantity=int(input("\nEnter the quantity of product: "))
            cursor.execute("select no_of_stocks from snacks where pID=%s",(pID,))
            stocks=cursor.fetchall()
            rem_stock=stocks[0][0]-quantity
            cursor.execute("update snacks set no_of_stocks=%s where pID=%s",(rem_stock,pID))
            cursor.execute("select price_per_unit from product where prod_ID=%s",(pID,))
            price=cursor.fetchall()
            product=quantity*price[0][0]
            query="insert into sales(bill_ID,cust_ID,prod_ID,no_of_units,price) values(%s,%s,%s,%s,%s)"
            values=(bill1_ID,cID[0][0],pID,quantity,product)
            cursor.execute(query,values)
            db.commit()    
        
        
    def billing():
        cursor.execute("select prod_ID,cust_ID,no_of_units,price from sales where bill_ID=%s",(bill1_ID,))
        L=cursor.fetchall()
        new_list=[]
        for i in L:
            new_list.append(i)
        cursor.execute("select name from customer where cust_ID=%s",(new_list[0][1],))
        H=cursor.fetchall()
        cust_namelist=[]
        for k in H:
            cust_namelist.append(k)
        print("\n\n******************************BILL**************************************")
        print("\nCustomer name: "+cust_namelist[0][0])
        cursor.execute("select sales_date from sales where sales_id=1")
        date=cursor.fetchall()
        print("Date - {}".format(date[0][0]))
        for i in range(len(new_list)):            
            cursor.execute("select prod_name from product where prod_ID=%s",(new_list[i][0],))
            F=cursor.fetchall()
            p_name=[]
            for d in F:
                p_name.append(d[0]) 
            cursor.execute("select price_per_unit from product where prod_ID=%s",(new_list[i][0],))
            U=cursor.fetchall()
            no_of_unitlist=[]
            for u in U:
                no_of_unitlist.append(u[0]) 
            print()            
            print(p_name[0]+"---------- "+str(new_list[i][2])+"  *  "+str(no_of_unitlist[0])+"  =  "+str(new_list[i][3]))
            cursor.execute("select price from sales where bill_ID=%s",(bill1_ID,))
            total=cursor.fetchall()
            total_list=[]
            for i in total:
                total_list.append(i[0])
        print("\n                                       Total amount={}".format(sum(total_list)))
        print("                                       GST=8.52%")        
        print("\n\n**************Thank You Visit Again!******************")    
                
    while True:
        choice=int(input("\nEnter 1 to add product, 2 to exit:  "))
        if choice==1:
            add_product(name1)
        else:
            billing()
            break     
def customer_registration():
    name=input("\nEnter your name: ")
    mobile=int(input("\nEnter your number: "))
    age=int(input("\nEnter your age: "))
    gender=input("\nYour gender: ")
    query="insert into customer(name,ph_number,age,gender) values(%s,%s,%s,%s)"
    values=(name,mobile,age,gender)
    cursor.execute(query,values)
    db.commit()
    sales()
    
 
def customer_valid():
    number_list=[]
    mobile=int(input("\nEnter your mobile number: "))
    name=input("\nEnter your name: ")
    cursor.execute("select ph_number,name from customer")
    number=cursor.fetchall()
    for i in number:
        number_list.append(i[0])
        if mobile in number_list and i[1]==name:
            print("\nExisting customer")
            sales()
            break
            
    else:
        print("\n\tRegister your mobile number")
        customer_registration()        
print("\t\t\t\t\t\t\t\tWELCOME ADMIN")


def daily_turnover():
        date=int(input("\n\nEnter the date for which you need the total turnover: "))
        cursor.execute("select price from sales where sales_date=%s",(date,))
        df=cursor.fetchall()
        total=0
        for i in df:
            for j in i:
                total+=j    
        print("\nTotal amount for the date you entered is: {}".format(total))
 
def product_add():
    print("\t\nWhich category you want to add?")
    print("""\n
                     1.Dairy
                     2.Fruits
                     3.Beverages
                     4.Snacks
               """)
    category=int(input("\nSelect the category: "))       
    if category==1:
        cursor.execute("select prod_ID,prod_name from product,dairy where product.prod_ID=dairy.pID")
        for d in cursor:
            print("\t\t\t"+str(d))
        pID=int(input("\nWhich product do you want to add: "))
        quantity=int(input("\nEnter number of units you want to add: "))
        cursor.execute("select no_of_stocks from dairy where pID=%s",(pID,))
        stock=cursor.fetchall()
        add=stock[0][0]+quantity
        cursor.execute("update dairy set no_of_stocks=%s where pID=%s",(add,pID))
        db.commit()
    elif category==2:
        cursor.execute("select prod_ID,prod_name from product,fruits where product.prod_ID=fruits.pID")
        for d in cursor:
            print("\t\t\t"+str(d))
        pID=int(input("\nWhich product do you want to add: "))
        quantity=int(input("\nEnter number of units you want to add: "))
        cursor.execute("select no_of_stocks from fruits where pID=%s",(pID,))
        stock=cursor.fetchall()
        add=stock[0][0]+quantity
        cursor.execute("update fruits set no_of_stocks=%s where pID=%s",(add,pID))
        db.commit()
        
    elif category==3:
        cursor.execute("select prod_ID,prod_name from product,beverages where product.prod_ID=beverages.pID")
        for d in cursor:
            print("\t\t\t"+str(d))
        pID=int(input("\nWhich product do you want to add: "))
        quantity=int(input("\nEnter number of units you want to add: "))
        cursor.execute("select no_of_stocks from beverages where pID=%s",(pID,))
        stock=cursor.fetchall()
        add=stock[0][0]+quantity
        cursor.execute("update beveerages set no_of_stocks=%s where pID=%s",(add,pID))
        db.commit()
    elif category==4:
        cursor.execute("select prod_ID,prod_name from product,snacks where product.prod_ID=snacks.pID")
        for d in cursor:
            print("\t\t\t"+str(d))
        pID=int(input("\nWhich product do you want to add: "))
        quantity=int(input("\nEnter number of units you want to add: "))
        cursor.execute("select no_of_stocks from snacks where pID=%s",(pID,))
        stock=cursor.fetchall()
        add=stock[0][0]+quantity
        cursor.execute("update snacks set no_of_stocks=%s where pID=%s",(add,pID))
        db.commit()



def selection(): 
    print("""\n\n
    1.Add product
    2.Buy product
    3.Daily turnover
      """)     
    print("\n\nWhat are you going to do?")
    selection=int(input("\nEnter your choice : "))
    if selection==1:
        product_add()
    elif selection==2:
        customer_valid()
    elif selection==3:
        daily_turnover()
    else:
        pass        
    


while True:
    passw=input("\nEnter password to Enter: ")
    if passw=="12345":
        selection()
        break
    else:
        print("\nEnter the correct password")
            
db.close()

from unittest import installHandler


class Laptop:
    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price

    def show_details():
        print(f'The Laptop\'s name is ')    

instance1 = Laptop('Thinkpad', 'Lenovo', 45000)
instance1.show_details()
# Laptop.show_details()
import pyautogui

# Holds down the alt key
pyautogui.keyDown("alt")

# Lets go of the alt key
pyautogui.keyUp("alt")
def receive_any(arg1,*args):
    print(f'first argument is {arg1}')
    print()
    print(f'Nxt argument is {[i for i in args]}')

def receive_dicts(**kwargs):
    for i,j in kwargs.items():
        print(i,j)
        
# import array 

# new_array = array.array('i',[1,2,3,4,5])

# print(new_array)
# # new_array[6] = 120
# # new_array[2:5] = array.array('i',[12,13,14])
# print(type(new_array))
# print(new_array)

# from django.shortcuts import render
# import datetime

# Create your views here.
from datetime import datetime


import datetime

def home():
    "nothis "
    currentdate = datetime.date.today()
    print('cur ', currentdate)
    formatDate = currentdate.strftime("%d-%b-%y")
    print(formatDate)

home()

def find_max_binary_gap(num) :
    binary = bin(num).replace('0b','')
    zeros_length = []
    loop_range = len(binary) - 1
    for char in range(loop_range) :
        if binary[char] == '1' :
            temp = 0
            temp_str = binary[char+1 :]
            for zero in range(len(temp_str)) :
                if temp_str[zero] == '1' :
                    break
                else :
                    temp += 1
            if temp > 0 :        
                zeros_length.append(temp)
    print(zeros_length)

number =  25637
find_max_binary_gap(number)
from timeit import timeit

func = '''
def binary_search(array,value) :
    array = [5,9,17,23,25,45,59,63,71,89]    
    value = 25
    left = 0
    right = len(array) - 1

    while left <= right :
        mid = (left+right)//2 
        if value == array[mid] :
            return mid
            break
        elif value < array[mid] :
            right = mid - 1
        elif value > array[mid] :
            left = mid + 1  

'''

t = timeit("binary_search",setup=func)
print(t)
# print(binary_search(array,value))
# print(array.index(value))
def binary_sort(arr) :
    length = len(arr)
    for i in range(length) :
        flag = 0
        for j in range(length-1-i) :
            if arr[j] > arr[j+1] :
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                flag = 1
        if flag == 0 :
            break    
    return arr
 
arr = [3,2,6,1,13,9]
print(binary_sort(arr))
def time_elapsed(series,duration):
    elapsed_time = 0
    current_time = 0
    for attack_time in series :
        if attack_time == current_time :
            elapsed_time += 1
            continue
        else :
            current_time = attack_time + (duration - 1 )
            elapsed_time += 2    

    return f"Time elapsed until start of the attack is {elapsed_time}"            

timeSeries = [1,4,6,7,9]
duration = 2
print(time_elapsed(timeSeries,duration))
# Recursive function to find the n-th
# element of sequence
def sequence(n):
	if n == 1 or n == 2:
		return 1
	else:
		return sequence(sequence(n-1)) + sequence(n-sequence(n-1))
		
# Driver code
def main():
	n = 10
	print(sequence(n))
	
if __name__ == '__main__':
	main()




class Check:
    def __init__(self):
        print("This condtructor is called when an object is instantiated")

    def __init__(self):
        print("This is a overridden constructor")        

obj = Check()        

class Calculation1:  
    def Summation(self,a,b):  
        return a+b;  
class Calculation2:  
    def Multiplication(self,a,b):  
        return a*b;  
class Derived(Calculation1,Calculation2):  
    def Divide(self,a,b):  
        return a/b;  
obj = Derived()
print(issubclass(Calculation2,Calculation1))  

txt = "Hello"
print(isinstance(obj,Derived))
import unittest
from selenium import webdriver
from time import sleep

class SearchEnginesTest(unittest.TestCase):
    def test_Google(self):
        self.driver = webdriver.Chrome(executable_path = 'E:\Selenium\chromedriver.exe')
        self.driver.get('http://www.google.com/')
        print(self.driver.title)
        sleep(3)
        self.driver.close()
    def test_Bing(self):
        self.driver = webdriver.Chrome(executable_path = 'E:\Selenium\chromedriver.exe')
        self.driver.get('http://bing.com')
        print(self.driver.title)
        sleep(3)

if __name__ == '__main__':
    unittest.main()        
class Checker:
    cvar = 21
    
    @classmethod
    def method1(cls):
        print('this is method 1', cls.cvar)

    def method2():
        print('This is method 2')  

Checker.method1()  
Checker.method2()
import os
SECRET_KEY = os.environ['PATH']
lis = SECRET_KEY.split(';')

for i in lis:
    print(i)
class check :
    def normal():
        print("Im without self variable")
    def self_fun(self):
        print("Im a class method accessible by a instance")
  
instance = check()
check.normal()   # You can call this method only by using class name
instance.self_fun() # You can only call using instance created

print(check.__dict__)
# def club_everything(dict):
#     res_list = []
#     for key,val in dict.items() :
#         temp_list = []
#         temp_list.append(key)
#         for char in val :
#             temp_list.append(char)
#         res_list.append(temp_list)
#     return res_list  
 
# test_dict = {'gfg': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}
# print(club_everything(test_dict))

# # Alternate

# res_list = [[key] + val for key,val in test_dict.items()]
# print(res_list)

class Softwares:
    names = []
    versions = {}
    def __init__(self,names):
        if names:
            self.names = names.copy()
            for name in names:
                self.versions[name] = 1
            print(self.versions)    
        else:
            raise Exception("Please Enter the names")

p = Softwares(['S1','S2','S3'])
print(p)
# p1 = Softwares([])
# height = [1,8,6,2,5,4,8,3,7]
# max_area = 0

# for i in range(len(height)):
#     for j in range(i+1,len(height)):
#         if j<len(height):
#             # print(i,j)
#             result = min(height[i],height[j])*(j-i)
#             if result>max_area:
#                 max_area = result

# print(max_area)                

nums = [2,7,11,15]
target = 9
result = []

for i in range(len(nums)-1):
    if (nums[i] + nums[i+1]) == target:
        result.append(i)
        result.append(i+1)

print(result)        
object1 = {
    'Name': 'Sriram',
    'Age': 22
}

list1 = [2,3,4,5]
list2 = list1

list2.append(9)
list1.append(333)
print(list1[4])
print(list2)
array = [3,4,5,8,9]
resultList = []

targetValue = array[0]
resultList.append(targetValue)

for number in array:
    if number>targetValue:
        resultList.append(number)

print(len(resultList))        
def check(username, password, email):
    if not username:
        raise ValueError('set username mandatory')
    print('success')    

username = ''
password = 'loop'
email = 'srsr'

check(username=username, password=password, email=email)
def hello_decorator(func):
	def inner1(*args, **kwargs):
		
		print("before Execution")
		
		# getting the returned value
		returned_value = func(*args, **kwargs)
		print("after Execution")
		
		# returning the value to the original frame
		return returned_value
		
	return inner1


# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
	print("Inside the function")
	return a + b

a, b = 1, 2

# getting the value through return of the function
print("Sum =", sum_two_numbers(a, b))

test_dict = {'Gfg' : 3, 'is' : 7, 'best' : 10, 'for' : 6, 'geeks' : 'CS'} 
K = 7 

res = {}
for key in test_dict :
    if not (isinstance(test_dict[key],int) and test_dict[key] >= K ) :
       res[key] = test_dict[key] 

print(res)       

# Alternate 

res = {key : val for key,val in test_dict.items() if not(isinstance(val,int) and val >= 7)}
print(res)

test_list = [[2, 4, 1], [8, 1, 2], [9, 1, 10], [4, 3, 2]]
tar_list = [2, 3, 10, 7, 5, 4]

not_tar = [number for sub_list in test_list for number in sub_list if number not in tar_list]
print(not_tar)
temp_test_list = [value for sub in test_list for value in sub]

not_test = [number for number in tar_list if number not in temp_test_list]
# not_test = [number for number in tar_list for sub_list in test_list if number not in sub_list]

result = abs(sum(not_tar) - sum(not_test))

print(result)
nums = [4,3,2,7,8,2,3,1]
max_num = max(nums)
res_list = []

for num in range(1,max_num+1):
    if num in nums:
        pass
    else:
        res_list.append(num)

print(res_list)        

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

new_records = [[1], [2], [4], [5]]

def do_foo(x, y):
    print('foo', x, y)

def receive_args(*args):
    do_foo(*args)

receive_args(2,3,4)

def do_bar(s):
    print('bar', s)


# for tag, *args in new_records:
#     # if tag == 'foo':
#     #     do_foo(*args)
#     # elif tag == 'bar':
#     #     do_bar(*args)
#     print(tag)
from array import array


class DynamicArray:
    def __init__(self):
        self.array = [2,3,4]
        self.size = 1
        self.count = 3
    
    def growSize(self):
        newsize = self.size * 2
        temp = [0 for num in range(newsize)]
        for num in range(len(self.array)):
            temp[num] = self.array[num]
        self.array = temp        

    def addElement(self,num):
        if self.size == self.count:
            self.growSize()
        self.array.append(num)
        print(self.array)    

obj = DynamicArray()
obj.addElement()
row = 5
col = 5 
const = 1

for i in range(row):
    for j in range(col):
        print(const, end=" ")
        const+=1
    print()    
n = 2
count = 0
for i in range(0,100) :
    if len(str(i)) == n-1:
        count +=1
    if len(str(i)) == n :
        if str(i)[0] == str(i)[1] :
            pass
        else :
            count += 1

print(count)            
        

#!/usr/bin/python3

import os

all_env = os.environ

#for i in all_env:
#    print(f"{i}={all_env[i]}")

print(os.environ['MY_HOME'])

lis = [2,34,0]

# a= 23k

b="Hello"

# c=9s

file_path = r"C:\Users\Admin\Pictures\Camera Roll\myimage.jpg"

with open(file_path,'wb+') as img:
    for chunck in file_path.chunks():
        print(chunck)
def find_binary(num) :
    binary_text = ''
    while num >= 1 :
        val = num % 2
        binary_text += str(val)
        num = num//2 
    return binary_text[::-1]

num = 1041
print(find_binary(num))

num = 1041
binary = bin(num).replace('0b','')


def return_first(nums1,nums2):
    res_list = []
    for sub in nums1 :
        idx = nums2.index(sub)
        for nxt in nums2[idx+1:] :
            if nxt > sub :
                res_list.append(nxt)
                break
        else :
            res_list.append(-1)
    return res_list            

nums1 = [2,4]
nums2 = [1,2,3,4]

print(return_first(nums1,nums2))
def find_and_replace(test_dict,test_list,K) :
    if K in test_list :
        result = test_dict.get(K)
        return f'Exctracted value is {result}'
    else :
        return f'Key not present in the list'

test_list = ["Gfg","is", "Good", "for", "Geeks"]
K = "Gfg"
test_dict = {"Gfg" : 2, "is" : 4, "Best" : 6}

if all(K in sub for sub in [test_dict,test_list]) :
    print(True)
else :
    print(False)    


print(find_and_replace(test_dict,test_list,K))

def find_perfect_square(number) :
    number = number**0.5
    if number - int(number) == 0 :
        return True 
    else :
        return False 

number = 64
print(find_perfect_square(number))


#!/usr/bin/python3

num = 12345
res = ""

for char in str(num):
    res = char + res

print(res)    

def word_index(string_list,target):
    count = -1
    for word in string_list :
        for char in word :
            count+=1
            if count == target :
                target_word = word
                target_char = char
    # print(target_word,target_char)        
    target_index = target_word.find(target_char) 
    return f'The target index is {target_index}'           

test_list = ["geekforgeeks","python","Java"]
target = 12
print(word_index(test_list,target))

# Alternate
test_list = ["geekforgeeks", "is", "best", "for", "geeks"]
index_by_word_list = [char_index[0] for word in enumerate(test_list) for char_index in enumerate(word[1])]
print(index_by_word_list[target])

def firstElementKTime(array, k):
    match_dict = dict()
    if k==1:
        return array[0]
    flag = 0
    for idx in range(len(array)-1):
    	count = 1
    	for nxt in range(idx+1, len(array)):
    		if array[nxt]==array[idx]:
    			count+=1
    			if count>=k:
    				if array[idx] not in match_dict:
    					# flag = 1
    				    match_dict[array[idx]] = nxt
    				    break
    if flag==0:
    	return -1
    else:
        print("Nop flag")				
    
    return list(match_dict.keys())[list(match_dict.values()).index(min(match_dict.values()))]
    
array = [5,4,3,4]    
k = 3

def sortArrays(arr):

    # Finding the length of array 'arr'
    length = len(arr)

    # Sorting using a single loop
    j = 0

    while j < length - 1:

        # Checking the condition for two
        # simultaneous elements of the array
        print('bef',j)
        if (arr[j] > arr[j + 1]):

            # Swapping the elements.
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

            j = -1
        print('aft', j)    
        j += 1
   
    return arr

# Driver Code
if __name__ == '__main__':
    
    # Declaring an integer array of size 11.
    arr = [1, 2, 99, 9, 8,
        7, 6, 0, 5, 4, 3]

    # Printing the original Array.
    print("Original array: ", arr)

    # Sorting the array using a single loop
    arr = sortArrays(arr)

    # Printing the sorted array.
    print("Sorted array: ", arr)

# This code is contributed by Mohit Kumar

name1 = input("Enter your name: ")
name2 = input("Enter your ❤ Love's name: ")

for char in name1:
    if char in name2:
        name1 = name1.replace(char,"",1)
        name2 = name2.replace(char,"",1)
        
count = len(name1)+len(name2)
flames = "flames"

start = 0
end = len(flames)
temp = 0

while len(flames)>1:
    for i in range(start,end):
        temp+=1
        if temp==count:
            flames = flames.replace(flames[i],"")   
            if i==len(flames):
                start = 0
                end = len(flames)
                temp=0
                break 
            start = i
            end = len(flames)
            temp = 0
            break

        if i==len(flames)-1:
            start = 0
            end = len(flames)

print("The Result of your Realtionship is : ", flames)

class Create:
    pass

if __name__  == "__main__":
    c = Create()
    print(type(c))
    print(__name__)
    val = str(c)
    print(val)
import re

ip = "192.168.0.89"
pattern = "^(((25[0-5]|1[0-9][0-9]|[0-9]?[0-9])\.){3}(25[0-5]|1[0-9][0-9]|[0-9]?[0-9])$)"

regex = re.search(pattern,ip)
print(regex)
class PrivateClass:
    def __init__(self):
        self.__name = "Sriram"

    def display(self):
        pass

ref = PrivateClass()
print(ref.__name)                
import os

# current_file_path = os.path.abspath(__file__)
print('File',__file__)
# print(current_file_path)
num = 123
bin_str = ""

while True:
    mod = num%2
    bin_str+=str(mod)
    num=num//2
    if num==0:
        break

print(bin_str[::-1])    
class Name:
    def __get__(self, instance, owner=None):
        return 'Alice Python'


class Person:
    name = Name()


alice = Person()
print(alice.name)
# Alice Python
from collections import Counter

colors_list = ['a','b','b','b','c','c','c','a','f','c']

color_map = Counter(colors_list)

for key,val in color_map.items():
    if val%2 !=0:
        print(key)
        break
n = 2

for i in range(n, -1, -1):
    for j in range(i):
        print(str(i)+ ' ')
import os

def fun_1():
    pid = os.getpid()
    print(pid)

def fun_2():
    fid = os.getpid()
    print(fid)

fun_1()
fun_2()     
print(os.getpid())   
matrix = [[1,1,1],[1,0,1],[1,1,1]]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 0:
            row = i
            col = j

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == row or j == col:
            matrix[i][j] = 0   

print(matrix)               
strs = ["eat","tea","tan","ate","nat","bat"]
anagrams = []

while len(strs)>0:
    first = strs[0]
    temp = []
    temp.append(first)
    for nxt in range(1,len(strs)):
        for char in strs[nxt]:
            if char not in first:
                break
        else:
            temp.append(strs[nxt])
    anagrams.append(temp)           
    for string in temp:
        strs.remove(string)

print(anagrams)        
from PIL import Image

img = Image.open('Sample_img.jpg')
# img.show()
print(img.format)
img.save(r'C:\Sriram\new_img.jpg')
array = [10,20,30,40,50,60,70,80,90]
low = 0
high = len(array)
key = 40

while low<=high:
    mid = (low+high)//2
    if(array[mid]) == key:
        print("Key found")
        print(mid)
        break
    elif key < array[mid]:
        high = mid-1
    elif key > array[mid]:
        low = mid+1

array = [5,4,10,1,6,2]
n = len(array)

for i in range(1, n):
    j = i-1
    temp = array[i]

    while j >= 0 and array[j] > temp:
        array[j+1] = array[j]
        j -= 1

    array[j+1] = temp

print(array)

array = [2,3,4,5,6]
key = 41

for i in array:
    if i==key:
        print("Key is found")
        break
else:
    print("Key not found")    

array = [5,9,3,1,6,2,7]
n = len(array)

for i in range(0,n-1):
    min = i
    for j in range(i+1,n):
        # print('i ',i,' j ',j)
        if array[j] < array[min]:
            # print(True)
            min = j
    if min != i:
        # print('true i not equal ',i)
        # print('min when i is ',i,' min ',min)
        array[i],array[min] = array[min], array[i]
    # print('array after i is ',i,' ',array)
print(array)        
class Stack:
    def __init__(self):
        self.size = -1
        self.stack = []

    def add(self, element):
        if self.size < 5:
            self.stack.append(element)
            self.size += 1
            return self.stack
        else:
            return f"Stack is full"    

    def pop(self):
        popped_value = self.stack.pop()
        return self.stack


user = Stack()
# print(user.add(2))
user.add(21)
user.add(12)
print(user.add(3))
user.add(21)
user.add(21)
print(user.add(6))
print(user.pop())


def insertion_sort(arr) :
    length = len(arr)
    for val in range(1,length) :
        compare_value = arr[val]
        reverse_range = val - 1
        while reverse_range >= 0 and arr[reverse_range] > compare_value :
            arr[reverse_range+1],arr[reverse_range] = arr[reverse_range],arr[reverse_range+1]
            reverse_range -= 1
    return arr       
        
arr = [5,4,10,1,6,2]
print(insertion_sort(arr))







s = 'abracadabra'

str_list = list(s)

str_list.insert(5,'k')

print(str_list)
class Check:
    def __init__(self,var1,var2):
        self.var1=var1
        self.var2=var2
        print(self.var1)

    def execute(self,anyarg):
        print("The argument got is %s"%anyarg)  

obj1=Check('sriram','sr')   
obj1.newvar = "Hello"   
var_to_pass = obj1.newvar
print(type(obj1.newvar))
obj1.execute(var_to_pass)

import re

ip=str(input("Enter the IP: "))

regex="^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

matches = re.findall(regex,ip)
print(matches)
if re.search(regex,ip):
    print("Valid IP")
else:
    print("Invalid IP")

test_list = ["gfg", "3", "oop", "9"]
key_list =[]
value_list=[]

for thing in test_list:
    try:
        temp = int(thing)
        value_list.append(thing)
    except ValueError as e:
        key_list.append(thing)   
res_dict ={}

for count in range(len(key_list)):
    res_dict[key_list[count]] = value_list[count]

print(res_dict)    

var = lambda x,y: x*y*x

print(var(9,12))
parking = [0,1, 0, 1, 1, 1, 1, 0 ,1, 0, 1, 1]
row = 4
col = 3
rowList = []

while row>0:
    temp = []
    for slot in range(col):
        temp.append(parking[0])
        parking.pop(0)
    rowList.append(temp)
    row-=1

rowDict = {}
for row in range(len(rowList)):
    rowDict[row+1] = rowList[row].count(1)

largeRowidx = 0
largeRow = 0

for key,val in rowDict.items():
    if val>largeRowidx:
        largeRow = key
    largeRowidx = val
    

print(largeRow)        

def convert_toDict(test,key):
    global length
    length = len(test)
    res_list = []
    for char in range(0,length,2):
        temp_dict = {key[0] : test[char],key[1] : test[char+1]}
        res_list.append(temp_dict)
    return res_list    

test_list = ["Gfg", 3, "is", 8, "Best", 10, "for", 18, "Geeks", 33]
key_list = ["name", "number"]
  
print(convert_toDict(test_list,key_list)) 

result = [{key_list[0] :test_list[char],key_list[1] : test_list[char+1]} for char in range(0,length,2)]
print(result)
test = "pwwkew"
length = len(test)
temp = ""
length_list = []

for i in range(length):
    if test[i] in temp:
        # length_list.append(len(temp))
        length_list.append(temp)
        temp = ""
    temp+=test[i]
    if i==length-1:
        # length_list.append(len(temp))
        length_list.append(temp)

# print(max(length_list))
print(length_list)

txt = "cbbd"
palindromeList = []

for char in range(len(txt)-1):
    temp = txt[char]
    for nxt in range(char+1,len(txt)):
        temp+=txt[nxt]
        rev = temp[::-1]
        if temp==rev:
            palindromeList.append(temp)
            break

print(palindromeList)        
strList = ["float", "flower", "flight", "floor"]
sample = strList[0]
strList = strList[1:]
subStrings = []

for word in strList:
    temp = ""
    for char in range(len(sample)):
        if char<len(word):
            if sample[char]==word[char]:
                temp+=word[char]
    subStrings.append(temp)
    
print(min(subStrings))              
def getLargePrefix():
    array = ['blow', 'bloweeee']
    pos = 0
    min = 9999

    for sub in array:
        if len(sub)<min:
            min = len(sub)

    for char in range(pos,min):
        for sub in array:
            if array[0][char] != sub[char]:
                return sub[:char]
    return array[0][:char+1]

print(getLargePrefix())    

strs = ["dog","racecar","car"]

compare_str = strs[0]

strs = strs[1:]
common_strs = ""

for char in range(len(compare_str)):
    flag = 0
    for word in strs:
        if char< len(word):
            if not compare_str[char] == word[char]:
                flag = 1
    if flag == 0:            
        common_strs+=compare_str[char]

print(common_strs)    
test_list = ['G', 'F', 'G', 'I', 'S', 'B', 'E', 'S', 'T']
checker = 'G'

result = list(map(lambda char: char if char==checker else '*' ,test_list))
print(result)

from collections import Counter

def non_rep_idx(text):
    for char in range(len(text)):
        if (text[char] not in text[:char]) and (text[char] not in text[char+1:]):
            return char
    return -1

def uniqCharIdx(s):
    count = {}
    for char in s:
        count[char] = count.get(char, 0) +1
    for char in range(len(s)):
        if count.get(s[char]) == 1 or count.get(s[char]) == 0:
            return char
        else:    
            return -1
text = 'leetcode'
print(uniqCharIdx(text))


#!/usr/bin/python3

arr = ["a","b","a"]
k = 3
distinct_array = []
output = ""

for char in range(len(arr)):
    if not char == len(arr)-1:
        if arr[char] in arr[char+1:] or arr[char] in arr[:char]:
            pass
        else:
            distinct_array.append(arr[char])
    else:
        if arr[char] not in arr[:char]:
            distinct_array.append(arr[char])

try:
    output = distinct_array[k-1]

except IndexError as idx_error:
    output = ""
    print(idx_error)

print(output)    



array1 = [2,4]
array2 = [1,2,3,4]
resarray = []

for number in array1:
    idx = array2.index(number)
    if idx != len(array2)-1:
        for nxt in array2[idx+1:]:
            if nxt > number:
                resarray.append(nxt)
                break
        else:
            resarray.append(-1)
    else:
        resarray.append(-1)

print(resarray)                
def optionalFunc(num,txt,p=False,q=True) -> bool:
    if not isinstance(q,bool):
        # raise ValueError
        return
        
    print(num)
    print(txt)
    print(p)
    print(q)

optionalFunc(21,"Sriram",True,"sr")
string = "a1b10"
contValue = 0
for char in range(len(string)):
    if char == contValue:
        continue
    if string[char].isdigit():
        var = string[char-1]
        if string[char+1].isdigit():
            loopRange = int(string[char])*10 + int(string[char+1])
            for i in range(loopRange):
                print(var,end = "")
            contValue = char+1  
        else:
            for i in range(int(string[char])):
                print(var,end = "")

import threading 

def fone():
    for i in range(5):
        print("hhh")

def ftwo():
    for k in range(5):
        print("mmm")        

thread1 = threading.Thread(target=fone())
thread2 = threading.Thread(target=ftwo())

thread1.start()
thread2.start()

thread1.join()
thread2.join()
import math

def find_prime_by_sqrt(number):
     prime_number = int(number**0.5)
     for divident in range(2,prime_number+1):
         if number%divident == 0 :
            #  print(divident)
             return False 
             break
     else :
         return True       

number = 571
print(find_prime_by_sqrt(number))

sqrt = math.sqrt(number)
print(int(sqrt))

def add_delimiter(array,result,delimiter):
    for char in range(len(array)):
        if char!= len(array) - 1 :
            result +=str(array[char])
            result+=delimiter
        else :
            result+=str(array[char])
    return result           



test_list = [4, 7, 8, 3, 2, 1, 9]
result = ""
delimiter = '*'
print(add_delimiter(test_list,result,delimiter))

num1 = 21
num2 = 122
num3 = num1+num2

print("addition of %d and %d is %d"%(num1, num2, num3))
for i in range(1,4):
    for j in range(3-i):
        print(" ",end="")
    for k in range(i,0,-1):
        print(k,end ="") 
    for l in range(2,i+1):
        print(l,end="")       
    print()    
import requests

endpoint = "http://localhost:8000/core/ex1"


with open('C:\Linux_Backup\Git_Repository\Git_cmnds.txt','r') as read_file :
    while True :
        try :
            line = next(read_file)
            print(line)
        except StopIteration as end_of_line :
            break
            
import re
 
String1 ='''secret We are learning regex with geeksforgeeks
         regex is very useful for secret matching.
          It is fast too.'''

regex = re.match("secret",String1,re.IGNORECASE)          
print(regex.group())
import random

mylist = [1,2,3,4,5,6,7,8,9]
random.shuffle(mylist)

print(mylist)
nums = [10,20,30,40,50,60,70,80,90]

def custom_remove(lis, ele):
    new_list = []
    for num in lis:
        if num!=ele:
            new_list.append(num)
    return new_list 

for i in range(0,len(nums),2):
    print(i)
    if i!=0:
        nums = custom_remove(nums,nums[i])
        print(nums)


       
test_dict = {1 : 'Gfg is best for geeks', 2 : 'Gfg is good', 3 : 'I love Gfg'}
sub_list = ['love', 'good']

remove_list = []

for word in sub_list :
    for key,val in test_dict.items() :
        if word in val :
            remove_list.append(key)

for key in remove_list :
    test_dict.pop(key)

print(test_dict)

# Alternate 

dict = {}

for k,v in test_dict.items() :
    if not any(word in v for word in sub_list) :
        dict[k] = v

print(dict)        

# Alternate

result = {for key,val in test_dict.items() if not any(word in val for word in sub_list)}
def check():
    number = 31
    answer = 0
    while True :
        while number>0:
            print("mod",number%10)
            answer += (number%10) * (number%10)
            number = number//10
        number = answer
        print(number)
        if(number==1):
            return f"True"
        elif(number<10):
            return f"False"


print(check())                
def check_func():
    print("This function is to check the default return type of a non returning function")

myfunc = check_func

print(myfunc)
test_list = [[5, 3, 2], [8, 6, 3], [3, 5, 2], [3, 6], [3, 7, 4], [2, 9]]
K = 4 

for idx in range(len(test_list)) :
    if idx == K-1 :
        temp = test_list[idx]
        temp.reverse()
        test_list[idx] = temp

print(test_list)        

array = [[1,2,3],[4,5,6],[7,8,9]]
res_array = [[0,0,0] for row in range(3)]
k = 2
for i in range(3):
    l = 0
    for j in range(3):
        res_array[l][k] = array[i][j]
        l+=1
    k-=1

for i in range(3):
    for j in  range(3):
        print(res_array[i][j],end=" ")        
    print()     
        

arr = [64, 34, 25, 12, 22, 11, 90]
n = len(arr)

for i in range(n):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)            

def bubbleSort(arr):
    n = len(arr)
  
    # Traverse through all array elements
    for i in range(n):
  
        # Last i elements are already in place
        for j in range(0, n-i-1):
  
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
  
  
# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]
  
bubbleSort(arr)
  
print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")

def selectninsert(array,target):
    if target in array:
        return array.index(target)
    for char in range(len(array)-1):
        if array[char]<target and array[char+1]>target:
            return char+1
        elif array[len(array)-1] < target:
            return len(array)

array = [1,3,5,6]            
target = 5
print(selectninsert(array,target))
import smtplib 

server = smtplib.SMTP_SSL("smtp.gmail.com",465) 
server.login("sriramsr9090@gmail.com","Sriram@8124")

from hashlib import new


newSet = set()

# print(type(newSet))

newSet.add(23)
newSet.add(13)
newSet.add(53)
newSet.add(13)

print(newSet)

array = [['java', 1995], ['c++', 1983],
             ['python', 1989]]

sorted_array = sorted(array,key=lambda x:x[0])
print(sorted_array)
test_dict = {"Five": 5,"Three": 3,"One": 1,"four": 4,"Five": 5}
val_sort = [num for num in test_dict.values()]
val_sort.sort()
res_dict = {}
for num in val_sort:
    for key,val in test_dict.items():
        if val==num:
            res_dict[key] = val

print(res_dict)            

from calendar import c
from collections import Counter
def sort_in_decreasing(txt) :
    char_list = list(txt)
    value_frequency = Counter(char_list)
    print(value_frequency)
    new_list = [[key,val] for key,val in value_frequency.items()]
    # print(new_list)
    new_list.sort(key = lambda x : x[1])
    # print(new_list)
    new_list = [new_list[tuple] for tuple in range(len(new_list)-1,-1,-1)]
    print(new_list)
    result = ""
    for tuple in new_list :
        for time in range(tuple[1]) :
            result+=tuple[0]
    return result    
 
s = "tree"
# s = "Aabb"
print(sort_in_decreasing(s))
def combineString(test_list):
    test_list = [['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't']]
    words_list = []
    for sub in test_list:
        temp = ""
        for char in sub:
            temp+=char
        words_list.append(temp)

    resultString = ""
    for word in range(len(words_list)):
        resultString+=words_list[word]
        if word!=len(words_list)-1:
            resultString+=" "
    print(resultString)

class Checker:
    def __init__(self):
        print("Constructor called")    

    def __del__(self):
        print("Objects dleeted")    

obj = Checker()




        
txt = "Geeks$For$Geeks"

for char in txt:
    if char.isalpha():
        print(True,char)
def squid_game(players) :
    winner_list = []
    for player in range(len(players)) :
        temp_list = players[:player] + players[player+1:]
        winner_list.append(sum(temp_list))
    return max(winner_list)

string = '3 6 4 2 5 1'
players_array = list(map(int,string.split()))
print(squid_game(players_array))

txt = 'ABCDCDC'
sub = 'CDC'

parsing_length = len(sub) - 1
count = 0

for i in range(len(txt)-parsing_length):
    if txt[i] == sub[0] :
        if txt[i:i+len(sub)] == sub :
            count += 1
print(count)

def recursive_sum(num):
    if num<10:
        return num
    mod = num%10
    rem = num//10
    return mod + recursive_sum(rem)    

print(recursive_sum(20))    
txt = "HackerRank.com presents Pythonist 2"

res = ""

for char in txt :
    if char.islower() :
        temp = char.upper()
        res += temp
    elif char.isupper() :
        temp = char.lower()
        res += temp
    else :
        res += char    

print(res)            
nums = [1,2,4,6]
operations = [[1,3],[4,7],[6,1]]

for sub in operations:
    if sub[0] in nums:
        idx = nums.index(sub[0])
        nums[idx] = sub[1]

print(nums)        

import sys

arg_1 = sys.argv[0]
print(arg_1)
print(sys.argv)  # Will print the program name as first argument and print any other args you give extra

# print(sys.executable)

# sys.exit()

# print(sys.path)
import os
import threading
import time


def task_sleep(sleep_duration, task_number, lock):
    lock.acquire()
    # Perform operation that require a common data/resource
    lock.release()

    time.sleep(sleep_duration)
    print(f"Task {task_number} done (slept for {sleep_duration}s)! "
          f"Main thread: {threading.main_thread().name}, "
          f"Current thread: {threading.current_thread().name}, "
          f"Process ID: {os.getpid()}")


if __name__ == "__main__":
    time_start = time.time()

    # Create lock (optional)
    thread_lock = threading.Lock()

    # Create thread
    t1 = threading.Thread(target=task_sleep, args=(2, 1, thread_lock))
    t2 = threading.Thread(target=task_sleep, args=(2, 2, thread_lock))

    # Start task execution
    t1.start()
    t2.start()

    # Wait for thread to complete execution
    t1.join()
    t2.join()

    time_end = time.time()
    print(f"Time elapsed: {round(time_end - time_start, 2)}s")

    # Task 2 done (slept for 2s)! Main thread: MainThread, Current thread: Thread-67, Process ID: 6068
    # Task 1 done (slept for 2s)! Main thread: MainThread, Current thread: Thread-66, Process ID: 6068
    # Time elapsed: 2.03s

test_list = [2,4,3,3,7,6,6,9,0]
res_list = []

for char in  range(len(test_list)-2):
    if test_list[char]==test_list[char+1]==test_list[char+2]:
        res_list.append(test_list[char])
    
if len(res_list)==0:
    res_list.append(0)

print(res_list)    
import time
common_list = []
def ten_numbers(n):
    start = time.time()
    for i in range(n):
        common_list.append(i)
    end = time.time()-start
    print(end)    

ten_numbers(10)    
import re

mix_text = """
                saree - 2500
                recharge - 900
                snacks - 500
                Hotstar - 500
                TV - 2000
                Vegis - 500
                Kalyan - 5000
                Beach - 5300
                Birthday - 1500
                CNC - 830
                Net - 500
                Annadhanam - 2500
                Fees - 10000
                Slipper - 300
                Medicine - 600
                Cab Injmbkm - 1250
                Blouse - 500 
                Bracelet - 500
                Sumathi - 500
                Cylinder - 1100
                Dentist - 100
                Router - 2500   """

regex = re.findall('[0-9]{3,5}', mix_text)                
total = 0
five_hundred_count = 0

for num in regex:
    if num == '500':
        five_hundred_count+=1
    print(num)
    total+=int(num)

print(total)
print(five_hundred_count)
print(__file__)

from black import err


try:
    print("Hello")
    array = [2,3,4]
    print(array[88])
except IndexError as error:
    print(error)
finally:
    print("Witout errors")

import pyautogui

# Holds down the alt key
pyautogui.keyDown("alt")

# Lets go of the alt key
pyautogui.keyUp("alt")
def receive_any(arg1,*args):
    print(f'first argument is {arg1}')
    print()
    print(f'Nxt argument is {[i for i in args]}')

def receive_dicts(**kwargs):
    for i,j in kwargs.items():
        print(i,j)
        
# import array 

# new_array = array.array('i',[1,2,3,4,5])

# print(new_array)
# # new_array[6] = 120
# # new_array[2:5] = array.array('i',[12,13,14])
# print(type(new_array))
# print(new_array)

# from django.shortcuts import render
# import datetime

# Create your views here.
from datetime import datetime


import datetime

def home():
    "nothis "
    currentdate = datetime.date.today()
    print('cur ', currentdate)
    formatDate = currentdate.strftime("%d-%b-%y")
    print(formatDate)

home()

def find_max_binary_gap(num) :
    binary = bin(num).replace('0b','')
    zeros_length = []
    loop_range = len(binary) - 1
    for char in range(loop_range) :
        if binary[char] == '1' :
            temp = 0
            temp_str = binary[char+1 :]
            for zero in range(len(temp_str)) :
                if temp_str[zero] == '1' :
                    break
                else :
                    temp += 1
            if temp > 0 :        
                zeros_length.append(temp)
    print(zeros_length)

number =  25637
find_max_binary_gap(number)
from timeit import timeit

func = '''
def binary_search(array,value) :
    array = [5,9,17,23,25,45,59,63,71,89]    
    value = 25
    left = 0
    right = len(array) - 1

    while left <= right :
        mid = (left+right)//2 
        if value == array[mid] :
            return mid
            break
        elif value < array[mid] :
            right = mid - 1
        elif value > array[mid] :
            left = mid + 1  

'''

t = timeit("binary_search",setup=func)
print(t)
# print(binary_search(array,value))
# print(array.index(value))
def binary_sort(arr) :
    length = len(arr)
    for i in range(length) :
        flag = 0
        for j in range(length-1-i) :
            if arr[j] > arr[j+1] :
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                flag = 1
        if flag == 0 :
            break    
    return arr
 
arr = [3,2,6,1,13,9]
print(binary_sort(arr))
def time_elapsed(series,duration):
    elapsed_time = 0
    current_time = 0
    for attack_time in series :
        if attack_time == current_time :
            elapsed_time += 1
            continue
        else :
            current_time = attack_time + (duration - 1 )
            elapsed_time += 2    

    return f"Time elapsed until start of the attack is {elapsed_time}"            

timeSeries = [1,4,6,7,9]
duration = 2
print(time_elapsed(timeSeries,duration))
# Recursive function to find the n-th
# element of sequence
def sequence(n):
	if n == 1 or n == 2:
		return 1
	else:
		return sequence(sequence(n-1)) + sequence(n-sequence(n-1))
		
# Driver code
def main():
	n = 10
	print(sequence(n))
	
if __name__ == '__main__':
	main()




class Check:
    def __init__(self):
        print("This condtructor is called when an object is instantiated")

    def __init__(self):
        print("This is a overridden constructor")        

obj = Check()        

class Calculation1:  
    def Summation(self,a,b):  
        return a+b;  
class Calculation2:  
    def Multiplication(self,a,b):  
        return a*b;  
class Derived(Calculation1,Calculation2):  
    def Divide(self,a,b):  
        return a/b;  
obj = Derived()
print(issubclass(Calculation2,Calculation1))  

txt = "Hello"
print(isinstance(obj,Derived))
import unittest
from selenium import webdriver
from time import sleep

class SearchEnginesTest(unittest.TestCase):
    def test_Google(self):
        self.driver = webdriver.Chrome(executable_path = 'E:\Selenium\chromedriver.exe')
        self.driver.get('http://www.google.com/')
        print(self.driver.title)
        sleep(3)
        self.driver.close()
    def test_Bing(self):
        self.driver = webdriver.Chrome(executable_path = 'E:\Selenium\chromedriver.exe')
        self.driver.get('http://bing.com')
        print(self.driver.title)
        sleep(3)

if __name__ == '__main__':
    unittest.main()        
class Checker:
    cvar = 21
    
    @classmethod
    def method1(cls):
        print('this is method 1', cls.cvar)

    def method2():
        print('This is method 2')  

Checker.method1()  
Checker.method2()
import os
SECRET_KEY = os.environ['PATH']
lis = SECRET_KEY.split(';')

for i in lis:
    print(i)
class check :
    def normal():
        print("Im without self variable")
    def self_fun(self):
        print("Im a class method accessible by a instance")
  
instance = check()
check.normal()   # You can call this method only by using class name
instance.self_fun() # You can only call using instance created

print(check.__dict__)
# def club_everything(dict):
#     res_list = []
#     for key,val in dict.items() :
#         temp_list = []
#         temp_list.append(key)
#         for char in val :
#             temp_list.append(char)
#         res_list.append(temp_list)
#     return res_list  
 
# test_dict = {'gfg': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}
# print(club_everything(test_dict))

# # Alternate

# res_list = [[key] + val for key,val in test_dict.items()]
# print(res_list)

class Softwares:
    names = []
    versions = {}
    def __init__(self,names):
        if names:
            self.names = names.copy()
            for name in names:
                self.versions[name] = 1
            print(self.versions)    
        else:
            raise Exception("Please Enter the names")

p = Softwares(['S1','S2','S3'])
print(p)
# p1 = Softwares([])
# height = [1,8,6,2,5,4,8,3,7]
# max_area = 0

# for i in range(len(height)):
#     for j in range(i+1,len(height)):
#         if j<len(height):
#             # print(i,j)
#             result = min(height[i],height[j])*(j-i)
#             if result>max_area:
#                 max_area = result

# print(max_area)                

nums = [2,7,11,15]
target = 9
result = []

for i in range(len(nums)-1):
    if (nums[i] + nums[i+1]) == target:
        result.append(i)
        result.append(i+1)

print(result)        
object1 = {
    'Name': 'Sriram',
    'Age': 22
}

list1 = [2,3,4,5]
list2 = list1

list2.append(9)
list1.append(333)
print(list1[4])
print(list2)
array = [3,4,5,8,9]
resultList = []

targetValue = array[0]
resultList.append(targetValue)

for number in array:
    if number>targetValue:
        resultList.append(number)

print(len(resultList))        
def check(username, password, email):
    if not username:
        raise ValueError('set username mandatory')
    print('success')    

username = ''
password = 'loop'
email = 'srsr'

check(username=username, password=password, email=email)
def hello_decorator(func):
	def inner1(*args, **kwargs):
		
		print("before Execution")
		
		# getting the returned value
		returned_value = func(*args, **kwargs)
		print("after Execution")
		
		# returning the value to the original frame
		return returned_value
		
	return inner1


# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
	print("Inside the function")
	return a + b

a, b = 1, 2

# getting the value through return of the function
print("Sum =", sum_two_numbers(a, b))

test_dict = {'Gfg' : 3, 'is' : 7, 'best' : 10, 'for' : 6, 'geeks' : 'CS'} 
K = 7 

res = {}
for key in test_dict :
    if not (isinstance(test_dict[key],int) and test_dict[key] >= K ) :
       res[key] = test_dict[key] 

print(res)       

# Alternate 

res = {key : val for key,val in test_dict.items() if not(isinstance(val,int) and val >= 7)}
print(res)

test_list = [[2, 4, 1], [8, 1, 2], [9, 1, 10], [4, 3, 2]]
tar_list = [2, 3, 10, 7, 5, 4]

not_tar = [number for sub_list in test_list for number in sub_list if number not in tar_list]
print(not_tar)
temp_test_list = [value for sub in test_list for value in sub]

not_test = [number for number in tar_list if number not in temp_test_list]
# not_test = [number for number in tar_list for sub_list in test_list if number not in sub_list]

result = abs(sum(not_tar) - sum(not_test))

print(result)
nums = [4,3,2,7,8,2,3,1]
max_num = max(nums)
res_list = []

for num in range(1,max_num+1):
    if num in nums:
        pass
    else:
        res_list.append(num)

print(res_list)        

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

new_records = [[1], [2], [4], [5]]

def do_foo(x, y):
    print('foo', x, y)

def receive_args(*args):
    do_foo(*args)

receive_args(2,3,4)

def do_bar(s):
    print('bar', s)


# for tag, *args in new_records:
#     # if tag == 'foo':
#     #     do_foo(*args)
#     # elif tag == 'bar':
#     #     do_bar(*args)
#     print(tag)
from array import array


class DynamicArray:
    def __init__(self):
        self.array = [2,3,4]
        self.size = 1
        self.count = 3
    
    def growSize(self):
        newsize = self.size * 2
        temp = [0 for num in range(newsize)]
        for num in range(len(self.array)):
            temp[num] = self.array[num]
        self.array = temp        

    def addElement(self,num):
        if self.size == self.count:
            self.growSize()
        self.array.append(num)
        print(self.array)    

obj = DynamicArray()
obj.addElement()
row = 5
col = 5 
const = 1

for i in range(row):
    for j in range(col):
        print(const, end=" ")
        const+=1
    print()    
n = 2
count = 0
for i in range(0,100) :
    if len(str(i)) == n-1:
        count +=1
    if len(str(i)) == n :
        if str(i)[0] == str(i)[1] :
            pass
        else :
            count += 1

print(count)            
        

#!/usr/bin/python3

import os

all_env = os.environ

#for i in all_env:
#    print(f"{i}={all_env[i]}")

print(os.environ['MY_HOME'])

lis = [2,34,0]

# a= 23k

b="Hello"

# c=9s

file_path = r"C:\Users\Admin\Pictures\Camera Roll\myimage.jpg"

with open(file_path,'wb+') as img:
    for chunck in file_path.chunks():
        print(chunck)
def find_binary(num) :
    binary_text = ''
    while num >= 1 :
        val = num % 2
        binary_text += str(val)
        num = num//2 
    return binary_text[::-1]

num = 1041
print(find_binary(num))

num = 1041
binary = bin(num).replace('0b','')


def return_first(nums1,nums2):
    res_list = []
    for sub in nums1 :
        idx = nums2.index(sub)
        for nxt in nums2[idx+1:] :
            if nxt > sub :
                res_list.append(nxt)
                break
        else :
            res_list.append(-1)
    return res_list            

nums1 = [2,4]
nums2 = [1,2,3,4]

print(return_first(nums1,nums2))
def find_and_replace(test_dict,test_list,K) :
    if K in test_list :
        result = test_dict.get(K)
        return f'Exctracted value is {result}'
    else :
        return f'Key not present in the list'

test_list = ["Gfg","is", "Good", "for", "Geeks"]
K = "Gfg"
test_dict = {"Gfg" : 2, "is" : 4, "Best" : 6}

if all(K in sub for sub in [test_dict,test_list]) :
    print(True)
else :
    print(False)    


print(find_and_replace(test_dict,test_list,K))

def find_perfect_square(number) :
    number = number**0.5
    if number - int(number) == 0 :
        return True 
    else :
        return False 

number = 64
print(find_perfect_square(number))


#!/usr/bin/python3

num = 12345
res = ""

for char in str(num):
    res = char + res

print(res)    

def word_index(string_list,target):
    count = -1
    for word in string_list :
        for char in word :
            count+=1
            if count == target :
                target_word = word
                target_char = char
    # print(target_word,target_char)        
    target_index = target_word.find(target_char) 
    return f'The target index is {target_index}'           

test_list = ["geekforgeeks","python","Java"]
target = 12
print(word_index(test_list,target))

# Alternate
test_list = ["geekforgeeks", "is", "best", "for", "geeks"]
index_by_word_list = [char_index[0] for word in enumerate(test_list) for char_index in enumerate(word[1])]
print(index_by_word_list[target])

def firstElementKTime(array, k):
    match_dict = dict()
    if k==1:
        return array[0]
    flag = 0
    for idx in range(len(array)-1):
    	count = 1
    	for nxt in range(idx+1, len(array)):
    		if array[nxt]==array[idx]:
    			count+=1
    			if count>=k:
    				if array[idx] not in match_dict:
    					# flag = 1
    				    match_dict[array[idx]] = nxt
    				    break
    if flag==0:
    	return -1
    else:
        print("Nop flag")				
    
    return list(match_dict.keys())[list(match_dict.values()).index(min(match_dict.values()))]
    
array = [5,4,3,4]    
k = 3

def sortArrays(arr):

    # Finding the length of array 'arr'
    length = len(arr)

    # Sorting using a single loop
    j = 0

    while j < length - 1:

        # Checking the condition for two
        # simultaneous elements of the array
        print('bef',j)
        if (arr[j] > arr[j + 1]):

            # Swapping the elements.
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

            j = -1
        print('aft', j)    
        j += 1
   
    return arr

# Driver Code
if __name__ == '__main__':
    
    # Declaring an integer array of size 11.
    arr = [1, 2, 99, 9, 8,
        7, 6, 0, 5, 4, 3]

    # Printing the original Array.
    print("Original array: ", arr)

    # Sorting the array using a single loop
    arr = sortArrays(arr)

    # Printing the sorted array.
    print("Sorted array: ", arr)

# This code is contributed by Mohit Kumar


from collections import Counter
array = [1,2,2,5,8,4,4,8]

count_dict = Counter(array)
res_list = []
for key in count_dict:
    res_list.append(key)
print(res_list)    
def getme():
    print(True)

from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("DataFlair-youtube video downloader")
Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()

link = StringVar()

Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)

def Downloader():     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)  

Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)

root.mainloop()
test = "geekksforgggeeks"

countList = []
length = len(test)

for i in range(length):
    if i!=0:
        if test[i] == test[i-1]:
            continue
    if i<length-1:
        if test[i]==test[i+1]:
            count = 0
            temp = test[i]
            for j in range(i,length):
                if test[j] == temp:
                    count+=1
                else:
                    countList.append(count)
                    break
        else:
            countList.append(1)            

print(countList)            
import subprocess as sp
from time import sleep
import re 

output = sp.getoutput("ip add")

Lines_split = output.split("\n")

eth_inf_list = []

for line in range(len(Lines_split)):
    if "eth0:" in Lines_split[line]:
        idx = line
        eth_inf_list.append(Lines_split[line])
        for newLine in range(idx+1,len(Lines_split)):
            eth_inf_list.append(Lines_split[newLine])

ethString = "\n".join(eth_inf_list)

reg = re.findall("[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}",ethString)
print(reg)

#!/usr/bin/python3

import re

text = """ <html>
        <head>
        <title> </title>
        <body> </body>
        </head></html>  """

#pattern = re.compile(r"<html>")
#print(pattern.match("<html>"))

#regex = re.findall("<html>",text)
#regex = re.search("<html>", text)

regex = re.match("<html>", text)
print(regex)

import re 

#pattern = "(?:(-?[A-Z0-9]{2}-?){6})"
#pattern = "(?:[A-Z0-9]{2}-){5}[A-Z0-9]{2}"

pattern = "\s(?:[A-Z0-9]{2}-){5}[A-Z0-9]{2}$"

text = """

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Intel(R) Centrino(R) Advanced-N 6205
   Physical Address. . . . . . . . . : 60-67-20-F2-27-4C
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::d079:803d:5285:f713%14(Preferred)
   IPv4 Address. . . . . . . . . . . : 192.168.0.133(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Lease Obtained. . . . . . . . . . : Thursday, July 21, 2022 9:36:07 AM
   Lease Expires . . . . . . . . . . : Sunday, August 27, 2158 6:27:46 PM
   Default Gateway . . . . . . . . . : 192.168.0.1
   DHCP Server . . . . . . . . . . . : 192.168.0.1
   DHCPv6 IAID . . . . . . . . . . . : 56649504
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-2A-49-55-7C-00-21-CC-D6-08-ED
   DNS Servers . . . . . . . . . . . : 192.168.0.1
                                       0.0.0.0
                                       """

regex = re.findall(pattern, text)
print(regex)

import re

text = """
 TCP    127.0.0.1:49657        DESKTOP-URD4TSH:49658  ESTABLISHED
  TCP    127.0.0.1:49658        DESKTOP-URD4TSH:49657  ESTABLISHED
  TCP    127.0.0.1:49680        DESKTOP-URD4TSH:49681  ESTABLISHED
  TCP    127.0.0.1:49681        DESKTOP-URD4TSH:49680  ESTABLISHED
  TCP    127.0.0.1:57629        DESKTOP-URD4TSH:57630  ESTABLISHED
  TCP    127.0.0.1:57630        DESKTOP-URD4TSH:57629  ESTABLISHED
  TCP    127.0.0.1:57631        DESKTOP-URD4TSH:57632  ESTABLISHED
  TCP    127.0.0.1:57632        DESKTOP-URD4TSH:57631  ESTABLISHED
  TCP    192.168.0.133:139      DESKTOP-URD4TSH:0      LISTENING
  TCP    192.168.0.133:49671    a184-26-84-26:https    ESTABLISHED
  TCP    192.168.0.133:50020    server-13-33-146-88:https  ESTABLISHED
  TCP    192.168.0.133:50029    server-13-33-146-22:https  ESTABLISHED
  TCP    192.168.0.133:60338    20.198.119.84:https    ESTABLISHED
  TCP    192.168.0.133:60409    sf-in-f188:5228        ESTABLISHED
  TCP    192.168.0.133:60504    a23-58-20-113:https    CLOSE_WAIT
  TCP    192.168.0.133:60507    a23-58-20-113:https    CLOSE_WAIT
  TCP    192.168.0.133:60511    a23-58-20-113:https    ESTABLISHED
  TCP    192.168.37.1:139       DESKTOP-URD4TSH:0      LISTENING
  TCP    192.168.182.1:139      DESKTOP-URD4TSH:0      LISTENING
  TCP    [::]:135               DESKTOP-URD4TSH:0      LISTENING
  TCP    [::]:445               DESKTOP-URD4TSH:0      LISTENING
  TCP    [::]:3306              DESKTOP-URD4TSH:0      LISTENING
  TCP    [::]:5357              DESKTOP-URD4TSH:0      LISTENING
  TCP    [::]:33060             DESKTOP-URD4TSH:0      LISTENING
  TCP    [::]:49664             DESKTOP-URD4TSH:0      LISTENING
  TCP    [::]:49665             DESKTOP-URD4TSH:0      LISTENING
  TCP    [::]:49666             DESKTOP-URD4TSH:0      LISTENING
  TCP    [::]:49667             DESKTOP-URD4TSH:0      LISTENING
  TCP    [::]:49668             DESKTOP-URD4TSH:0      LISTENING
  TCP    [::]:49669             DESKTOP-URD4TSH:0      LISTENING
  TCP    [::1]:49661            DESKTOP-URD4TSH:49662  ESTABLISHED"""


pattern = "([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}:\d*)|(\[::\d?\]:\d*)"
matches = re.findall(pattern,text)

for tup in matches:
    for each in tup:
        if each:
            if each[0].isdigit():
                print(each.split(":")[1])
            if not each[0].isdigit():
                print(each.split("]:")[1])

def bubble_sort(arr) :
    length = len(arr)
    for i in range(length) :
        flag = 0
        for j in range(length-1-i) :
            if arr[j] > arr[j+1] :
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                flag = 1
        if flag == 0 :
            break    
    return arr
 
arr = [3,2,6,1,13,9]
print(bubble_sort(arr))
def insertion_sort(arr) :
    length = len(arr)
    for val in range(1,length) :
        compare_value = arr[val]
        reverse_range = val - 1
        while reverse_range >= 0 and arr[reverse_range] > compare_value :
            arr[reverse_range+1],arr[reverse_range] = arr[reverse_range],arr[reverse_range+1]
            reverse_range -= 1
    return arr       
        
# arr = [5,4,10,1,6,2]
# insertion_sort(arr)

arr = [5,4,10,1,6,2]
print(insertion_sort(arr))
# for i in range(1,len(arr)) :
#     temp = arr[i]
#     j = i-1
#     while j>=0 and arr[j] > temp :
#         arr[j+1],arr[j] = arr[j],arr[j+1]
#         j-=1
# print(arr)        







def selection_sort(array):
    n = len(array)
    for start in range(n-1):
        min_idx = start
        sub_array = array[start+1:]
        min_value = min(sub_array)
        min_idx = array.index(min_value)
        array[start], array[min_idx] = array[min_idx], array[start]

    return array


array = [5,7,1,4,9,2,8]
print(selection_sort(array))
