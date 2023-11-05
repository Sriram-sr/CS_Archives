from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, StudentList
from django.db.models import Q

def viewTable(request):
    # students = Student.objects.all()
    students = Student.objects.filter(
        Q(name__startswith='M')|
        Q(name='Sr'))
    # print(students.query)
    print(students)

    # students = StudentList.objects.filter(classroom=2) | StudentList.objects.filter(lastname__startswith='s')
    # print(students)
    # print(students.query)
    return HttpResponse('')

def selectQuery(request):
    students = Student.objects.all().values_list('name', 'age')
    # this is like Select name,age from students
    all_students = Student.objects.all().values_list()
    all_in_dictionary = Student.objects.all().values('name')
    print(all_in_dictionary)
    # this is like select*from students

    both_names = Student.objects.all().values_list('name').union(StudentList.objects.all().values_list('age'))

    print(both_names)
    print(all_students)
    print(students)
    return HttpResponse('')

def fiter_startswith(request):
    students_by_s = StudentList.objects.filter(
        Q(firstname__startswith='s') |
        Q(lastname__startswith='s')
         ).values('firstname', 'lastname')

    print(students_by_s)     
    return HttpResponse('')

def exclude_fields(request):
    not_age_students = StudentList.objects.exclude(age=12)
    # print(not_age_students.query)
    # print(not_age_students)
    # greater_age_students = StudentList.objects.exclude(age__lte=14)
    greater_age_students = StudentList.objects.filter()
    print(greater_age_students)

    
    return HttpResponse('')

def using_order_by(request):
    students = StudentList.objects.all().order_by('firstname')
    students = StudentList.objects.all().order_by('-lastname')
    students = StudentList.objects.all().order_by('-age')
    students = StudentList.objects.all().order_by('?')    # this will be random order
    print(students)
    
    return HttpResponse('')

