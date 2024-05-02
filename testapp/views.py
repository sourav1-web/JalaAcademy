from django.shortcuts import render,redirect
from testapp.forms import EmployeeForm
from .models import Employee
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def HomeView(request):
  return render(request,'testapp/index.html')

def InsertEmployee(request):
  form=EmployeeForm()
  if request.method=='POST':
    form=EmployeeForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/List_Employee')
  return render(request,'testapp/Insert_Employee.html',{'form':form})

def ListEmployee(request):
  employee_list=Employee.objects.all()
  return render(request,'testapp/List_Employee.html',{'employee_list':employee_list})

def UpdateEmployee(request, id):
    employee_instance = Employee.objects.get(id=id)
    form = EmployeeForm(instance=employee_instance)
    
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee_instance)
        if form.is_valid():
            form.save()
            return redirect('/List_Employee')
    
    return render(request, 'testapp/update.html', {'form': form})

def DeleteEmployee(request,id):
    employee_instance = Employee.objects.get(id=id)
    employee_instance.delete()
    return redirect('/List_Employee')


def More_Menu_1(request):
   return render (request,'testapp/more1.html')
def More_Menu_2(request):
   return render (request,'testapp/more2.html')
def More_Menu_3(request):
   return render (request,'testapp/more3.html')
def More_Menu_4(request):
   return render (request,'testapp/more4.html')
def More_Menu_5(request):
   return render (request,'testapp/more5.html')
def More_Menu_6(request):
   return render (request,'testapp/more6.html')

