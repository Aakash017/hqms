from django.db import models
class UserRole(models.Model):
    role_id=models.AutoField(primary_key=True)
    role_name=models.CharField(max_length=255,default="",unique=True)

    def __str__(self):
     return self.role_name

class myuser(models.Model):
    user_roleid = models.ForeignKey(UserRole,on_delete=models.CASCADE,default="")
    #user_id=models.AutoField(primary_key=True)
    user_username= models.CharField(max_length=255,default="")
    user_password=models.CharField(max_length=20,default="")
    user_email=models.EmailField(primary_key=True,max_length=255,default="",unique=True)
    user_mobile=models.CharField(max_length=255,default="")
    user_gender=models.CharField(max_length=20,default="")
    user_dob=models.CharField(max_length=255,default="")
    user_image= models.CharField(max_length=255,null=True)

    user_isactive=models.BooleanField(default=True)

    def __str__(self):
            return self.user_username


