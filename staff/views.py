from django.shortcuts import render
from patient.forms import myuserform
#from staff.forms import patientform
from django.core.files.storage import FileSystemStorage
from patient.models import UserRole
from patient.models import myuser
from django.contrib.auth .hashers import make_password,check_password
from django.contrib.auth.hashers import BCryptSHA256PasswordHasher



def index(request):

    return render(request,'staffindex.html')


def addpatient(request):
    addpatientobj=myuserform()

    if (request.method == "POST"):

        img=None
        if request.FILES:
            #return render(request,'success1.html')
            myfile=request.FILES['img']
            fs=FileSystemStorage()
            filename=fs.save(myfile.name, myfile)
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

        userrole=UserRole()
        userrole.role_id=3

        f.user_roleid=userrole

        f.save()

        return render(request,'addpatient.html',{'i':img})

    return render(request,'addpatient.html')

def viewpatient(request):

    s=myuser.objects.filter(user_roleid=3)

    return render(request,'viewpatient.html',{'k':s})

def editpatient(request):
    id=request.GET["eid"]
    sdata=myuser.objects.get(user_email=id)

    if request.method=="POST":

        name=request.POST["t1"]
        #id=request.POST["t2"]
        mob=request.POST["t3"]
        dob=request.POST["t4"]

        update = myuser(
            user_email=id,
            user_username=name,
            user_mobile=mob,
            user_dob=dob
        )
        update.save(update_fields=["user_username","user_mobile","user_dob"])

        s=myuser.objects.filter(user_email=id)

        return render(request,'viewstaff.html',{'k':s})



    return render(request,'editpatient.html',{'pdata':sdata})




def delpatient(request):

    id=request.GET["eid"]
    ddata=myuser.objects.get(user_email=id)
    ddata.delete()
    sdata=myuser.objects.filter(user_roleid=3)
    return render(request,'viewpatient.html',{'k':sdata})



# Create your views here.
