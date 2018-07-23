from patient.models import myuser
from django import forms


class patientform(forms.ModelForm):

    class meta():
        model=myuser
        exclude=["user_isactive","user_username","user_password","user_gender","user_dob","user_image","user_email","user_mobile"]
