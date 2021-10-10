from django.db import models
from django.db.models.fields import EmailField


# contact form model
class Contact(models.Model):    
    name=models.CharField(max_length=200,null=False,)
    email=models.EmailField(unique=True,null=False)
    phone=models.BigIntegerField(unique=True,null=False)
    message=models.CharField(max_length=1000,blank=False,null=True)

# signup form models
class SignUp(models.Model):
    first_name=models.CharField(max_length=150,null=False)
    last_name=models.CharField(max_length=150,null=False)
    email=models.EmailField(max_length=200,unique=True,null=False)
    password=models.CharField(max_length=150,null=False)
    def __str__(self):
        return self.email

#Profile model form
class Profile(models.Model):
    user=models.OneToOneField(SignUp,on_delete=models.CASCADE)
    token=models.CharField(max_length=100, null=False)
    is_verified=models.BooleanField(default=False)
    created_date=models.DateTimeField(auto_now_add=True)
    