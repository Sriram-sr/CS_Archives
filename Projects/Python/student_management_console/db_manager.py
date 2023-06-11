from utilities import *
from datetime import datetime
from threading import Event

class DbAdmin:
    def __init__(self):
        self.db_dictionary = read_json()
        self.event = Event()

    def get_table_from_json(self, field_name, reflect_change=None):
        if reflect_change:
            self.db_dictionary[field_name] = reflect_change
            write_json(self.db_dictionary)
            return 
        return self.db_dictionary.get(field_name)    

    def add_field_to_table(self,field_name, content):
        table_data = self.get_table_from_json(field_name)
        field_id = table_data[-1].get('id')+1
        content = {**{'id': field_id},**content}
        table_data.append(content)
        self.get_table_from_json(field_name, reflect_change=table_data)

    def add_teacher_to_db(self, content):
        self.add_field_to_table('Teachers', content=content)
        logging.info('Admin added %s as Teacher'%(content['first_name']+' '+content['last_name']))

    def add_student_to_db(self, content):
        self.add_field_to_table('Students', content=content)
        logging.info('Admin added %s as Student'%content['fullname'])
        
    def add_user_profile_to_db(self, content):
        self.add_field_to_table('Users', content)

    def add_course_to_db(self, content):
        self.add_field_to_table('Courses', content=content)

    def show_courses(self):
        courses = self.get_table_from_json(field_name='Courses')

