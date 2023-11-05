from abc import abstractmethod, ABC

'''

An abstract method is a method that is declared, but contains no implementation.
In python there is no abstarct keyword used for abstarct classes and methods, instead it has a module to enforce
abstraction

'''

class BaseClass(ABC):
    @abstractmethod # need to use this decorator to indicate abstract method
    def to_be_implemented(self):
        raise Exception('Should implement this method in child class, cannot call')
        # should be implemented and mistakenly called means raising error

    def optional_method(self):
        print('This is normal method of Base class')    

class DerivedClass(BaseClass):
    # if this method is not implemented it will throw error
    def to_be_implemented(self):
        print('Implemented class')

    def own_method(self):
        print('I dont care about abstact method')    

derived = DerivedClass()
derived.optional_method()


class Parent:
    __name = None
    __place = None
    __age = None

    def __init__(self, name, place, age):
        self.__name = name
        self.__place = place
        self.__age = age

    def data_about_parent(self):
        print(f'name from parent class {self.__name}')
        # print(f'The parent\'s name is {self.name}, age is {self.age}, and the place is {self.place}')    
        # print(f'The properties that I got from my parent are {self.__name}, {self.__age}, {self.__place}')

    def _protected_method(self):
        'using single _underscore'
        print('protected by parent')

class Child(Parent):
    def use_parent_properties(self):
        pass
        # print(f'name from child class {self.__name}') # this will throw an error
        # print(f'The properties that I got from my parent are {self.__name}, {self.__age}, {self.__place}')

    def calling_parent_methods(self):
        self._protected_method()

child = Child('Ashwin', 'Chennai', 36)        
# child.data_about_parent()
# child.use_parent_properties()
# print(child.__age)
child.calling_parent_methods()
class Base:
	def __init__(self):
		self._a = 2

class Derived(Base):
	def __init__(self):
		Base.__init__(self)
		print("Calling protected member of base class: ")
		print(self._a)

obj1 = Derived()
		
obj2 = Base()
print(obj2.a)



class man:
    def __init__(self):
        self.__C="c"        
class men(man):
    def __init__(self):
        man.__init__(self)
        
ob=men()
print(ob.C)  #It will show error 

''' single underscore is protected variable
    Doule underscore is private variable  '''

class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data member
        self.name = name
        # private member
        self.__salary = salary

    def Use_inside(self):
        print("Using the private variable inside the class")
        print("\nSalary is ",self.__salary)    

# creating object of a class
emp = Employee('Jessa', 10000)
# emp.Use_inside()

# accessing private data members
print('Salary:', emp._Employee__salary)


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

class father:
    def __init__(self):
        self.name="Panneer"
        print(self.name)

    def show(self):
        print('This is from father')    

class mother:
    def __init__(self):
        self.name1="Dharani"
        print(self.name1)

    def show(self):
        print('This is from father')    
    
class son(father,mother):
    def __init__(self):    #Calling the parent class
        father.__init__(self)
        mother.__init__(self)
        print(f"My father is {self.name} and my mother is {self.name1}")

# ob=son()        
# ob.show()

def yield_demo(number):
    for val in range(number):
        if val%2==0:
            yield val

funcChecker = yield_demo(10)            
print(type(funcChecker))
#Instance attributes
class user:
  course= 'Java'   
 #declaring class attribute


O = user()   #creating instance for the class user
 # creating object in user class 
# print(user.course)
print('class dict ', user.__dict__)
print('object dict ', O.__dict__)

O.course = 'C++'   #changing  the attribute value of course
print('object dict2', O.__dict__)
print(O.course)

user.course="Python"

O2 =user()    #creating second instance
print(O2.course) #here  course is printed from the data in its parent class user

class Check:
    cvar = 90
    def __init__(self):
        self.num = 32
        self.val = "Hello"

    def instmeth(self):
        print("This is a instant method")
        print(Check.cvar)
        print(self.num)
    
    # @staticmethod
    def statmeth():
        print("This is a static method")    

    def clasmeth():
        print("This is a class method")


ref = Check()
# ref.statmeth()
Check.statmeth()
# print(ref.num)  
# # print(Check.val)    
# ref.instmeth() 
'''

A class method is a method that is bound to a class rather than its object

'''


class BaseClass:
    class_variable = 'class variable'

    def __init__(self, some_arg):
        self.some_arg = some_arg

    def this_is_stat_method():
        print('This is a static method')    
    
    @classmethod
    def this_is_class_method(cls):
        print('This is class method')

    def this_is_inst_method(self):
        print('This is instance method')

