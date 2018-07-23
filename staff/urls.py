from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from staff import views
from django.conf import settings
from django.conf.urls.static import static

app_name='staff'
urlpatterns = [
    url(r'^$',views.index,name="staffindex"),
    url(r'^addpatient/$',views.addpatient,name="addpatient"),
    url(r'^viewpatient/$',views.viewpatient,name="viewpatient"),
    url(r'^editpatient/$',views.editpatient,name="editpatient"),
    url(r'^deletepatient/$',views.delpatient,name="deletepatient"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
