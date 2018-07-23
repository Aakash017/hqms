from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from patient import views

app_name='patient'
urlpatterns = [

    url(r'^index/',views.index,name="index"),
    url(r'^changepassword/',views.changepassword,name="changepassword"),
    url(r'^editprofile/',views.edittprofile,name="editprofile"),





]