base = BaseClass('argument')
BaseClass.this_is_inst_method() # can't call like this 
base.this_is_class_method() # can call class method with created instance


class Student:
    def __init__(self, name, roll_no, age):
        # private member
        self.name = name
        # private members to restrict access
        # avoid direct data modification
        self.__roll_no = roll_no
        self.__age = age

    def show(self):
        print('Student Details:', self.name, self.__roll_no)

    # getter methods
    

    # setter method to modify data member
    # condition to allow data modification with rules
    def set_roll_no(self, number):
        if number < 50:
            print('Invalid roll no. Please set correct roll number')
        else:
            self.__roll_no = number
    def get_roll_no(self):
        return self.__roll_no        

jessa = Student('Jessa', 10, 15)

# before Modify
jessa.show()
# changing roll number using setter
jessa.set_roll_no(120)
print(jessa.get_roll_no())

jessa.set_roll_no(25)
jessa.show()
class parent:
    def __init__(self):
        self.name="Mani"
class child1(parent):
    def displaychild1(self):
        print(f"my father is {self.name}")
class child2(parent):
    def displaychild2(self):
        print(f"my father is {self.name}")    
c1=child1()
c2=child2()
c1.displaychild1()
c2.displaychild2()

class sample:
    def __init__(self,arg1,arg2):
        self.name=arg1
        self.address=arg2
    def use_init(self):
        print("Name: "+self.name)
        print("Area: "+self.address)
ob=sample('sriram','chennai')
ob.use_init()


class new:
    def __init__(self,age):
        self.age=age
    def fun(self,name):
        self.name=name      #Using a method variable in another method
    def usefun(self):
        return self.name
        
ob=new(12)
ob.fun("sri")
print(ob.usefun())




class sample:
	var1="Sri"   #This is class variable
	def __init__(self,name,age):
		self.name=name
		self.age=age
		print("Name is ",name,"Age is",age)   #This is instance variable

obj1=sample("Vijay",22)
print(obj1.var1)		

class Person:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def display(self):
        print(f"Name is {self.name} and id is {self.id}")

class Office(Person):
    def __init__(self,name,age,id,address):
        self.name=name
        self.age=age
        self.id=id
        self.address=address

        super().__init__(self, name)  # Invoking the parent class(giving arguments to parent class's init)

office_instance = Office("sriram",22,2017,"chennai")
office_instance.display()

class method:
    var1='Java'
    var2='Python'

    def use_var(self):
        print("Var1 : "+method.var1)
        print("Var2 : "+method.var2)
#method.use_var()    # Class method   
ob=method()          #Object method
ob.use_var()

class GrandFather:
    def __init__(self):
        self.grand_father_name = 'GrandFather'

    def common_behaviour(self):
        print('I always takes rest')

class Father(GrandFather):
    def __init__(self):
        self.father_name = 'Father'

    def common_behaviour(self):
        print('I always work')

class Mother(Father):
    def __init__(self):
        self.mother_name = 'Mother'

    def common_behaviour(self):
        print('I always cook')

class Son(Mother, Father):
    def access_methods(self):
        print('I can call ', self.mother_name, ' variable')
        self.common_behaviour() # if this method is not in Mother class, it looks in Father class because of order
        # of inheritance

son = Son()
son.access_methods()


class Grandfather:
    def __init__(self,name):
        self.name=name

    def printdetails(self):
        print(f"My grandson name is {self.name}")

class Father(Grandfather):
    def __init__(self,name,age,address):
        Grandfather.__init__(self,name)
        self.age=age
        self.address=address

    def printfather(self):
        print(f"My son age is {self.age} our address is {self.address}")
     
class son(Father):
    def __init__(self,name,age,address,pin):
        Father.__init__(self,age,address)
        self.name=name
        self.pin=pin
        
    def printson(self):
        print(f"My name is {self.name} and  my pin is {self.pin}")

s=son("sriram",21,"chennai",6066)
s.printson()
s.printfather()
s.printdetails()

class Animals:
	# Initializing constructor
	def __init__(self):
		self.legs = 4
		self.domestic = True
		self.tail = True
		self.mammals = True
	
	def isMammal(self):
		if self.mammals:
			print("It is a mammal.")
	
	def isDomestic(self):
		if self.domestic:
			print("It is a domestic animal.")
	
class Dogs(Animals):
	def __init__(self):
		super().__init__()

	def isMammal(self):
		super().isMammal()

