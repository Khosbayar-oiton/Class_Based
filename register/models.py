from django.db import models
from django.conf import settings
from django.utils import timezone



class Student(models.Model):

    studID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    studName = models.CharField(max_length=50)
    studAge = models.IntegerField()
    studEmail = models.CharField(max_length=50)
    
class Class(models.Model):
    classID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    className = models.CharField(max_length=50)
    kidQuantity = models.IntegerField()
