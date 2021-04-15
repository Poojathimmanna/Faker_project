from django.shortcuts import render
from MyApp1.models import Student
def view1(request):
    S=Student.objects.all()
    d={"std":S}
    return render(request,'MyApp1/1.html',d)
