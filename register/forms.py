# app_name/forms.py
from django import forms
from .models import Class, Student

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['class_Name', 'teacher_Name']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['stud_Class', 'stud_Name', 'stud_Age', 'stud_Email']
