from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Employee
# Create your views here.


def emp_home(request):
    emp = Employee.objects.all()

    return render(request, 'emp/home.html', {'emp': emp})


def add_emp(request):
    if request.method == 'POST':
        # data fetch
        name = request.POST.get('emp_name')
        # print(name)
        address = request.POST.get('address')
        # print(address)
        email = request.POST.get('email')
        # print(email)
        number_1 = request.POST.get('number')
        # print(number_1)
        branch = request.POST.get('branch')
        # print(branch)
        working = request.POST.get('working')
        # print(working)
        # crearte model set and set up d    ata
        e = Employee(employee_name=name, employee_address=address,
                     employee_email=email, employee_phone=number_1, employee_department=branch)
        if working is None:
            e.employee_working = False
        else:
            e.employee_working = True
        e.save()
        # save the object
        # prepare message
        return redirect('/emp/home')
    return render(request, 'emp/addemployee.html')


def delete_emp(request, emp_id):
    aa = Employee.objects.get(pk=emp_id)
    aa.delete()

    return redirect('/emp/home')


def update_emp(request, emp_id):
    aa = Employee.objects.get(pk=emp_id)

    return render(request, "emp/update_emp.html", {'emp': aa})


def update_do(request, emp_id):
    if request.method == 'POST':
        emp_name = request.POST.get("emp_name")
        emp_id_temp = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working")
        emp_department = request.POST.get("emp_department")

        e = Employee.objects.get(pk=emp_id)
        e.employee_name = emp_name

        e.employee_phone = emp_phone
        e.employee_address = emp_address
        e.employee_department = emp_department
        if emp_working is None:
            e.working = False
        else:
            e.working = True

        e.save()
        # save the object
        # prepare message
        return redirect('/emp/home')
