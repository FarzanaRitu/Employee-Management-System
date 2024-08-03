from django.shortcuts import render, HttpResponse
from .models import Employee, Department, role
from datetime import datetime
from django.db.models import Q

# Create your views here.

def index(request):
    # return HttpResponse("this is home page")
    return render(request, 'index.html')

# def filter_emp(request):
#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         dept = int(request.POST['dept'])
#         role = int(request.POST['role'])
#         emps = Employee.objects.all()
#         if name:
#             emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
#         if dept:
#             emps = emps.filter(dept__name = dept)
#         if role:
#             emps = emps.filter(role__name = role)
#         context = {
#         'emps': emps
#                   }    
#         return render(request, 'view_emp.html', context)
#     elif request.method == 'GET':
#         return render(request, 'filter_emp.html')
#     else:
#         return HttpResponse("An exception Occured")
     
#     # return HttpResponse("this is home page")
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from .models import Employee

def filter_emp(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        dept = request.POST.get('dept', '')
        role = request.POST.get('role', '')

        name = first_name + ' ' + last_name  # Combine first name and last name
        
        emps = Employee.objects.all()
        
        if name.strip():
            emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        
        if dept:
            emps = emps.filter(dept__name=dept)
         
        if role:
            emps = emps.filter(role__name=role)
        
        context = {
            'emps': emps
        }    
        return render(request, 'view_emp.html', context)
    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse("An exception occurred")

    
def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phn = int(request.POST['phn'])
        dept = request.POST['dept']
        role = request.POST['role']
        salary =int(request.POST['salary'])
        bonus = int( request.POST['bonus'])
        hire_date = request.POST['hire_date']
        new_emp = Employee(first_name = first_name, last_name = last_name, phn = phn, dept_id = dept, role_id = role, hire_date = datetime.now() )
        new_emp.save()
        return HttpResponse("Employee Added Successfully")
    elif request.method == 'GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponse("some error occured")

def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Succesfully")
        except:
            return HttpResponse("Enter a valid response")
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    # return HttpResponse("this is home page")
    return render(request, 'remove_emp.html',context)

def view_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)

    # return HttpResponse("this is home page")
    return render(request,'view_emp.html', context)