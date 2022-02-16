from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import *

# Create your views here.


def a_login(request):
    error = ""
    if request.method=='POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    d = {'error':error}
    return render(request, 'a_login.html',d)


def a_home(request):
    if not request.user.is_staff:
        return redirect('a_login')
    dcount = Doctor.objects.all().count()
    pcount = Patient.objects.all().count()
    acount = Appointment.objects.all().count()
    return render(request,'a_home.html',{'dcount':dcount,'pcount':pcount,'acount':acount})






def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')


def view_doctor(request):
    doctor = Doctor.objects.all()
    return render(request, 'view_doctor.html', {'doctor':doctor})



def delete_doctor(request,pid):
    if not request.user.is_staff:
        return redirect('a_login')
    doctor = Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')




def a_logout(request):
        if not request.user.is_staff:
            return redirect('a_login')
        logout(request)
        return redirect('a_login') 



def add_doctor(request):
    if not request.user.is_staff:
        return redirect('a_login')
    error = ""
    if request.method=='POST':
        n = request.POST['name']
        nu = request.POST['num']
        s = request.POST['special']
        try:
           Doctor.objects.create(name=n,number=nu,specialization=s)
           error="no"
           
        except:
            error="yes"
    d = {'error':error}
    return render(request, 'add_doctor.html',d)


def add_patient(request):
    if not request.user.is_staff:
        return redirect('a_login')
    error = ""
    if request.method=='POST':
        n =  request.POST['name']
        g = request.POST['gender']
        nu = request.POST['num']
        add = request.POST['address']
        try:
           Patient.objects.create(name=n,gender=g,number=nu,address=add)
           error = "no"
        except:
            error = "yes"
    d = {'error':error}
    return render(request,'add_patient.html',d)



def view_patient(request):
    if not request.user.is_staff:
        return redirect('a_login')
    patient = Patient.objects.all()
    return render(request,'view_patient.html',{'patient':patient})


def delete_patient(request,pid):
    if not request.user.is_staff:
        return redirect('a_login')
    patient = Patient.objects.get(id=pid)
    patient.delete()
    return redirect('view_patient')

def add_appointment(request):
    if not request.user.is_staff:
        return redirect('a_login')
    error = ""
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()
    if request.method=='POST':
        d =  request.POST['doctor']
        p = request.POST['patient']
        da = request.POST['date']
        t = request.POST['time']

        doctor = Doctor.objects.filter(name=d).first()
        patient = Patient.objects.filter(name=p).first()

        try:
           Appointment.objects.create(doctor=doctor,patient=patient,date1=da,time1=t)
           error = "no"
        except:
            error = "yes"
    d = {'patient': patient1,'doctor':doctor1,'error':error}
    return render(request,'add_appointment.html',d)


def view_appointment(request):
    if not request.user.is_staff:
        return redirect('a_login')
    appointment = Appointment.objects.all()
    return render(request,'view_appointment.html',{'appointment':appointment})


def delete_appointment(request,pid):
    if not request.user.is_staff:
        return redirect('a_login')
    appointment = Appointment.objects.get(id=pid)
    appointment.delete()
    return redirect('view_appointment')


def edit_doctor(request,pid):
    if not request.user.is_staff:
        return redirect('a_login')
    error = ""
    doc = Doctor.objects.get(id=pid)


    if request.method == 'POST':
       n = request.POST['name']
       nu = request.POST['num']
       sp = request.POST['special']
      


       doc.name = n
       doc.number = nu
       doc.specialization = sp
       try:
           doc.save() 
           error="no"
       except: 
           error="yes"
       
    d={'error':error,'doc':doc}

    return render(request,'edit_doctor.html',d)




