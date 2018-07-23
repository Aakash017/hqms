from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from manager import views
from django.conf import settings
from django.conf.urls.static import static


app_name='manager'

urlpatterns=[
     url(r'^$',views.index,name="index"),
     url(r'^adddept/$',views.addept,name="adddept"),
     url(r'^viewdept/$',views.viewdept,name="viewdept"),
     url(r'^deletedept/$',views.deldept,name="delete"),
     url(r'addstaff/$',views.addstaff,name="addstaff"),
     url(r'viewstaff/$',views.viewstaff,name="viewstaff"),
     url(r'deletestaff/$',views.delstaff,name="deletestaff"),
     url(r'updatedept/$',views.updep,name="updatedept"),
     url(r'updatestaff/$',views.upstaff,name="updatestaff"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
