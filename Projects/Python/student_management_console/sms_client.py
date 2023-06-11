import socket
from utilities import *
from datetime import date

class Admin():
    def __init__(self, client,username, password):
        self.client = client
        self.username = username
        self.password = password

    def login_admin(self):
        admin_credentials = {'username': self.username, 'password': self.password}
        send_object(self.client, content=admin_credentials)
        admin_login_status = receive_object(self.client)
        if admin_login_status.get('status')==True:
            self.select_choice()
        else:
            print('\nEnter the correct credentials for admin')
            send_text(self.client, content='Sorry server for entering wrong credentials')


    def select_choice(self):
        print('''\nWelcome admin....
        what would you like to do?
        1) Add Teacher
        2) Add Student
        3) Add course
        ''')
        admin_choice = input('Enter your choice: ')
        send_text(self.client, content=admin_choice)
        if admin_choice=='1':
            self.add_teacher()
        elif admin_choice=='2':
            self.add_student()
        elif admin_choice=='3':
            self.add_course()

    def add_teacher(self):
        first_name = input('Enter the First Name: ')
        last_name = input('Enter the Last Name: ')
        email = input('Enter the Email: ')
        mobile_number = input('Enter the Mobile Number: ')
        teacher_status = 'active'
        add_teacher_content={
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'mobile_number': mobile_number,
            'teacher_status': teacher_status
        }
        send_object(self.client, content=add_teacher_content)

    def add_student(self):
        fullname = input('Enter the Full Name: ')
        first_name = input('Enter the First Name: ')
        last_name = input('Enter the Last Name: ')
        mobile_number = input('Enter the Mobile Number: ')
        gender = input('Enter the Gender: ')
        email = input('Enter the Email: ')
        enrollment_date = str(date.today())
        add_student_content={
            'fullname': fullname,
            'first_name': first_name,
            'last_name': last_name,
            'mobile_number': mobile_number,
            'gender': gender,
            'email': email,
            'enrollment_date': enrollment_date
        }
        send_object(self.client, content=add_student_content)

    def add_course(self):
        course_name = input('Enter the name of the course: ')
        start_date = input('Enter the course starting date: ')
        end_date = input('Enter the course ending date: ')
        description = input('Enter the description of the course: ')
        add_course_content={
            'course_name': course_name,
            'start_date': start_date,
            'end_date': end_date,
            'description': description
        }
        send_object(self.client, content=add_course_content)

class Student:
    def student_activities(self, client):
        print('''
        what would you like to do?
        1) Enroll a Course
        2) Update Profile
        3) Pay Fees
        ''')
        user_choice = input('Enter your choice: ')
        send_text(client, content=user_choice)
        received_msg = receive_object(client)
        print(received_msg)
        selected_course = input('\n Enter the ID of the course correctly you want to choose: ')
        send_text(client, content=selected_course)

class Teacher:
    pass    

def startup_page(client):
    user_mode = input('''Who are you ?
    1.Admin
    2.Others
Enter your choice: ''')
    send_text(client, content=user_mode)
    if user_mode=='1':    
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        admin_instance = Admin(client, username, password)
        admin_instance.login_admin()
    elif user_mode=='2':
        user_choice = input('''Who are you ?
        1.Student
        2.Teacher
Enter your choice: ''')
        send_text(client, content=user_choice)
        if user_choice=='1':
            student_instance = Student()
            student_instance.student_activities(client)
        elif user_choice=='2':
            teacher_instance = Teacher()

def connect_server():
    host = '127.0.0.1'
    port = 25454
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    msg_from_server = receive_text(client)
    print(msg_from_server)
    startup_page(client)


if __name__ == '__main__':
    connect_server()    