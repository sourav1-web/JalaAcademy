from django.contrib import admin
from testapp.models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','first_name','last_name','email','mobile','dob','gender','address','country','city','skills']
admin.site.register(Employee,EmployeeAdmin)    