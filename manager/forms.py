from manager.models import department
from manager.models import staff
from django import forms
from patient.models import myuser


class departmentform(forms.ModelForm):

    class Meta():
        model=department
        #fields='__all__'
        exclude=["dept_id","dept_name"]


class staffform(forms.ModelForm):

    class Meta():
        model=myuser
        exclude=["user_isactive","user_username","user_roleid","user_password","user_gender","user_dob","user_image","user_email","user_mobile"]
