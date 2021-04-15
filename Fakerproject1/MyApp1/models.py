from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=30)
    roll=models.IntegerField()
    marks=models.CharField(max_length=30)
    dob=models.DateField()
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    #address=models.CharField(max_length=60)
