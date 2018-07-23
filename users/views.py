from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from patient.forms import myuserform
from django.core.files.storage import FileSystemStorage
from patient.models import UserRole,myuser
from django.contrib.auth .hashers import make_password,check_password
from django.contrib.auth.hashers import BCryptSHA256PasswordHasher


# Create your views here
def index(request):
    return render(request,'index.html')



