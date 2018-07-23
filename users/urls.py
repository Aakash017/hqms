from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from patient import views
from users import views

app_name='users'
urlpatterns = [

    url(r'^index/',views.index,name="index"),






]






