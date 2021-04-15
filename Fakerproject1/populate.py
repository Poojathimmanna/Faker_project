import os
import sys
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Fakerproject1.settings')
django.setup()
from faker import Faker
from MyApp1.models import Student
f=Faker()
def Populate(n):
    for i in range(n):
        fname=f.name()
        froll=f.random_int(min=1,max=20)
        fmarks=f.random_int(min=1,max=100)
        fdob=f.date_of_birth()
        femail=f.email()
        fphone=f.random_int(min=1,max=10)
        s=Student.objects.get_or_create(name=fname,roll=froll,marks=fmarks,dob=fdob,email=femail,phone=fphone)
Populate(20)
