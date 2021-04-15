from django.contrib import admin
from MyApp1.models import Student
class StudentAdmin(admin.ModelAdmin):
    l=["name","roll","marks","dob","email","phone"]
admin.site.register(Student,StudentAdmin)
