from patient.models import myuser
from django import forms


class myuserform(forms.ModelForm):

    class Meta():
        model=myuser
        #fields='__all__'
        exclude=["user_isactive","user_username","user_roleid","user_password","user_gender","user_dob","user_image","user_email","user_mobile"]







