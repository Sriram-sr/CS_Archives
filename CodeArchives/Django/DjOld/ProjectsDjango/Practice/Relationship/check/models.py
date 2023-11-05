from django.db import models

class Semester(models.Model):
    sem_number = models.IntegerField()
    sem_name = models.CharField(max_length=20)

    def __str__(self):
        return self.sem_name

class Student(models.Model):
    semesters = (
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
        ("5","5"),
        ("6","6"),
    )    
    name = models.CharField(max_length=20)
    semchoices = models.CharField(max_length=3,choices=semesters,null=False)
    sem = models.ManyToManyField(Semester)
    
    def __Str__(self):
        return self.name