from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from student.models import Student


def home(request):
    return render(request, 'index.html')


def f1(request):
    return render(request, 'registration.html')


def f2(request):
    return render(request, 'login.html')

def registrationfunction(request):
    userName = request.POST['userName']
    userEmail = request.POST['userEmail']
    userPassword = request.POST['userPassword']
    userSubject = request.POST['userSubject']
    userMobile = request.POST['userMobile']
    #WE NEED TO CREATE student object WITH ABOVE VALUES
    s1 = Student()
    s1.name = userName
    s1.email = userEmail
    s1.pw = userPassword
    s1.sub = userSubject
    s1.mobile = userMobile
    #NOW LETS INSERT A ROW (object)
    s1.save() #---> inserts s1 object into Student table
    return render(request, 'registration.html')


def showfunction(request):
    #first we will get all rows from student table
    allstudents = Student.objects.all() #select * from student
    return render(request, 'display.html', {'x' : allstudents} )

def loginfunction(request):
    x = request.POST['userEmail'] #user has entered some email...
    y = request.POST['userPassword'] #user has entered some pw..
    if Student.objects.filter(email= x,pw=y).exists():
        return HttpResponse('<h1>success</h1>')
    else:
        return HttpResponse('<h1>failure</h1>')





def updatefunction(request,id): #id will be 4 if im clicking 2nd student
    student = Student.objects.get(id=id)

    if request.method == "POST":
        student.name = request.POST['userName']
        student.email = request.POST['userEmail']
        student.pw = request.POST['userPassword']
        student.sub = request.POST['userSubject']
        student.mobile = request.POST['userMobile']
        student.save()
        x = Student.objects.all()
        return render(request,'display.html',{'x' : x})

    return render(request,'update.html',{'data' : student})

def deletefunction(request,id):
    student = Student.objects.get(id=id)
    student.delete()
    x = Student.objects.all()
    return render(request, 'display.html', {'x': x})
