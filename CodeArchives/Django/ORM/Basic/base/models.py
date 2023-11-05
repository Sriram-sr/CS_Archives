from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100, null=True)
    age = models.IntegerField()
    place = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class StudentList(models.Model):
    firstname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True)
    classroom = models.IntegerField(null=True)
    teacher = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.firstname+' '+self.lastname

class ChoiceChecker(models.Model):
    YEAR_IN_SCHOOL_CHOICES = [
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('GR', 'Graduate'),
    ]

    name = models.CharField(max_length=100, null=True, blank=True)
    year_in_school = models.CharField(choices=YEAR_IN_SCHOOL_CHOICES, max_length=2)

    def __str__(self):
        return self.year_in_school

class Classroom(models.Model):
    gender_choices = [
        ('M', 'male'),
        ('F', 'female')
    ]
    name = models.CharField(max_length=100, null=True)
    std = models.IntegerField(null=True)
    mark = models.IntegerField(null=True)
    gender = models.CharField(max_length=1, choices=gender_choices, null=True)

    def __str__(self):
        return self.name