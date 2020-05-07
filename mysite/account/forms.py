from django.forms import ModelForm 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms 
from .models import cust

class CustsForm(ModelForm):
    class Meta:
        model = cust
        fields = '__all__'
        exclude = ['user']