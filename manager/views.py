from django.shortcuts import render
from manager.forms import departmentform
from manager.forms import staffform
from manager.models import department
from django.core.files.storage import FileSystemStorage
from django.contrib.auth .hashers import make_password,check_password
from django.contrib.auth.hashers import BCryptSHA256PasswordHasher
from patient.models import UserRole
from patient.models import myuser

from patient.forms import myuserform


def index(request):
    return render(request,'managerindex.html')


def addept(request):

    dobj=departmentform()



    if (request.method == "POST"):
        #return render(request,'success.html')


        form=departmentform(request.POST)

        f=form.save(commit=False)
        f.dept_name=request.POST["d1"]

        f.save()

        return render(request,'success.html')
    return render(request,'adddept.html')


def viewdept(request):

    depdata=department.objects.all()

    return render(request,'viewdept.html',{'dep':depdata})

def deldept(request):

    id=request.GET["did"]
    ddata=department.objects.get(dept_id=id)
    ddata.delete()

    depdata=department.objects.all()

    return render(request,'viewdept.html',{'dep':depdata})



def addstaff(request):
    addstaffobj=staffform()


    if (request.method == "POST"):

        img=None
        if request.FILES:
            myfile=request.FILES['img']
            fs=FileSystemStorage()
            filename=fs.save(myfile.name,myfile)
            img=fs.url(filename)
            img=myfile.name


        form=myuserform(request.POST)

        f=form.save(commit=False)
        f.user_username=request.POST["Name"]
        f.user_email=request.POST["email"]
        f.user_password= make_password(request.POST["password"])
        f.user_mobile=request.POST["mobileno"]
        f.user_gender=request.POST["gender"]
        f.user_dob=request.POST["dob"]
        f.user_image=img


        staff=UserRole()
        staff.role_id=2

        f.user_roleid=staff

        f.save()

        return render(request,'success.html')





    return render(request,'addstaff.html')

def viewstaff(request):

    s=myuser.objects.filter(user_roleid=2)

    return render(request,'viewstaff.html',{'k':s})

def delstaff(request):
    id=request.GET["sid"]
    sdata=myuser.objects.get(user_email=id)
    sdata.delete()

    s=myuser.objects.filter(user_roleid=2)

    return render(request,'viewstaff.html',{'k':s})

def updep(request):
    id=request.GET["did"]
    ddata=department.objects.get(dept_id=id)




    return render(request,'updatedept.html',{'dep':ddata})


def upstaff(request):
    id=request.GET["sid"]
    sdata=myuser.objects.get(user_email=id)

    if request.method=="POST":

        name=request.POST["t1"]
        email=request.POST["t2"]
        mob=request.POST["t3"]
        dob=request.POST["t4"]

        update = myuser(
            user_email=email,
            user_username=name,
            user_mobile=mob,
            user_dob=dob
        )
        update.save(update_fields=["user_username","user_mobile","user_dob"])

        s=myuser.objects.filter(user_email=email)

        return render(request,'viewstaff.html',{'k':s})




    return render(request,'updatestaff.html',{'sdata':sdata})




# Create your views here.
