from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from patient import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^adminbase/',views.adminbase,name='adminbase'),
    url(r'^$',views.base,name="index"),
    url(r'^home/$',views.home,name="home"),
    url(r'^login/$',views.login,name="login"),
    url(r'^signup/$',views.signup,name="signup"),
    url(r'^patient/',include('patient.urls')),
    url(r'^manager/',include('manager.urls')),
    url(r'^staff/',include('staff.urls')),
    



]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
