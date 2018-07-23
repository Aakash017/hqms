from django.shortcuts import render,HttpResponse,redirect
from patient.forms import myuserform
from django.core.files.storage import FileSystemStorage
from patient.models import UserRole,myuser
from django.contrib.auth .hashers import make_password,check_password
from django.contrib.auth.hashers import BCryptSHA256PasswordHasher

def base(request):
    return render (request,'base.html')

def home(request):
    return render(request,'home.html')



def signup(request):

    signobj=myuserform()

    if request.method == "POST":
        #return render(request,'success.html')
        img = None
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

        userrole=UserRole()
        userrole.role_id=3

        f.user_roleid=userrole

        f.save()

        return render(request,'success.html')





    return render(request,'signup.html')

# Create your views here.

def login(request):

    context={
        "message":"please log in",
        "error":False
    }

    if(request.method=="POST"):   #when we click on submit#
        pwd=""
        try:
            getUser=myuser.objects.get(user_email=request.POST["email"])
            context['msg'] = getUser
            pwd = request.POST['password']
            pwd2 = getUser.user_password

            result = check_password(pwd, pwd2)

        except:
            context['message']="wrong username"
            context['error']=True

            return render(request,'login.html',{'wrnguname':'success'})

        if(result==True):
            request.session['authenticated']=True

            request.session['roleid']=getUser.user_roleid_id
            request.session['user_image']=getUser.user_image
            request.session['user_name']=getUser.user_username
            request.session['emailid']=request.POST["email"]
            request.session['password']=request.POST["password"]

            if(request.session['roleid']==3):
                return redirect('/patient/index/')
            if(request.session['roleid']==1):
                return redirect('/manager/')
            if(request.session['roleid']==2):
                return redirect('/staff/')





        else:

            context['message']="wrong password"
            context['error']=True

            return render(request,'login.html',{'wrngpass':'success'})



    return render(request,'login.html',context)



def adminbase(request):

    return render(request,'adminbase.html')





def index(request):
    return render (request,'managerindex.html')

def changepassword(request):
    #form=NewUserForm()
    if request.method=="POST":
        #form=NewUserForm(request.POST)
        email=request.session["useremail"]
        oldpwd=request.POST['oldpassword']

        newpwd=request.POST['newpassword']
        conpwd=request.POST['conpassword']

        us = myuser.objects.get(user_email=email)
        b=us.user_password
        #return render(request,'changePassword.html',{'op':oldpwd,'b':b,'np':email})
        if(check_password(oldpwd,b)):

            if(newpwd==conpwd):

                    addUser = myuser(
                        user_email = email,
                        user_password = make_password(newpwd)
                    )
                    addUser.save(update_fields=["user_password"])


                    return render(request,'changePassword.html',{'correctpwd':'sucess'})
            else:
                return render(request,'changePassword.html',{'mismatchpassword':'sucess'})
        else:
            return render(request,'changePassword.html',{'wrngpwd':'sucess'})

    return render(request,'changePassword.html')



def edittprofile(request):
    email=request.session["useremail"]
    userdata=myuser.objects.get(user_email=email)
    if request.method=="POST":
        user_image=None
        if request.FILES:
            myfile = request.FILES['user_image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name,myfile)
            user_image=fs.url(filename)
            user_image=myfile.name
        else:
            user_image=userdata.user_image

        email=request.session["useremail"]
        name=request.POST['name']
        dob=request.POST['dob']
        mobile=request.POST['mobile']
        update = myuser(
            user_email =email,
            user_name=name,
            user_dob=dob,
            user_mobile=mobile,
            user_image=user_image
        )
        update.save(update_fields=["user_name","user_dob","user_image","user_mobile"])
        email=request.session["useremail"]
        userdata=myuser.objects.get(user_email=email)
        return render(request,'profile.html',{'editsuc':'success','userdata':userdata})
    userdata=myuser.objects.get(user_email=email)
    return render(request,'edit_profile.html',{'userdata':userdata})