class Horses(Animals):
	def __init__(self):
		super().__init__()

	def hasTailandLegs(self):
		if self.tail and self.legs == 4:
			print("Has legs and tail")

# Driver code
Tom = Dogs()
Tom.isMammal()
Bruno = Horses()
Bruno.hasTailandLegs()
Bruno.isMammal()

class Super_Invoke_Demo:
    def __init__(self):
        self.usable1 = 'Sriram'
        self.usable2 = 23
  
    def formalityMethod(self):
        pass

class Deriver(Super_Invoke_Demo):
    def __init__(self):
        # This is my own init method, but I use the properties from my parent
        super().__init__()
 
    def showGotted(self):
        print('I got this')
        print(f'{self.usable1} is soon to be {self.usable2}')

child_obj = Deriver()
child_obj.showGotted()
def multiple(a,b=0):
    if b>0:
        print(a**b)
    else:
        print(a**2)
        
multiple(5) 
multiple(5,3)           
'''

Polymorphism is a programming term that refers to the use of the same function name, 
but with different signatures, for multiple types in classes

'''

class Vehicle:
    def can_move(self):
        print('Any vehicle can move')


class Bus(Vehicle):
    def can_move(self): # like this child class can implement their own implementation having same function in parent
        print('A bus can move')

class Car(Vehicle):
    def can_move(self):
        print('A car can move')

car_instance = Car()
car_instance.can_move() # if can move is not in Car class, then same method in parent gets called

class default():
    def __init__(self,at1,at2):
        self.at1=at1
        self.at2=at2

    def funn(self):
        print("1st method") 
        
class child(default):
    def child_method(self):
        print("No problem")

obj1=default("at","atti")        
#obj=child() #You should create objects of the child class with attributes to be passed that the parent class expects
obj1.funn()

class office:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    @property  #Changing the method as a attribute   
    def data(self):
        return f"Name is {self.name} and age is {self.age}"
o=office('sri',20)
o.age=21
print(o.data)



class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        self.email = f"{self.fname}.{self.lname}.com"

    def fullname(self):
        print(f"{self.fname} {self.lname}")

emp = Employee("SRi","Ram")  
emp.fname = "SRiraaaaam"  
print(emp.email)
emp.fullname()      
  
class Parent:
  def __init__(self, txt):
    self.message = txt

  def printmessage(self):
    print(self.message)

  def parent_method(self):
    print('Call me using super')

class Child(Parent):
  def __init__(self, txt):
    super().__init__(txt) # here we are providing arguments to the parent(super) fn, using super()

  def child_method(self):
    super().parent_method() # like this you can use super fn to call parent methods
    # self.parent_method()  # you can also acheive with just self

x = Child("Hello, and welcome!")

x.printmessage()
x.child_method()


from abc import abstractmethod, ABC

'''

An abstract method is a method that is declared, but contains no implementation.
In python there is no abstarct keyword used for abstarct classes and methods, instead it has a module to enforce
abstraction

'''

class BaseClass(ABC):
    @abstractmethod # need to use this decorator to indicate abstract method
    def to_be_implemented(self):
        raise Exception('Should implement this method in child class, cannot call')
        # should be implemented and mistakenly called means raising error

    def optional_method(self):
        print('This is normal method of Base class')    

class DerivedClass(BaseClass):
    # if this method is not implemented it will throw error
    def to_be_implemented(self):
        print('Implemented class')

    def own_method(self):
        print('I dont care about abstact method')    

derived = DerivedClass()
derived.optional_method()


class GrandFather:
    def __init__(self):
        self.grand_father_name = 'GrandFather'

    def common_behaviour(self):
        print('I always takes rest')

class Father(GrandFather):
    def __init__(self):
        self.father_name = 'Father'

    def common_behaviour(self):
        print('I always work')

class Mother(Father):
    def __init__(self):
        self.mother_name = 'Mother'

    def common_behaviour(self):
        print('I always cook')

class Son(Mother, Father):
    def access_methods(self):
        print('I can call ', self.mother_name, ' variable')
        self.common_behaviour() # if this method is not in Mother class, it looks in Father class because of order
        # of inheritance

son = Son()
son.access_methods()


class Person:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def display(self):
        print(f"Name is {self.name} and id is {self.id}")

class Office(Person):
    def __init__(self,name,age,id,address):
        self.name=name
        self.age=age
        self.id=id
        self.address=address

        Person.__init__(self, name,id)  # Invoking the parent class(giving arguments to parent class's init)

office_instance = Office("sriram",22,2017,"chennai")
office_instance.display()

