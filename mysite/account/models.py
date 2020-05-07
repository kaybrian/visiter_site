from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# Create your models here.

class cust(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=50,null=True)
    profile_pic = models.ImageField(null=True)
    phone = models.CharField(max_length=50,null=True)
 
    def __str__(self):
        return self.name

class Create_user_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        