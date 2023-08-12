from django.http import HttpResponse
from django.shortcuts import render
import datetime


def home(request):
    date = datetime.datetime.now()
    isActive = False
    name = "Akshat"
    list_of_programs = ['Write a program to check even odd',
                        'Write a program to check prime numbers ',
                        'Write a program to print all prime numbers from 1 to 100',
                        'Write a program to print pascals triangle']
    student = {'student_name': 'rahul', 'student_college':
               'ZyZ', 'student_city': 'Dewas'}

    if request.method == 'POST':
        aa = request.POST.get('fname')
        bb = request.POST.get('lname')
        cc = request.POST.get('check')
        print(cc)
        if cc == 'True':
            isActive = True
        else:
            isActive = False
        print(aa, bb, isActive)
    data = {
        'isActive': isActive,
        'name': name,
        'list_of_programs': list_of_programs,
        'student': student,
        'date': date
    }
    return render(request, 'home.html', data)


def about(request):
    return render(request, 'about.html')


def service(request):
    return render(request, 'service.html')
