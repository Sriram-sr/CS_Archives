import socket
from _thread import start_new_thread
from utilities import *
from db_manager import DbAdmin

logging.basicConfig(filename=log_file_path, level=logging.info,
                    format='%(asctime)s- %(levelname)s - %(message)s')

class AdminUtilities(DbAdmin):
    def choose_admin_choice(self, choice):
        if choice=='1':
            self.add_teacher()
        elif choice=='2':
            self.add_student()
        elif choice=='3':
            self.add_course()

    def add_teacher(self):
        content = receive_object(client)
        self.add_teacher_to_db(content)

    def add_student(self):
        content = receive_object(client)
        self.add_student_to_db(content)

    def add_course(self):
        content = receive_object(client)
        self.add_course_to_db(content) 

class StartupUtilities(DbAdmin):
    def initial_functions(self, client):
        client_choice = receive_text(client)
        if client_choice == '1':
            credentials_from_client = receive_object(client)
            credentials_from_db = self.get_table_from_json('Credentials')[0].get('admin')
            if credentials_from_db == credentials_from_client:
                logging.info('Admin login Successful')
                send_object(client, content={'status': True})
            else:
                send_object(client, content={'status': False})   
            admin_choice = receive_text(client)
            admin_instance = AdminUtilities()
            admin_instance.choose_admin_choice(admin_choice)
        
        elif client_choice == '2':
            student_or_teacher = receive_text(client)
            if student_or_teacher == '1':
                student_instance = StudentFunctions()
                student_choice = receive_text(client)
                if student_choice == '1':
                    student_instance.course_enrollment()
                    # StudentFunctions.course_enrollment(DbAdmin)
                    # self.course_enrollment()
            if student_or_teacher == '2':
                pass


class StudentFunctions(StartupUtilities):
    def course_enrollment(self):
        courses = self.get_table_from_json(field_name='Courses')
        send_object(client, content=courses)


def start_server():
    global server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 25454
    server.bind((host, port))
    server.listen()
    print('Server Listening')
    logging.info('Server Started')


def client_thread_start(client):
    start_instance = StartupUtilities()
    start_instance.initial_functions(client)


if __name__ == '__main__':
    start_server()
    while True:
        client, address = server.accept()
        logging.info('Connected with client %s' % (address[0]))
        send_text(client, content='Successfully connected...')
        start_new_thread(client_thread_start, (client,))
