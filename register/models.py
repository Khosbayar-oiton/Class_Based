# app_name/models.py
from django.db import models

class Class(models.Model):
    class_Name = models.CharField(max_length=50)
    teacher_Name = models.CharField(max_length=50)

    def __str__(self):
        return self.class_Name

class Student(models.Model):
    stud_Class = models.ForeignKey(Class, on_delete=models.CASCADE)
    stud_Name = models.CharField(max_length=50)
    stud_Age = models.IntegerField()
    stud_Email = models.EmailField()

    def __str__(self):
        return self.stud_Name
