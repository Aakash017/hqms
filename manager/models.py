from django.db import models
from patient.models import UserRole




class department(models.Model):
    dept_id=models.AutoField(primary_key=True)
    dept_name=models.CharField(max_length=255,default="",unique=True)

    def __str__(self):
     return self.dept_name


class staff(models.Model):

    staff_roleid = models.ForeignKey(UserRole,on_delete=models.CASCADE,default="")
    staff_id=models.AutoField(primary_key=True)
    staff_username= models.CharField(max_length=255,default="")
    staff_password=models.CharField(max_length=20,default="")
    staff_email=models.EmailField(max_length=255,default="",unique=True)
    staff_mobile=models.CharField(max_length=255,default="")
    staff_gender=models.CharField(max_length=20,default="")
    staff_dob=models.CharField(max_length=255,default="")
    staff_image= models.CharField(max_length=255,null=True)

    staff_isactive=models.BooleanField(default=True)

    def __str__(self):
            return self.staff_username



# Create your models here.
