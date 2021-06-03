from django.db import models
from django.db.models.deletion import CASCADE
from datetime import datetime

# Create your models here.
# When you create a model (table) you have to run python manage.py makemigrations and then python manage.py migrate to save the changes
# many to one: one model record can have many other model record associated with it. For example, A school model can have many Student Models associated with it. 
# one to one: One record is associated with just another record. For example, in a school setting, a student can only have one studentID while a studentID can only be assigned to one student.

class School(models.Model): #this is a table, the categories below are columns
    name = models.CharField(max_length =50)
    address = models.CharField(max_length = 50)
    zip_code = models.IntegerField()

    def __str__(self):
        return self.name

class Faculty(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length = 50)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Certificate_Type(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name


class Grade(models.Model):
    grade_level= models.CharField(max_length = 50)

    def __str__(self):
        return self.grade_level


class Student(models.Model):
    full_name = models.CharField(max_length = 50)
    year_of_graduation = models.DateField(auto_now=datetime.year)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    certificate_type = models.ForeignKey(Certificate_Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name