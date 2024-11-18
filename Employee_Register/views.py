from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.db import transaction

from .forms import EmployeeForm
from .models import Employee,Position

# Create your views here.

def employee_list(request):
    employees=Employee.objects.all()
    return render(request,"employee/employee_list.html",{'employees':employees})

def employee_form(request,id=0):
    if request.method=="POST":
        if id==0:
            form=EmployeeForm(request.POST)
        else:
            employee=Employee.objects.get(pk=id)
            form=EmployeeForm(request.POST,instance= employee)                 
        if form.is_valid():
                form.save()
        else:
             print(form.add_error)
             print("KKK")        
        return redirect("employee_list")      
    else:
         if id==0:
              form=EmployeeForm()
         else:
              employee=Employee.objects.get(pk=id)
              form=EmployeeForm(instance=employee)
    return render(request,"employee/employee_form.html",{'form':form})    

def employee_delete(request,id):
    print("Deleting")
    deleted=Employee.objects.filter(id=id).delete()
    print(str(deleted))
    return redirect('employee_list')