'''

Polymorphism is a programming term that refers to the use of the same function name, 
but with different signatures, for multiple types in classes

'''

class Vehicle:
    def can_move(self):
        print('Any vehicle can move')


class Bus(Vehicle):
    def can_move(self): # like this child class can implement their own implementation having same function in parent
        print('A bus can move')

class Car(Vehicle):
    def can_move(self):
        print('A car can move')

car_instance = Car()
car_instance.can_move() # if can move is not in Car class, then same method in parent gets called

class Parent:
  def __init__(self, txt):
    self.message = txt

  def printmessage(self):
    print(self.message)

  def parent_method(self):
    print('Call me using super')

class Child(Parent):
  def __init__(self, txt):
    super().__init__(txt) # here we are providing arguments to the parent(super) fn, using super()

  def child_method(self):
    super().parent_method() # like this you can use super fn to call parent methods
    # self.parent_method()  # you can also acheive with just self

x = Child("Hello, and welcome!")

x.printmessage()
x.child_method()

with open('dummy.txt', 'w') as new_file:
    pass
import re

output = '''
Interface: 192.168.0.114 --- 0x2
  Internet Address      Physical Address      Type
  7192.168.0.1           70-4f-57-9d-b3-7f     dynamic
  224.0.0.22            01-00-5e-00-00-16     static
  224.0.0.251           01-00-5e-00-00-fb     static
  255.255.255.255       ff-ff-ff-ff-ff-ff     static '''

'''
Interface: 10.21.150.167 --- 0xd
  Internet Address      Physical Address      Type
  13.69.109.131         00-11-22-33-44-55     dynamic
  13.78.111.198         00-11-22-33-44-55     dynamic
  13.89.178.27          00-11-22-33-44-55     dynamic
  13.89.179.9           00-11-22-33-44-55     dynamic
  13.107.4.52           00-11-22-33-44-55     dynamic
  13.107.4.254          00-11-22-33-44-55     dynamic
  13.107.5.93           00-11-22-33-44-55     dynamic
  13.107.6.158          00-11-22-33-44-55     dynamic
  20.42.1.1             00-11-22-33-44-55     dynamic
'''

ipPattern = '(((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]?[0-9]))'

# macPattern = '(([0-9a-z]{2}-){5}([0-9a-z]{2}))'

# ip_match = re.findall(ipPattern, output)
# print(ip_match)
# mac_match = re.findall(macPattern, output)

ip_match = re.finditer(ipPattern, output)

for ip in ip_match:
    print(ip.group())



import re

ipString = '''
    
Ethernet adapter VMware Network Adapter VMnet1:

   Connection-specific DNS Suffix  . :
   Link-local IPv6 Address . . . . . : fe80::69f3:eabd:7d30:3011%28
   IPv4 Address. . . . . . . . . . . : 192.168.72.1
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . :

Ethernet adapter VMware Network Adapter VMnet8:

   Connection-specific DNS Suffix  . :
   Link-local IPv6 Address . . . . . : fe80::2d5f:6b6c:451b:6b06%39
   IPv4 Address. . . . . . . . . . . : 192.168.120.1
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . :

Wireless LAN adapter Wi-Fi:

   Connection-specific DNS Suffix  . :
   Link-local IPv6 Address . . . . . : fe80::a895:81d9:b79f:b96a%2
   IPv4 Address. . . . . . . . . . . : 192.168.0.114
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 192.168.0.1
'''

pattern = '(((25[0-9]|2[0-4][0-9]|1[0-9][0-9]|[0-9]?[0-9])\.){3}(25[0-9]|2[0-4][0-9]|1[0-9][0-9]|[0-9]?[0-9]))'

found_addresses = re.findall(pattern, ipString)

print(found_addresses)

class Checker:
    cvar = 23
    def __init__(self, arg1):
        self.arg1 = arg1

    def sampleMeth(self):
        return self.arg1

print('class Dict', Checker.__dict__)      

instance1 = Checker('Sr')

print('Instance dict', instance1.__dict__)
def CommonFunction(shower):
    def wrapper(name, age, place):
        # name+='Hello'
        print(shower(name, age, place))
        print('Executed wrapper')

    return wrapper

@CommonFunction
def displayer(name, age, place):
    return 'The exact name is %s , age is %s and place is %s'%(name, age, place)

displayer('Sriram', 22, 'Chennai')
def getNumber(n):
    try:
        print('Before error')
        m = n/0
        print('After error')
    except Exception as error:
        print(error)
    finally:
        print('In finally')   

def checkFunction(n):
    pass         

getNumber(10)        

